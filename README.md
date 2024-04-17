#Discord Notification Bot

###Overview
This Discord bot notifies users about various events happening on different platforms such as Reddit, TikTok, Twitch, and YouTube. It is designed to run continuously in the background and send notifications to a dedicated channel on a Discord server.

###Features
Reddit Notifications: Monitors a subreddit for new posts and sends notifications to Discord.
TikTok Notifications: Scrapes a TikTok profile for new content and sends notifications to Discord.
Twitch Notifications: Monitors a Twitch channel for live streams and sends notifications to Discord.
YouTube Notifications: Monitors a YouTube channel for new videos and sends notifications to Discord.

###Setup
Clone this repository to your local machine.
Create a virtual environment and activate it.

bash

python -m venv .venv
.\.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

Install the required dependencies.

bash

pip install -r requirements.txt

Obtain API keys and tokens for Discord, Reddit, TikTok, Twitch, and YouTube.
Update the config.py file with your API keys, tokens, and channel IDs.
Run the bot using the following command:

bash

python bot.py

Configuration
Discord Configuration: Set your Discord bot token, server ID, and notification channel ID in config.py.
Reddit Configuration: Set your Reddit client ID, client secret, user agent, and subreddit name in config.py.
TikTok Configuration: Set your TikTok username in config.py.
Twitch Configuration: Set your Twitch client ID, client secret, access token, and channel name in config.py.
YouTube Configuration: Set your YouTube API key and channel ID in config.py.
Usage
Once the bot is running, it will automatically monitor the specified platforms for new content and send notifications to the designated Discord channel.
