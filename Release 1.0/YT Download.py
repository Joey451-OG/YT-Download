import PySimpleGUI as sg
import main as dowloader

sg.theme('DarkAmber') # Color Scheme

# GUI layout
layout = [ [sg.Text("Thank you for using YT Download!")],
           [sg.Text("YouTube URL:"), sg.InputText(key='URL')],
           [sg.Checkbox('Download as an audio file (mp3)?', default=False, key='isAudio')],
           [sg.Text('File path. Leave blank to save download to program location.')],
           [sg.Input(key='DIR'), sg.FolderBrowse()],
           [sg.Button('Download'), sg.Cancel()]

]

# Returns 'program directory' if dir is empy, otherwise returns dir
def format_dir(dir):
    if dir == '':
        return 'program directory.'
    else:
        return dir
    
def incorrect_url_check(title):
    if title == 'ERROR':
        sg.popup('INVALID YOUTUBE URL', icon='logo.ico', title='YT Download')
        return False
    else:
        return title

# Main logic loop. Calls the apropriate functions in main.py
window = sg.Window('YT Download', layout, icon='logo.ico')
while True:
    
    event, values = window.read() # Check the active event and the value dictionary.
    print(event, values) # Print event and values for debuging in the command line.


    if event == sg.WIN_CLOSED or event == 'Cancel': # Break the loop if the window is closed or the 'Cancel' button is pressed
        break

    if event == 'Download' and values['isAudio'] and values['URL'] != "": # When the 'Download' button is pressed, check to see if the 'isAudio' check box is checked and see if the url feild is not blank.
        dir = format_dir(values['DIR'])                                   # Then, call format_dir() and fetch the video title. Finially, download the audio and display the popup when done.
        title = incorrect_url_check(dowloader.return_title(values['URL']))
        if title != False:
            dowloader.logic(values['URL'], True, dir)
            sg.popup(f'Downloaded {title} as a .mp3 file to {dir}', icon='logo.ico', title='YT Download')
    elif event == 'Download' and not values['isAudio'] and values['URL'] != "": # When the 'Download' button is pressed, check to see if the 'isAudio' check box is not checked and see if the url feild is not blank.
        dir = format_dir(values['DIR'])                                         # Then, call format_dir() and fetch the video title. Finially, download the video and display the popup when done.
        title = incorrect_url_check(dowloader.return_title(values['URL']))
        if title != False:
            dowloader.logic(values['URL'], False, dir)
            sg.popup(f'Downloaded {title} as a .mp4 file to {dir}', icon='logo.ico', title='YT Download')
    elif event == 'Download' and values['URL'] == '':
        sg.popup('Please make sure to provide a URL', icon='logo.ico', title='YT Download')

window.close() # Kill the program