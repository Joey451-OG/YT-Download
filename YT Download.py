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

import PySimpleGUI as sg
import main as downloader
import webbrowser as web
import os
from sys import platform
cfg = downloader.config()
downloader.terminal_msgs(0, 0)
sg.theme(cfg.color_theme) # Color Scheme

# OS based default directory lookup
downloader.terminal_msgs(0, 1)
if cfg.use_default_directory:  
    if platform == 'win32':
        user_dir = os.environ['USERPROFILE'] + '\Documents\YT Download'
        logo = 'logo.ico'
    if platform == 'linux' or platform == 'linux2':
        user_dir = '~/Documents/YT-Download'
        logo = 'logo.png'
else:
    user_dir = cfg.custom_default_directory
    if platform == 'win32':
        logo = 'logo.ico'
    if platform == 'linux' or platform == 'linux2':
        logo = 'logo.png'

font = (None, 10, 'underline')


# GUI layout
layout = [ [sg.Text("Thank you for using YT Download!")],
           [sg.Text("YouTube URL:"), sg.InputText(key='URL')],
           [sg.Checkbox('Download as an audio file (mp3)?', default=cfg.default_as_audio, key='isAudio')],
           [sg.Text('File path. Leave blank to save download to:')],
           [sg.Text(f'{user_dir}')],
           [sg.Input(key='DIR'), sg.FolderBrowse()],
           [sg.Button('Download'), sg.Cancel(), sg.Text('Version: 1.3.0', tooltip='https://github.com/Joey451-OG/YT-Dowload', enable_events=True, key='GITHUB', font=font)]
    ]

# Main logic function. Calls the appropriate functions in main.py and handles input errors.
def GUI_checks(audio_val: str, url_val: str, dir_val: str):
    
    
    download = True
    
    if 'playlist?list=' in url_val and cfg.playlist_confirmation: # URL is a playlist and playlist confirmation is True
        playlist_window = sg.Window('YT Download', playlist_layout, icon=logo)
        
        while True: # Open the confirmation popup
            p_event, p_val = playlist_window.read()
            print(p_event, p_val)
            if p_event == 'Yes': # If yes, continue downloading and close the popup
                playlist_window.close()
                break
                
            elif p_event == 'No' or p_event == sg.WIN_CLOSED: # If no (or popup was closed), stop downloading and close the popup
                sg.popup('Not downloading playlist...', icon=logo, title='YT Download')
                playlist_window.close()
                download = False
                break

    if download:
        # Reason for setting title to playlist
        '''
        I set the title to playlist first to handle the condition in which the user is trying to download a playlist.
        title will be changed if the user is not downloading a playlist.
        '''
        title = 'playlist'

        if 'playlist?list=' not in url_val:
            title = downloader.return_title(url_val)
        
        if dir_val == '': # Check to see if user wants to use the default dir
            dir_val = user_dir
        
        if audio_val: # Check to see if the user want to download as an audio file
            file_type = '.mp3'
        else:
            file_type = '.mp4'

        
        if url_val == '': # Check to see if the url field is empty, then warn the user if it is.
            sg.popup('Please make sure to provide a URL', icon=logo, title='YT Download')
        else:
            if title == 'ERROR': # Check for an invalid url
                sg.popup('INVALID YOUTUBE URL', icon=logo, title='YT Download')
                title = False

            if title != False: # Start downloading
                yt_download = downloader.logic(url_val, audio_val, dir_val)

                if yt_download == 'FFMPEG ERROR': # Check for a FFMPEG error
                    sg.popup('It looks like FFmpeg is not installed. Try reinstalling YT Download or add FFmpeg to the PATH manually.', icon=logo, title='YT Download')
                elif cfg.file_downloaded: # Downloaded confirmation popup
                    sg.popup(f'Downloaded {title} as a {file_type} file to {dir_val}', icon=logo, title='YT Download')
            

# Main setup loop. Calls GUI_checks()
downloader.terminal_msgs(0, 2)
window = sg.Window('YT Download', layout, icon=logo)
while True:
    
    playlist_layout = [
        [sg.Text('You are trying to download a Playlist. Do you want to continue?')],
        [sg.Button('Yes'), sg.Button('No')]
    ]

    event, values = window.read() # Check the active event and the value dictionary.
    print(event, values) # Print event and values for debugging in the command line.

    if event == sg.WIN_CLOSED or event == 'Cancel': # Break the loop if the window is closed or the 'Cancel' button is pressed
        break
    
    if event == 'GITHUB': # If the linked is clicked, open the GitHub repo.
        web.open("https://github.com/Joey451-OG/YT-Dowload")

    if event == 'Download': # Was the Download button pressed?
        GUI_checks(values['isAudio'], values['URL'], values['DIR'])

window.close() # Kill the program
