import discord
from discord.ext import commands
import praw
import requests
from bs4 import BeautifulSoup
from googleapiclient.discovery import build
from config import DISCORD_BOT_TOKEN, DISCORD_SERVER_ID, NOTIFICATION_CHANNEL_ID, \
    REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT, SUBREDDIT_NAME, \
    TIKTOK_USERNAME, TWITCH_CLIENT_ID, TWITCH_CLIENT_SECRET, TWITCH_ACCESS_TOKEN, TWITCH_CHANNEL_NAME, \
    YOUTUBE_API_KEY, YOUTUBE_CHANNEL_ID

# Initialize Discord bot
bot = commands.Bot(command_prefix='!')

# Initialize Reddit client
reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID, client_secret=REDDIT_CLIENT_SECRET, user_agent=REDDIT_USER_AGENT)

# Initialize YouTube client
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

# Function to send Reddit notification
async def send_reddit_notification(submission):
    channel = bot.get_channel(NOTIFICATION_CHANNEL_ID)
    await channel.send(f'New post on r/{SUBREDDIT_NAME}: {submission.title} - {submission.url}')

# Function to send TikTok notification
async def send_tiktok_notification():
    url = f'https://www.tiktok.com/@{TIKTOK_USERNAME}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Use BeautifulSoup to extract information about latest posts
    # Example: post_titles = soup.find_all('h2', class_='post-title')

# Function to send Twitch notification
@bot.event
async def event_ready():
    print(f'Logged in as {bot.nick}')

@bot.command(name='hello')
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.name}!')

# Function to send YouTube notification
def get_new_videos():
    request = youtube.search().list(part='snippet', channelId=YOUTUBE_CHANNEL_ID, order='date', type='video', maxResults=10)
    response = request.execute()
    return response['items']

# Command to greet users
@bot.command(name='hello', help='Responds with a greeting.')
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.mention}!')

# Command to echo user input
@bot.command(name='echo', help='Repeats your message.')
async def echo(ctx, *, message):
    await ctx.send(message)

# Event handler for when the bot is ready
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

    # Monitor subreddit
    subreddit = reddit.subreddit(SUBREDDIT_NAME)
    for submission in subreddit.stream.submissions():
        await send_reddit_notification(submission)

    # Monitor TikTok profile
    await send_tiktok_notification()

    # Monitor YouTube channel
    while True:
        new_videos = get_new_videos()
        # Process new videos and send notifications

# Run the Discord bot
bot.run(DISCORD_BOT_TOKEN)
