import os
import yt_dlp
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def download_youtube_video(url, path='.'):
    # Ensure the directory exists
    if not os.path.exists(path):
        os.makedirs(path)

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': f'{path}/%(title)s.%(ext)s'
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        logging.info("Download successful!")
        return True
    except yt_dlp.utils.DownloadError as e:
        logging.error(f"Download error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    
    return False

# Example usage
if __name__ == "__main__":
    url = input("Enter the YouTube video URL: ")
    download_youtube_video(url, path='./videos')