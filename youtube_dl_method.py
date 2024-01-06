import youtube_dl
import json
import os

# YouTube user URL
user_url = 'https://www.youtube.com/@RapperViperVEVO/videos'

# Output file for video information
output_file = 'videos.json'

# Output directory for downloaded videos
download_directory = '/media/jhare/data/viper'

# Function to download videos and save their titles and URLs
def download_videos(url, output_file, download_dir):
    ydl_opts = {
        'quiet': False,
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        with open(output_file, 'r') as json_file:
            videos_info = json.load(json_file)

            for video in videos_info:
                video_url = video['url']
                print(f'Downloading video: {video["title"]}')
                ydl.download([video_url])

    print(f'All videos downloaded to {download_dir}')

# Execute the function
download_videos(user_url, output_file, download_directory)
