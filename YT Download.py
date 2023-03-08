import PySimpleGUI as sg
import main as downloader
import os

sg.theme('DarkAmber') # Color Scheme

user_dir = os.environ['USERPROFILE'] + '\Documents\YT Download'

# GUI layout
layout = [ [sg.Text("Thank you for using YT Download!")],
           [sg.Text("YouTube URL:"), sg.InputText(key='URL')],
           [sg.Checkbox('Download as an audio file (mp3)?', default=False, key='isAudio')],
           [sg.Text('File path. Leave blank to save download to:')],
           [sg.Text(f'{user_dir}')],
           [sg.Input(key='DIR'), sg.FolderBrowse()],
           [sg.Button('Download'), sg.Cancel()]

]

# Main logic function. Calls the appropriate functions in main.py and handles input errors.
def GUI_checks(event, audio_val, url_val, dir_val):
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
            downloader.logic(url_val, audio_val, dir_val)
            sg.popup(f'Downloaded {title} as a {file_type} file to {dir_val}', icon='logo.ico', title='YT Download')

            

# Main setup loop. Calls GUI_checks()
window = sg.Window('YT Download', layout, icon='logo.ico')
while True:
    
    event, values = window.read() # Check the active event and the value dictionary.
    print(event, values) # Print event and values for debuging in the command line.

    if event == sg.WIN_CLOSED or event == 'Cancel': # Break the loop if the window is closed or the 'Cancel' button is pressed
        break

    GUI_checks(event, values['isAudio'], values['URL'], values['DIR'])

window.close() # Kill the program