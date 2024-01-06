import json
import subprocess

# YouTube user URL
user_url = "https://www.youtube.com/@RapperViperVEVO/videos"

# Function to download videos and extract information
def download_videos_and_save_info():
    try:
        # Run youtube-dl to download video information
        command = f"youtube-dl -j --flat-playlist {user_url}"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

        if process.returncode != 0:
            print(f"Error fetching video information: {error.decode('utf-8')}")
            return

        # Parse JSON output
        videos_info = [json.loads(line) for line in output.decode('utf-8').split('\n') if line]

        # Extract title and URL for each video
        videos_data = [{'title': video['title'], 'url': video['url']} for video in videos_info]

        # Save the result to a JSON file
        with open('videos_info.json', 'w') as json_file:
            json.dump(videos_data, json_file, indent=2)

        print('Videos information fetched and saved to videos_info.json')

    except Exception as e:
        print(f"Error: {e}")

# Execute the function
download_videos_and_save_info()
