import praw
from config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT, SUBREDDIT_NAME

reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID, client_secret=REDDIT_CLIENT_SECRET, user_agent=REDDIT_USER_AGENT)

def monitor_subreddit():
    subreddit = reddit.subreddit(SUBREDDIT_NAME)
    for submission in subreddit.stream.submissions():
        send_reddit_notification(submission)

async def send_reddit_notification(submission):
    channel = discord_bot.get_channel(NOTIFICATION_CHANNEL_ID)
    await channel.send(f'New post on r/{subreddit_name}: {submission.title} - {submission.url}')
