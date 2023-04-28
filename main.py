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
from sys import platform
import yaml
import os

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

default_config_state = {
    'Directory_Settings': {
        'use_default_directory': True,
        'custom_default_directory': 'paste\custom\default\directory\path\here'
    },

    'Popup_Settings': {
        'playlist_confirmation': True,
        'file_downloaded': True    
    },

    'Miscellaneous_Settings': {
        'default_as_audio': False,
        'color_theme': 'DarkAmber'
    }
}

# Handles the config file
class config:
    def __init__(self) -> None:
        # Check if YT-Download is running on windows and change config file path.
        config_path = 'config.yml'
        if platform == 'win32':
            config_path = r'%PROGRAMDATA%\\YT Download\\config.yml'

        if os.path.exists(config_path):
            # Update config file while not overwriting the entire file.
            with open(config_path, 'r+') as file:
                current_config = yaml.load(file, Loader=yaml.FullLoader)
                for item in default_config_state:
                    if item not in current_config:
                        current_config[item]
                    
        else:
            # Config file does not exist, write the config file with default configuration.
            with open(config_path, 'w') as file:
                file.write(yaml.dump(default_config_state))
        
        with open(config_path, 'r') as file:
            self.cfg = yaml.load(file, Loader=yaml.FullLoader)
            # Directory Settings
            self.use_default_directory = self.cfg['use_default_directory']
            self.custom_default_directory = self.cfg['custom_default_directory']
            # Popup Settings
            self.playlist_confirmation = self.cfg['playlist_confirmation']
            self.file_downloaded = self.cfg['file_downloaded']
            # Miscellaneous Settings
            self.default_as_audio = self.cfg['default_as_audio']
            self.color_theme = self.cfg['color_theme']


# Handles downloading and retrieving information
def YoutubeDownloader(settings: dict, url: str):
    with YoutubeDL(settings) as ydl:
        try:
            ydl.download(url)
        except utils.DownloadError:
            return 'FFMPEG ERROR'    

# Main logic. Sets directory and calls YoutubeDownloader()
def logic(URL: str, ISaudio: bool, DIR: str):
    terminal_msgs(0, 3)
    audio_options['outtmpl'] = DIR + '/%(title)s.%(ext)s'
    video_options['outtmpl'] = DIR + '/%(title)s.%(ext)s'                
    
    terminal_msgs(0, 4)
    if ISaudio: # Download as audio or video
        return YoutubeDownloader(audio_options, URL)
    else:
        return YoutubeDownloader(video_options, URL)
    
# Returns the title of video the url points to.
def return_title(url: str):
    with YoutubeDL() as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            return info['title']
        except utils.DownloadError: # Invalid YouTube url error.
            return 'ERROR'

# Prints terminal messages
def terminal_msgs(dic: int, key: int):
    operational = {
        0: 'TERMINAL Please keep this window open for YT Download to work.\n', # Only is seen in the Command Line. Anything that prints to the console will only be seen in the command line.
        1: '\nDetecting OS...\n',
        2: '\nInitializing application windows...\n',
        3: '\nSelecting directory...\n',
        4: '\nDownloading...\n'
    }

    if dic == 0:
        print(operational[key]) # I might add more dictionaries to this function so this code isn't redundant
'''
Useful testing things:

One video
https://youtu.be/I8sUC-dsW8A

Playlist
https://youtube.com/playlist?list=PLq-8SN7V15mnk7-hLp2i7Lwh7gPZwkFoX
'''
