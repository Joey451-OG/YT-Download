from yt_dlp import YoutubeDL
import os
url = "https://youtu.be/yModCU1OVHY"

settings = {'outtmpl': '~/home/joey/YT-Download/%(title)s.%(ext)s',
	    'verbose': True}

with YoutubeDL(settings) as ydl:
    ydl.download(url)
