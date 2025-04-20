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

import FreeSimpleGUI as sg
import main as downloader
import webbrowser as web
from sys import platform

cfg = downloader.config()
downloader.terminal_msgs(1, 1)
sg.theme(cfg.color_theme) # Color Scheme

# OS based default directory lookup
downloader.terminal_msgs(1, 2)
if cfg.use_default_directory or (not cfg.use_default_directory and cfg.custom_default_directory == ''):
    if platform == 'win32':
        user_dir = cfg.check_for_OneDrive()
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
           [sg.Text(user_dir)],
           [sg.Input(key='DIR'), sg.FolderBrowse()],
           [sg.Button('Download'), sg.Button('Settings'), sg.Cancel(button_text='Exit'), sg.Push(), sg.Text(f'Version: {cfg.version}', tooltip='https://github.com/Joey451-OG/YT-Download', enable_events=True, key='GITHUB', font=font)]
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
                    sg.popup('It looks like FFmpeg is not installed. Try reinstalling FFmpeg or checking if it has been added to the PATH correctly.', icon=logo, title='YT Download')
                elif cfg.file_downloaded: # Downloaded confirmation popup
                    sg.popup(f'Downloaded {title} as a {file_type} file to {dir_val}', icon=logo, title='YT Download')
            
# Main logic behind the settings menu window. Calls appropriate functions in main.py.
def settings_menu():
    print(f'\n\n{"x" * 10}\nNOW ENTERING SETTINGS MENU. ALL EVENT/VALUE PAIRS ARE SPECIFIC TO THE SETTINGS WINDOW.\n{"x" * 10}\n\n')
    settings_window = sg.Window('YT Download', settings_layout, icon=logo)
    while True:
        s_event, s_value = settings_window.read()
        print(s_event, s_value)

        if s_event == sg.WIN_CLOSED or s_event == 'Exit': # Check to see if the user closes the settings window or clicks the EXIT button
            settings_window.close()
            break
        if s_event == 'Apply': # Check to see if the user clicks the APPLY button
            # Package the settings menu data
            s_value.pop('Browse') # Remove the data associated with the BROWSE key. This is duplicate information as the INPUT (key: 2) field. Since the INPUT field can be used independently of BROWSE, we keep it.
            setting_list = list(s_value.values())

            # Check for accidental overwrite of the custom default directory
            if not cfg.use_default_directory and s_value[2] == '':
                setting_list[1] = cfg.custom_default_directory
            
            # Check if user wants to revert to default settings
            if not setting_list[6]:
                # Send data to main.py for writing to config file
                cfg.update_config_file(setting_list)
            else:
                # Update config file with default settings
                cfg.apply_default_settings()
                

            # Restart YT Download
            settings_window.close()
            sg.popup('Closing YT Download in five seconds... \nClick OK to shutdown now.',title='YT Download', auto_close=True, auto_close_duration=5, icon=logo)
            window.close()
            

# Main setup loop. Calls GUI_checks()
downloader.terminal_msgs(1, 3)
window = sg.Window('YT Download', layout, icon=logo)
while True:
    
    # Playlist Layout
    playlist_layout = [
        [sg.Push(), sg.Text('You are trying to download a Playlist. Do you want to continue?'), sg.Push()],
        [sg.Push(), sg.Button('Yes'), sg.Button('No'), sg.Push()]
    ]

    # Settings Menu Layout
    settings_layout = [
        [sg.Push(), sg.Text('Settings Menu'), sg.Push()],
        [sg.Push(), sg.Text('~' * 15), sg.Push()],
        [sg.Text('Directory Settings'), sg.HorizontalSeparator(pad=(10, 5))],
        [sg.Checkbox('Use default directory', default=cfg.use_default_directory)],
        [sg.Text('Custom default directory:', tooltip='Custom default directory will not be used if USE DEFAULT DIRECTORY is checked')],
        [sg.Input(tooltip='Custom default directory will not be used if USE DEFAULT DIRECTORY is checked'), sg.FolderBrowse(tooltip='Custom default directory will not be used if USE DEFAULT DIRECTORY is checked')],
        [sg.Text('Popup Settings'), sg.HorizontalSeparator(pad=(10, 5))],
        [sg.Checkbox('Show playlist confirmation popup', default=cfg.playlist_confirmation)],
        [sg.Checkbox('Show file downloaded popup', default=cfg.file_downloaded)],
        [sg.Text('Miscellaneous Settings'), sg.HorizontalSeparator(pad=(10, 5))],
        [sg.Checkbox('Download as .mp3 by default', default=cfg.default_as_audio)],
        [sg.Text('Color Theme:'), sg.Combo(sg.theme_list(), default_value=cfg.color_theme)],
        [sg.Checkbox('Revert to default settings?', default=cfg.use_defaults, tooltip='If checked, YT Download will revert to default settings.')],
        [sg.Push(), sg.Text('~' * 15), sg.Push()],
        [sg.Button('Apply', tooltip='YT Download will shutdown in order to apply your changes'), sg.Push(), sg.Button('Exit', tooltip='Exiting will not save any changes')]

    ]

    event, values = window.read() # Check the active event and the value dictionary.
    print(event, values) # Print event and values for debugging in the command line.

    if event == sg.WIN_CLOSED or event == 'Exit': # Break the loop if the window is closed or the 'Cancel' button is pressed
        break
    
    if event == 'GITHUB': # If the linked is clicked, open the GitHub repo.
        web.open("https://github.com/Joey451-OG/YT-Dowload")

    if event == 'Download': # If the Download button was clicked, being file download
        GUI_checks(values['isAudio'], values['URL'], values['DIR'])
    
    if event == 'Settings': # If the Settings button is clicked, open the settings Menu
        settings_menu()

window.close() # Kill the program
