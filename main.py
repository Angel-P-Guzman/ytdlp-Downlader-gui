# gui and main program logic
import sys
import tkinter as tk
from downloader import download_video
from formats import get_all_formats, is_valid_format, get_default_format


def main():
    root = tk.Tk()
    root.title("YouTube Downloader")
    root.geometry("600x400")
    root.resizable(False, False)
    
    #downloader = download_video("")
    #gui = downloader.create_gui(root)
   
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

def on_closing():
    print("Closing the application.")
    sys.exit(0)
    
        
if __name__ == "__main__":
    main()

# This is the main entry point for the YouTube Downloader application.
# It initializes the GUI and starts the main event loop.
# The Downloader class handles the downloading logic, while the GUI class manages the user interface.
