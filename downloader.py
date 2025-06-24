import os
from yt_dlp import YoutubeDL

def download_video(url: str, format: str = "best",  output_path: str = "downloads/"):
    """
    downloads video from given URL to specified path
    uses yt-dlp for downloading
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    if not url:
        raise ValueError("URL cannot be empty")
    
    if not isinstance(url, str):
        raise TypeError("URL must be a string")
    
    if format not in ["best", "worst", "mp4", "webm"]:
        raise ValueError("Format must be one of: 'best', 'worst', 'mp4', 'webm'")
    
    ydl_options = {
        'format': format,
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'noplaylist': True,
        'quiet': False,
    }
    
    with YoutubeDL(ydl_options) as ydl:
        try:
            ydl.download([url])
            print(f"Downloaded video from {url} to {output_path}")
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
    return True
