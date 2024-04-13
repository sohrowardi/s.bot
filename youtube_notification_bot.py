from googleapiclient.discovery import build
from config import YOUTUBE_API_KEY, YOUTUBE_CHANNEL_ID
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

def get_new_videos():
    request = youtube.search().list(part='snippet', channelId=YOUTUBE_CHANNEL_ID, order='date', type='video', maxResults=10)
    response = request.execute()
    return response['items']
