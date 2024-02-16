import tkinter as tk
from tkinter import messagebox
import yt_dlp
import os

def duration_converter(seconds):
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def clear_all_content():
    entry_widget.delete(0, tk.END)
    label_title.config(text='')
    label_length.config(text='')

def paste_url():
    try:
        entry_widget.delete(0, tk.END)
        latestClipboardValue = window.clipboard_get()
        entry_widget.insert(0, latestClipboardValue)
    except:
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, 'Nothing Copied')

def search_content():
    try:
        url = entry_widget.get()
        ydl_opts = {}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            title = info.get('title', 'N/A')
            length = info.get('duration', 'N/A')
            length = duration_converter(length)
            print("Title: " + title)
            print("Length: " + length)
            label_title.config(text=title)
            label_length.config(text=length)
    except:
        label_title.config(text='Not found. Please check the video link.')
        label_length.config(text='')

def pop_up_info():
    messagebox.showinfo('', 'Audio Downloaded.')

def download():
    print('DOWNLOAD STARTED')
    url = entry_widget.get()
    format_id='140' # Container: M4A, Audio Codec AAC(LC), Audio Bitrate:128Kbps, Chanels: Stereo(2)
    ydl_opts = {'format': format_id}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
    print('DOWNLOAD FINISHED')
    pop_up_info()

def open_folder():
    # Get the current directory where the Python file is located
    current_directory = os.path.dirname(os.path.realpath(__file__))
    # Open the directory
    os.system(f'explorer {current_directory}')

def window_geometry(window):
    # set window's resolution 
    window_width = 640
    window_height = 250
    # disable window resizing
    window.resizable(False, False)
    # get the client's screen resolution
    client_screen_width = window.winfo_screenwidth()
    client_screen_height = window.winfo_screenheight()
    # find the center point
    centerX = int(client_screen_width/2 - window_width / 2)
    centerY = int(client_screen_height/2 - window_height / 2)
    # center the window 
    window.geometry(f'{window_width}x{window_height}+{centerX}+{centerY}')
    # set the window's icon
    window.iconbitmap('./assets/windowIcon256.ico')

window = tk.Tk()
window.title('YouTube Audio Downloader')
window_geometry(window)

# 1st Frame
frame1 = tk.Frame(window)
frame1.pack()
# Label widget to inform the user about pop-up
label_pop_remainder = tk.Label(frame1, text="You will be informed with pop-up when download is finished.")
label_pop_remainder.pack()
# Entry widget for links
entry_widget = tk.Entry(frame1, width=120)
entry_widget.pack(padx=10)
# Buttons
clear_button = tk.Button(frame1, command=clear_all_content, text="Clear", width=10)
clear_button.pack(side=tk.LEFT, padx=(10, 2.5), pady=5)
paste_button = tk.Button(frame1, text="Paste", command=paste_url, width=10)
paste_button.pack(side=tk.LEFT, padx=(2.5, 2.5), pady=5)
search_button = tk.Button(frame1, text="Search", command=search_content, width=90)
search_button.pack(side=tk.RIGHT, padx=(2.5, 10), pady=5)

# 2nd Frame
frame2 = tk.Frame(window, width=620, height=40)
frame2.pack(pady=5)
frame2.pack_propagate(0)
# Label widgets for showing audio informations.
label_title=tk.Label(frame2)
label_title.pack()
label_length=tk.Label(frame2)
label_length.pack()

# 3rd Frame
frame3 = tk.Frame(window)
frame3.pack(pady=5)
# Buttons
download_button = tk.Button(frame3, text='DOWNLOAD', command=download, width=60 , height=5)
download_button.pack(side=tk.LEFT, padx=(10, 5))
openFolder_button = tk.Button(frame3, text='Open Folder', command=open_folder, width=40, height=5)
openFolder_button.pack(side=tk.RIGHT, padx=(5, 10))

# 4th Frame
frame4 = tk.Frame(window)
frame4.pack(pady=(0,5))
# Label widget to inform the user about copyright rules
label_copyright_info = tk.Label(frame4, text="Please follow COPYRIGHT rules. This project has been developed for hobby purposes.")
label_copyright_info.pack()

window.mainloop()
