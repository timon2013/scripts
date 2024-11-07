import os
import yt_dlp
import logging
from urllib.parse import urlparse

# Set up logging
logging.basicConfig(level=logging.INFO)

def download_video(url, path='.'):
    # Ensure the directory exists
    os.makedirs(path, exist_ok=True)

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(path, '%(title)s.%(ext)s')
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

def get_domain(url):
    return urlparse(url).netloc

SUPPORTED_DOMAINS = {
    'youtube.com', 'youtu.be', 'odysee.com'
}

if __name__ == "__main__":
    url = input("Enter the video URL (YouTube or Odysee): ")
    path = input("Enter the download path (press Enter for current directory): ") or '.'

    domain = get_domain(url)
    if any(supported in domain for supported in SUPPORTED_DOMAINS):
        if download_video(url, path):
            print("Download completed successfully.")
        else:
            print("Download failed.")
    else:
        logging.error("Unsupported URL. Please enter a YouTube or Odysee URL.")