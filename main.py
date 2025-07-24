# gui and main program logic
import sys
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from downloader import download_video
from formats import get_format_names, get_default_format
import threading

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # for PyInstaller
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def start_download(url, fmt, output_path, status_label, download_button):
    def run():
        download_button.config(state=tk.DISABLED)
        status_label.config(text="Downloading...", fg="blue")
        try:
            success = download_video(url, fmt, output_path)
            if success:
                status_label.config(text="Download complete!", fg="green")
            else:
                status_label.config(text="Download failed.", fg="red")
        except Exception as e:
            status_label.config(text=f"Error: {e}", fg="red")
        download_button.config(state=tk.NORMAL)
    threading.Thread(target=run).start()

def main():
    root = tk.Tk()
    root.title("YouTube Downloader")
    root.geometry("500x250")
    root.resizable(False, False)

    # URL input
    tk.Label(root, text="YouTube URL:").pack(anchor="w", padx=10, pady=(10, 0))
    url_var = tk.StringVar()
    url_entry = tk.Entry(root, textvariable=url_var, width=60)
    url_entry.pack(padx=10, pady=2)

    # Format dropdown
    tk.Label(root, text="Format:").pack(anchor="w", padx=10, pady=(10, 0))
    format_var = tk.StringVar(value=get_default_format())
    format_names = get_format_names()
    format_menu = ttk.Combobox(root, textvariable=format_var, values=format_names, state="readonly")
    format_menu.pack(padx=10, pady=2)

    # Output folder selection
    tk.Label(root, text="Download Folder:").pack(anchor="w", padx=10, pady=(10, 0))
    output_path_var =  tk.StringVar(value=resource_path("downloads/"))
    folder_frame = tk.Frame(root)
    folder_frame.pack(fill="x", padx=10, pady=2)
    folder_entry = tk.Entry(folder_frame, textvariable=output_path_var, width=45)
    folder_entry.pack(side="left", fill="x", expand=True)
    def choose_folder():
        folder = filedialog.askdirectory()
        if folder:
            output_path_var.set(folder)
    tk.Button(folder_frame, text="Browse", command=choose_folder).pack(side="left", padx=5)

    # Status label
    status_label = tk.Label(root, text="", fg="blue")
    status_label.pack(pady=(10, 0))

    # Download button
    def on_download():
        url = url_var.get().strip()
        fmt = format_var.get()
        output_path = output_path_var.get().strip()
        if not url:
            messagebox.showerror("Error", "Please enter a YouTube URL.")
            return
        if not fmt:
            messagebox.showerror("Error", "Please select a format.")
            return
        if not output_path:
            messagebox.showerror("Error", "Please select a download folder.")
            return
        start_download(url, fmt, output_path, status_label, download_button)

    download_button = tk.Button(root, text="Download", command=on_download)
    download_button.pack(pady=10)

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()
            sys.exit(0)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()
