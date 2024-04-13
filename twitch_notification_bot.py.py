from twitchio.ext import commands
from config import TWITCH_CLIENT_ID, TWITCH_CLIENT_SECRET, TWITCH_ACCESS_TOKEN, TWITCH_CHANNEL_NAME
bot = commands.Bot(token=TWITCH_ACCESS_TOKEN, client_id=TWITCH_CLIENT_ID, nick='YOUR_TWITCH_BOT_USERNAME', prefix='!')

@bot.event
async def event_ready():
    print(f'Logged in as {bot.nick}')

@bot.command(name='hello')
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.name}!')

bot.run()
