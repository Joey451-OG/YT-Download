import PySimpleGUI as sg
import main as downloader
import webbrowser as web
import os

sg.theme('DarkAmber') # Color Scheme

user_dir = os.environ['USERPROFILE'] + '\Documents\YT Download'

font = (None, 10, 'underline')

# GUI layout
layout = [ [sg.Text("Thank you for using YT Download!")],
           [sg.Text("YouTube URL:"), sg.InputText(key='URL')],
           [sg.Checkbox('Download as an audio file (mp3)?', default=False, key='isAudio')],
           [sg.Text('File path. Leave blank to save download to:')],
           [sg.Text(f'{user_dir}')],
           [sg.Input(key='DIR'), sg.FolderBrowse()],
           [sg.Button('Download'), sg.Cancel(), sg.Text('Version: 1.2.1', tooltip='https://github.com/Joey451-OG/YT-Dowload', enable_events=True, key='GITHUB', font=font)]
    ]

# Main logic function. Calls the appropriate functions in main.py and handles input errors.
def GUI_checks(event, audio_val, url_val, dir_val):
    download = True
    
    if 'playlist?list=' in url_val:
        # URL is a playlist
        playlist_window = sg.Window('YT Download', playlist_layout, icon='logo.ico')
        
        while True:
            p_event, p_val = playlist_window.read()
            print(p_event, p_val)
            if p_event == 'Yes':
                playlist_window.close()
                break
                
            elif p_event == 'No' or p_event == sg.WIN_CLOSED:
                sg.popup('Not downloading playlist...', icon='logo.ico', title='YT Download')
                playlist_window.close()
                download = False
                break

    if download:
        # URL is not a playlist

        title = 'playlist'

        if 'playlist?list=' not in url_val:
            title = downloader.return_title(url_val)
        
        if dir_val == '':
            dir_val = user_dir
        
        if audio_val:
            file_type = '.mp3'
        else:
            file_type = '.mp4'

        if event == 'Download':
            if url_val == '':
                sg.popup('Please make sure to provide a URL', icon='logo.ico', title='YT Download')
            else:
                if title == 'ERROR':
                    sg.popup('INVALID YOUTUBE URL', icon='logo.ico', title='YT Download')
                    title = False

            if title != False and url_val != '':
                yt_download = downloader.logic(url_val, audio_val, dir_val)

                if yt_download == 'FFMPEG ERROR':
                    sg.popup('It looks like FFmpeg is not installed. Try reinstalling YT Download or add FFmpeg to the PATH manually.', icon='logo.ico', title='YT Download')
                else:
                    sg.popup(f'Downloaded {title} as a {file_type} file to {dir_val}', icon='logo.ico', title='YT Download')
            

# Main setup loop. Calls GUI_checks()
window = sg.Window('YT Download', layout, icon='logo.ico')
while True:
    
    playlist_layout = [
        [sg.Text('You are trying to download a Playlist. Do you want to continue?')],
        [sg.Button('Yes'), sg.Button('No')]
    ]

    event, values = window.read() # Check the active event and the value dictionary.
    print(event, values) # Print event and values for debuging in the command line.

    if event == sg.WIN_CLOSED or event == 'Cancel': # Break the loop if the window is closed or the 'Cancel' button is pressed
        break
    
    if event == 'GITHUB':
        web.open("https://github.com/Joey451-OG/YT-Dowload")

    if event == 'Download':
        GUI_checks(event, values['isAudio'], values['URL'], values['DIR'])

window.close() # Kill the program