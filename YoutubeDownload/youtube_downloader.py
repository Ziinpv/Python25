import tkinter as tk
from tkinter import ttk, messagebox
from yt_dlp import YoutubeDL
import threading
import re
from tkinter import filedialog
import os

class YoutubeDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Video Downloader")
        self.root.geometry("800x500")
        self.root.configure(bg="#f0f0f0")

        # Style
        self.style = ttk.Style()
        self.style.configure("Custom.TFrame", background="#f0f0f0")
        self.style.configure("Custom.TButton", padding=10, font=('Helvetica', 10))
        self.style.configure("Custom.TLabel", background="#f0f0f0", font=('Helvetica', 10))

        # Main frame
        self.main_frame = ttk.Frame(root, style="Custom.TFrame", padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # URL Entry
        self.url_label = ttk.Label(self.main_frame, text="Nhập URL YouTube:", style="Custom.TLabel")
        self.url_label.pack(pady=5)

        self.url_entry = ttk.Entry(self.main_frame, width=70)
        self.url_entry.pack(pady=5)

        # Download location
        self.location_frame = ttk.Frame(self.main_frame, style="Custom.TFrame")
        self.location_frame.pack(fill=tk.X, pady=10)

        self.location_label = ttk.Label(self.location_frame, text="Vị trí lưu:", style="Custom.TLabel")
        self.location_label.pack(side=tk.LEFT, padx=5)

        self.location_entry = ttk.Entry(self.location_frame, width=50)
        self.location_entry.pack(side=tk.LEFT, padx=5)
        self.location_entry.insert(0, os.path.expanduser("~/Downloads"))

        self.browse_button = ttk.Button(self.location_frame, text="Chọn thư mục", 
                                      command=self.browse_location, style="Custom.TButton")
        self.browse_button.pack(side=tk.LEFT, padx=5)

        # Quality Selection
        self.quality_label = ttk.Label(self.main_frame, text="Chất lượng:", style="Custom.TLabel")
        self.quality_label.pack(pady=5)

        self.quality_var = tk.StringVar(value="best")
        qualities = [
            ("Chất lượng cao nhất", "best"),
            ("720p", "720"),
            ("480p", "480"),
            ("360p", "360")
        ]

        self.quality_frame = ttk.Frame(self.main_frame, style="Custom.TFrame")
        self.quality_frame.pack(pady=5)

        for text, value in qualities:
            ttk.Radiobutton(self.quality_frame, text=text, value=value, 
                           variable=self.quality_var).pack(side=tk.LEFT, padx=10)

        # Download Button
        self.download_button = ttk.Button(self.main_frame, text="Tải xuống", 
                                        command=self.start_download, style="Custom.TButton")
        self.download_button.pack(pady=20)

        # Progress
        self.progress_label = ttk.Label(self.main_frame, text="", style="Custom.TLabel")
        self.progress_label.pack(pady=5)

        self.progress_bar = ttk.Progressbar(self.main_frame, length=400, mode='determinate')
        self.progress_bar.pack(pady=5)

    def browse_location(self):
        directory = filedialog.askdirectory()
        if directory:
            self.location_entry.delete(0, tk.END)
            self.location_entry.insert(0, directory)

    def update_progress(self, d):
        if d['status'] == 'downloading':
            try:
                progress = float(d['_percent_str'].replace('%',''))
                self.progress_bar['value'] = progress
                self.progress_label['text'] = f"Đang tải: {d['_percent_str']}"
                self.root.update()
            except:
                pass
        elif d['status'] == 'finished':
            self.progress_label['text'] = "Tải xuống hoàn tất!"
            messagebox.showinfo("Thành công", "Video đã được tải xuống thành công!")
            self.progress_bar['value'] = 0
            self.download_button['state'] = 'normal'

    def download_video(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showerror("Lỗi", "Vui lòng nhập URL YouTube!")
            return

        if not re.match(r'^https?://(?:www\.)?youtube\.com/.*|^https?://(?:www\.)?youtu\.be/.*', url):
            messagebox.showerror("Lỗi", "URL không hợp lệ!")
            return

        quality = self.quality_var.get()
        download_path = self.location_entry.get()

        ydl_opts = {
            'format': f'bestvideo[height<={quality}]+bestaudio/best[height<={quality}]' 
                     if quality != 'best' else 'bestvideo+bestaudio/best',
            'progress_hooks': [self.update_progress],
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4'
        }

        try:
            self.download_button['state'] = 'disabled'
            self.progress_label['text'] = "Đang chuẩn bị tải xuống..."
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except Exception as e:
            messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {str(e)}")
            self.download_button['state'] = 'normal'
            self.progress_label['text'] = ""
            self.progress_bar['value'] = 0

    def start_download(self):
        thread = threading.Thread(target=self.download_video)
        thread.start()

if __name__ == "__main__":
    root = tk.Tk()
    app = YoutubeDownloader(root)
    root.mainloop() 