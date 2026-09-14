from pytubefix import YouTube
import tkinter as tk
from tkinter import filedialog


def download_video(url, save_path):
    try:
        # 'ANDROID' client bypasses many signature and bot checks
        yt = YouTube(url, client="ANDROID")

        # get_highest_resolution() directly picks the highest available stream
        stream = yt.streams.get_highest_resolution()

        if stream is None:
            # Fallback to the first available stream if highest_res isn't found
            stream = yt.streams.filter(file_extension="mp4").first()

        if stream:
            stream.download(output_path=save_path)
            print("Video downloaded successfully!")
        else:
            print("No downloadable stream found for this video.")

    except Exception as e:
        print(f"Error: {e}")


def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")

    return folder


# url = "https://www.youtube.com/watch?v=NpmFbWO6HPU&t=7137s"
# save_path = "../Data/"


if __name__ == "__main__":
    root = tk.Tk()  # initialize window
    root.withdraw()  # hide window

    video_url = input("Please enter a YouTube video url: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Started Downloading...")
        download_video(video_url, save_dir)
    else:
        print("Invalid save location ")
