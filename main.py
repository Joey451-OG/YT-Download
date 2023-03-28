# LICENSE
'''
YT Download. A simple GUI wrapper for yt-dlp.
    Copyright (C) 2023  Joey451-OG

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

from yt_dlp import YoutubeDL, utils

print('TERMINAL Please keep this window open for YT Download to work.\n') # Only is seen in the Command Line. Anything that prints to the console will only be seen in the command line.

video_options = {
    # Download the best mp4 video available, or the best video if no mp4 available ["..." COPIED FROM: https://github.com/yt-dlp/yt-dlp#format-selection-examples]
    'format': "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4] / bv*+ba/b"
}

audio_options = {
    'format': 'm4a/bestaudio/best',
    'postprocessors': [{ #FFmpeg Settings see: |yt-dlp/__init__.py --> .postprocessor| for a list of settings.
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3'
    }]
}


# Handels downlaoding and retriving information
def YoutubeDownloader(settings: dict, url: str):
    with YoutubeDL(settings) as ydl:
        try:
            ydl.download(url)
        except utils.DownloadError:
            return 'FFMPEG ERROR'    

# Main logic. Sets directory when specified and calls YoutubeDownloader()
def logic(URL: str, ISaudio: bool, DIR: str):
   
   
    audio_options['outtmpl'] = DIR + '/%(title)s.%(ext)s'
    video_options['outtmpl'] = DIR + '/%(title)s.%(ext)s'                
    
    if ISaudio: # Download as audio or video
        return YoutubeDownloader(audio_options, URL, True)
    else:
        return YoutubeDownloader(video_options, URL, True)
    
# Returns the title of video the url points to.
def return_title(url: str):
    with YoutubeDL() as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            return info['title']
        except utils.DownloadError: # Invalid YouTube url error.
            return 'ERROR'


'''
Usefull testing things:

https://youtu.be/I8sUC-dsW8A
'''
