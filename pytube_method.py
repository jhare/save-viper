import os
import json
from pytube import YouTube

# YouTube user URL
USER_URL = "https://www.youtube.com/@RapperViperVEVO/videos"

# Function to get video information from a YouTube user URL
def get_videos_info():
    try:
        # Create a YouTube object from the user URL
        user_channel = YouTube(USER_URL)

        # Extract video details (titles and URLs)
        videos = [{
            'title': video.title,
            'url': video.watch_url
        } for video in user_channel.video_urls]

        return videos
    except Exception as e:
        print(f"Error fetching video information: {e}")
        return None

# Save video information to a JSON file
def save_to_json(videos):
    if videos:
        with open('videos.json', 'w') as json_file:
            json.dump(videos, json_file, indent=2)
        print('Video information saved to videos.json')

# Download all videos from the YouTube user URL
def download_videos(videos):
    try:
        for video in videos:
            yt_video = YouTube(video['url'])
            video_stream = yt_video.streams.get_highest_resolution()
            print(f"Downloading: {video['title']}")
            video_stream.download('downloads')  # Downloads videos to 'downloads' folder

        print('All videos downloaded successfully.')
    except Exception as e:
        print(f"Error downloading videos: {e}")

# Main function
def main():
    videos_info = get_videos_info()

    if videos_info:
        save_to_json(videos_info)
        download_videos(videos_info)

if __name__ == "__main__":
    main()
