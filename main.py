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

config_path = 'config.yml'

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

default_config = {
    'version': '1.3.1',

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
        
        self.config_path = 'config.yml'
        update_file = False
        
        if platform == 'win32': # Check if YT-Download is running on windows and change config file path.
            self.config_path = self.check_for_OneDrive()
            if not os.path.exists(self.config_path):
                os.makedirs(self.config_path)

            if not os.path.exists(self.config_path + '\\config.yml'): # Write the config file using default config settings if the file does not exist.
                with open(self.config_path + '\\config.yml', 'w') as file:
                    yaml.dump(default_config, file, sort_keys=False)    
                file.close()        

            self.config_path = self.config_path + r'\\config.yml' # Update self.config_path to point to the actual config file
        
        with open(self.config_path, 'r') as file:
            # Update config file if version numbers differ
            cfg = yaml.load(file, yaml.FullLoader)
            if cfg['version'] != default_config['version']: 
                cfg['version'] = default_config['version'] # Update the version number
                for item in default_config.keys():
                    if item not in cfg.keys(): # Only add new settings to the config file. This maintains any settings the user has made before updating.
                        cfg[item] = default_config[item]
                        update_file = True # Allows the updated config to be dumped to the file
        
                cfg['version'] = default_config['version']
            file.close()

            if update_file: # Dump the new settings
                with open(self.config_path, 'w') as file:
                    yaml.dump(cfg, file, sort_keys=False)
                file.close()
        
        self.update_class_vars()
    
    # Sets and dumps the new changes made by a user in the Settings Menu (see YT Download.py)
    def update_config_file(self, settings_list: list) -> None:
        with open(self.config_path, 'r') as file:
            cfg = yaml.load(file, Loader=yaml.FullLoader)
            # See YT Download.py (starting at line X) for reason why settings_list is not a dictionary

            # If anyone knows a better way to do this please make a PR!
            cfg['Directory_Settings']['use_default_directory'] = settings_list[0]
            cfg['Directory_Settings']['custom_default_directory'] = settings_list[1]
            cfg['Popup_Settings']['playlist_confirmation'] = settings_list[2]
            cfg['Popup_Settings']['file_downloaded'] = settings_list[3]
            cfg['Miscellaneous_Settings']['default_as_audio'] = settings_list[4]
            cfg['Miscellaneous_Settings']['color_theme'] = settings_list[5]
        file.close()
        
        with open(self.config_path, 'w') as file:
            yaml.dump(cfg, file, sort_keys=False)
        file.close()
    
    # Update class variables so they can be used elsewhere
    def update_class_vars(self) -> None: 
        with open(self.config_path, 'r') as file:
            cfg = yaml.load(file, Loader=yaml.FullLoader)
            # Directory Settings
            self.use_default_directory = cfg['Directory_Settings']['use_default_directory']
            self.custom_default_directory = cfg['Directory_Settings']['custom_default_directory']
            # Popup Settings
            self.playlist_confirmation = cfg['Popup_Settings']['playlist_confirmation']
            self.file_downloaded = cfg['Popup_Settings']['file_downloaded']
            # Miscellaneous Settings
            self.default_as_audio = cfg['Miscellaneous_Settings']['default_as_audio']
            self.color_theme = cfg['Miscellaneous_Settings']['color_theme']
            self.version = cfg['version']

            file.close()
    
    # Check if the OneDrive folder exists and return the actual Documents path (WINDOWS ONLY)
    def check_for_OneDrive(self) -> str: 
        userprofile = os.getenv('USERPROFILE')
        if os.path.exists(f'{userprofile}\\OneDrive'):
            return f'{userprofile}\\OneDrive\\Documents\\YT Download'
        else:
            return f'{userprofile}\\Documents\\YT Download'

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
