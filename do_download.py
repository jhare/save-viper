import json
from pytube import YouTube

# Function to download videos based on the JSON file
def download_videos_from_json(json_file):
    try:
        # Load JSON data from the file
        with open(json_file, 'r') as file:
            videos_data = json.load(file)

        # Loop through each video entry and download
        for video in videos_data:
            title = video['title']
            video_url = f"https://www.youtube.com/watch?v={video['url']}"

            # Specify the output path
            output_path = '/media/jhare/data/viper'
            try:
                # Download the video using Pytube
                yt = YouTube(video_url)
                stream = yt.streams.filter(file_extension='mp4', progressive=True).first()
                stream.download(output_path=output_path, filename=title)

                print(f"Downloaded '{title}' successfully")

            except Exception as e:
                print(f"Error downloading '{title}': {e}")

    except Exception as e:
        print(f"Error: {e}")

# Specify the JSON file containing video information
json_file_path = 'videos_info.json'

# Execute the function
download_videos_from_json(json_file_path)
