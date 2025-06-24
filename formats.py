#Predefines format/res choices
# might be useless, might be vestigial 
from typing import List

def get_available_formats() -> List[str]:
    """
    Returns a list of available video formats.
    """
    return ["best", "worst", "mp4", "webm"]

def is_valid_format(format: str) -> bool:
    """
    Checks if the provided format is valid.
    """
    valid_formats = get_available_formats()
    return format in valid_formats

def get_default_format() -> str:
    """
    Returns the default video format.
    """
    return "best"

def get_format_extension(format: str) -> str:
    """
    Returns the file extension for the given format.
    """
    format_extensions = {
        "best": "mp4",
        "worst": "mp4",
        "mp4": "mp4",
        "webm": "webm"
    }
    return format_extensions.get(format, "mp4")  # Default to mp4 if format is not recognized

def get_format_description(format: str) -> str:
    """
    Returns a description for the given format.
    """
    format_descriptions = {
        "best": "Best quality available",
        "worst": "Lowest quality available",
        "mp4": "Standard MP4 format",
        "webm": "WebM format, suitable for web use"
    }
    return format_descriptions.get(format, "Unknown format")

def get_all_formats() -> List[dict]:
    """
    Returns a list of dictionaries containing format details.
    Each dictionary contains 'name', 'extension', and 'description'.
    """
    formats = get_available_formats()
    return [
        {
            "name": fmt,
            "extension": get_format_extension(fmt),
            "description": get_format_description(fmt)
        }
        for fmt in formats
    ]

def get_format_by_name(name: str) -> dict:
    """
    Returns a dictionary containing details of the format by its name.
    If the format does not exist, returns an empty dictionary.
    """
    formats = get_all_formats()
    for fmt in formats:
        if fmt["name"] == name:
            return fmt
    return {}

def get_format_names() -> List[str]:
    """
    Returns a list of format names.
    """
    return [fmt["name"] for fmt in get_all_formats()]

def get_format_extensions() -> List[str]:
    """
    Returns a list of format file extensions.
    """
    return [fmt["extension"] for fmt in get_all_formats()]

def get_format_descriptions() -> List[str]:
    """
    Returns a list of format descriptions.
    """
    return [fmt["description"] for fmt in get_all_formats()]
