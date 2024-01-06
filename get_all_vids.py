import os
import json
from googleapiclient.discovery import build

# Set your API key and YouTube channel name

# Get API key from environment variable
API_KEY = os.environ.get('API_KEY')
CHANNEL_NAME = os.environ.get('CHANNEL_NAME')

# Create a YouTube Data API client
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Function to get the channel ID from the channel name
def get_channel_id():
    try:
        # Fetch the channel details for the specified channel name
        response = youtube.channels().list(
            part='id',
            forUsername=CHANNEL_NAME
        ).execute()

        # Extract the channel ID
        channel_id = response['items'][0]['id']

        return channel_id
    except Exception as e:
        print(f"Error fetching channel ID: {e}")
        return None

# Function to get the title and URL of all videos from a channel
def get_channel_videos():
    try:
        # Get the channel ID
        channel_id = get_channel_id()

        if channel_id:
            # Fetch the list of videos for the specified channel
            response = youtube.search().list(
                part='id',
                channelId=channel_id,
                type='video',
                maxResults=50  # Adjust as needed
            ).execute()

            # Extract video IDs
            video_ids = [item['id']['videoId'] for item in response['items']]

            # Fetch video details (titles and URLs)
            videos_details_response = youtube.videos().list(
                part='snippet',
                id=','.join(video_ids)
            ).execute()

            # Extract video details
            videos = [{
                'title': item['snippet']['title'],
                'url': f'https://www.youtube.com/watch?v={item["id"]}'
            } for item in videos_details_response['items']]

            # Save the result to a JSON file
            with open('videos.json', 'w') as json_file:
                json.dump(videos, json_file, indent=2)

            print('Videos information fetched and saved to videos.json')
    except Exception as e:
        print(f"Error fetching channel videos: {e}")

# Execute the function
get_channel_videos()
