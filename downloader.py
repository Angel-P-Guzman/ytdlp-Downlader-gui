import os
import logging
from yt_dlp import YoutubeDL
from typing import Optional

def download_video(
    url: str,
    format: str = "best",
    output_path: str = "downloads/",
    allow_playlist: bool = False,
    quiet: bool = False
) -> bool:
    """
    Download a video from the given URL to the specified path using yt-dlp.

    Args:
        url (str): The video URL.
        format (str): The format string for yt-dlp (default: "best").
        output_path (str): Directory to save the video (default: "downloads/").
        allow_playlist (bool): Whether to allow playlist downloads (default: False).
        quiet (bool): Suppress yt-dlp output (default: False).

    Returns:
        bool: True if download succeeded, False otherwise.

    Raises:
        ValueError: If url is empty or format is invalid.
        TypeError: If url is not a string.
    """
    if not url:
        raise ValueError("URL cannot be empty")
    if not isinstance(url, str):
        raise TypeError("URL must be a string")
    if not isinstance(format, str):
        raise TypeError("Format must be a string")

    # Normalize output path
    output_path = os.path.normpath(output_path)
    os.makedirs(output_path, exist_ok=True)

    ydl_options = {
        'format': format,
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'noplaylist': not allow_playlist,
        'quiet': quiet,
    }

    try:
        with YoutubeDL(ydl_options) as ydl:
            ydl.download([url])
        logging.info(f"Downloaded video from {url} to {output_path}")
        return True
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return False
