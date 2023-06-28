<div align="center">
<h1>YT Download</h1>

A GUI based YouTube downloader made with [yt-dlp](https://www.github.com/yt-dlp/yt-dlp)

![winget](https://user-images.githubusercontent.com/60891047/227323272-91f61384-b3af-4710-bac1-5d8f976333bd.png)
</div>

## Table of Contents  
* [Change Log](#change-log)
    * [Version 1.4.0](#version-140)
    * [Version 1.3.0](#version-130)
    * [Version 1.2.1](#version-121)
    * [Version 1.2.0](#version-120)
    * [Version 1.0.1](#version-101)
    * [Version 1.0.0](#version-100)
* [Installation](#installation)  
    * [Windows](#windows)  
    * [Linux](#linux)
    * [Suggested Changes for Linux Users](#suggested-changes-for-linux-users)
* [Updating YT Download](#updating-yt-download)
    * [Windows](#windows-1)
    * [Linux](#linux-1)
* [User Manual](#user-manual)  
    * [Launching on Linux](#launching-on-linux)
    * [Downloading Playlists](#downloading-playlists)  
* [The Settings Menu](#the-settings-menu)
* [The Config File](#the-config-file)
    * [Directory Settings](#directory-settings)
    * [Popup Settings](#popup-settings)
    * [Miscellaneous Settings](#miscellaneous-settings)
    * [Making Changes](#making-changes)
* [Credits](#credits)

## Change Log
### **Version 1.4.0**
- ➕ Added [Settings Menu](#PLACEHOLDER)
- ➖ Removed config file from `.msi` installer*
- 🐛 Fixed inaccessible config file bug by rewriting the `config()` class  

*The config file is now handled by the reworked `config()` class in `main.py`. The new class handles updating, reading, and writing the config file.
### **Version 1.3.0**  
- ➕ Added the ability to change settings through the [config](#changing-settings) file.  
- ➕ Added Linux support and documentation.  
- ➕ Revamped the documentation  
- ➕ Added terminal messages that display program progress in the terminal.  
- 🐛 Simplified the code base in order to make the source more readable.  

### **Version 1.2.1**
- 🐛 Fixed critical bug in .msi installer that deleted all other `PATH` variables when installing.  
- ➕ Added detection system for YouTube Playlists.*  
- ➕ Added a version number link that links to this repo.  
- ➕ Added an error message when FFmpeg is not installed to the `PATH`  

*The Playlist detection system will warn the user if it finds a playlist url. It will then ask if the user wants to proceed with the download of the entire playlist.

[QUICK PATCH 3/19/2023] Added LICENSE to the installation process. No functionality was changed, thus no new version number. Note, there may be another patch to the .msi if `winget` wants a truly admin perms free installation.

### **Version 1.2.0**  
Changed the default file download path to `C:\Users\%userprofile%\Documents\YT Download` when the user does not specify a file location.  

Cleaned the up `YT Download.py` while True loop and sent most of the logic to `GUI_checks()`.

**CRITICAL BUG!!!!!** All previous .msi installers are removing **ALL OTHER `PATH` VARIABLES**. Please **DO NOT USE** old .msi installers (1.2.0 and below). Working on a patch ASAP.  

### **Version 1.0.1**  
In the previous version, the included .msi installer was not adding FFmpeg (a required dependency) to the windows PATH, causing the program to crash when downloading. This has been fixed. None of the underline source code has been changed. Once again, thank you for using YT Download.

**CRITICAL BUG**: SEE VERSION 1.2.0

### **Version 1.0.0**  
Welcome to YT Download! To start, simply install the program with the .msi installer. You can also download the source code.
NOTE: Removed the original .msi installer. Currently working on a new one. The old installer was not installing FFmpeg to the path. Once I fix that, I'll release a new installer. For now, please uninstall YT Download with the original .msi installer. You can still run YT Download from source if you meet all of the prerequisites. For a full list of prerequisites, check Credits.txt - Joey [3/5/2023]

## Installation    
### Windows
You can install YT Download with `winget` by typing `winget install yt-download` in a powershell window. Alternatively, you can download the latest installer from the [Release tab.](https://github.com/Joey451-OG/YT-Download/releases)
```
PS C:\> winget install yt-download
```  

### Linux  
Since YT Download does not yet have a linux binary, you'll need to clone this github repo, install the dependencies, and start up YT Download by running the python file with the same name. Here is a step-by-step guide on how to do just that.  

First, install git:
```
$ sudo apt install git
```  
Next, install pip.  
```
$ sudo apt install python3-pip
```
Make sure to navigate to the folder where you want YT Download to install to.  
Then, clone this repo:
```
$ git clone https://www.github.com/Joey451-OG/YT-Download
```
Now it's time to install the dependencies.  
First, install PySimpleGUI:
```
$ pip install PySimpleGUI
```
Next, install Tkinter:
```
$ sudo apt install python3-tk
```
Now, install yt-dlp:
```
$ pip install yt-dlp
```
yt-dlp may not install to the PATH. To fix this, open `~/.bashrc` as `sudo`
```
$ sudo nano ~/.bashrc
```

> If you don't have nano installed, you can install it with:  
>```
>$ sudo apt install nano
>```

Then add this line to the bottom of the file.
```bash
export PATH="/home/YOUR_USERNAME_HERE/.local/bin:$PATH"
```

To save the file press `Ctrl+X` then press `y` and `enter`  

Then, source the `~/.bashrc` file.
```
$ source ~/.bashrc
```
Finally, install FFmpeg:
```
$ sudo apt install ffmpeg
```

YT Download is now ready to use. To launch YT Download, use this command in the directory where this repo was cloned:
```
$ python3 'YT Download.py'
``` 

The rest of the documentation still applies to linux. In rare instances where there are differences, there will be ample explanation.  

### Suggested Changes for Linux Users

Even though YT Download is fully functional (given you have followed the tutorial above), users might wish to make some quality of life changes.

First would be to rename `YT Download.py` to `YT-Download.py` in order to not have to type quotation marks when launching the program. This can be done using a GUI, but to do it in the terminal first navigate to where YT Download is installed and then run this command.
```
$ mv 'YT Download.py' YT-Download.py
```

Finally, it is very inconvenient to have to navigate to where YT Download was installed in order to launch it. To fix this, we need to make some modifications.

First, open `main.py` with nano.
```
$ nano main.py
```
Navigate to the `config_path` variable, it's at the top of the script right underneath the license and imports. Change `config_file = 'config.yml` to `config_path = '/home/YOUR_USERNAME_HERE/bin/config.yml'`.

```python
[...]

config_file = '/home/YOUR_USERNAME_HERE/bin/config.yml'

video_options = {
  [...]
```

Save the file by pressing `Ctrl + X` then `y` then `enter`.  

Next, open `YT-Download.py` with nano
```
$ nano YT-Download.py
```
Add this line to the very top of the file.
```
#!/usr/bin/env python3
```
Save the file.  

Make the script executable by running this command.
```
$ chmod +x YT-Download.py
```
Now, make two directories in the home folder. ALso, make a `python` directory in the lib folder.
```
$ cd ~
$ mkdir bin lib
$ mkdir lib/python
```
Next, open the `~/.bashrc` file as sudo.
```
$ sudo nano ~/.bashrc
```

Navigate to the bottom of the file and add this line:
```bash
PYTHONPATH=$HOME/lib/python
EDITOR=nano

export PYTHONPATH EDITOR
```
You will need to sign-out/sign-in for these changes to take into effect.  

Now navigate back into the directory where YT-Download is installed and move the following files to the new `/bin` directory.
```
$ mv YT-Download.py ~/bin/
$ mv main.py ~/bin/
$ mv logo.png ~/bin/
```

You are now done. To run YT-Download simply type this command.
```
$ YT-Download.py
```

> **Note:** You can delete the cloned repo directory since it is no longer needed.

## Updating YT Download
### Windows
To update YT Download on windows run `winget update yt-download` in powershell or simply download and run the new `.msi` from [Releases Tab](https://github.com/Joey451-OG/YT-Download/releases).
```
PS C:\> winget update yt-download
```
### Linux
If you are not going to follow [suggested changes for linux users](#suggested-changes-for-linux-users), simply clone this repository and delete the old repo.
```
$ git clone https://www.github.com/Joey451-OG/YT-Download
```

If you have followed suggested changes for linux users, clone the repo then replace `YT Download.py` and `main.py` in `~/bin/` with the updated files. Now start following the [suggested changes for linux users](#suggested-changes-for-linux-users) instructions. Stop after you `chmod` the `YT-Download.py` script.
>Note:
>If you get the error: `KeyError: 'version'` when running the script, you'll need to replace the config file in `~/bin` with the new one in the repo (only 1.3.0 and earlier). 

## User Manual  
After installing the program with the .msi or `winget`, open YT Download.

<img width="600" alt="opening" src="https://user-images.githubusercontent.com/60891047/225435630-903ae087-debf-4dbf-919b-db6555c6c089.png">  

> ### Launching on Linux
> Navigate to the directory where YT Download is installed and run:
>```
>$ python3 'YT Download.py'
>```
>Or, if you have followed [Suggested Changes for Linux Users](#suggested-changes-for-linux-users) you can run this command from any directory
>```
>$ YT-Download.py
>```  

The program will open a terminal window and the GUI. Do not close the terminal, it is required for the program to run.

<img width="1280" alt="first open" src="https://user-images.githubusercontent.com/60891047/225436355-a131b435-9930-45b1-b675-aac36f67b2c3.png">

Now, simply copy the url of the YouTube video you want to download and paste it in the `YouTube URL` feild.

<img width="1280" alt="url" src="https://user-images.githubusercontent.com/60891047/225436615-f6fbccc0-b49d-41e8-b100-f7a1cfdc2df1.png">

Make sure to check the `Download as an audio file (mp3)?` checkbox if you want to download as an audio file. For example, this video is an official audio video, so I will be checking this box.

>          
> **NOTE: This program automatically downloads your videos/audio in the highest quality possible.**
> 

<img width="1280" alt="url" src="https://user-images.githubusercontent.com/60891047/225436855-26570c71-893c-4aed-b572-0587ccc295cf.png">

Now choose a file path for your file to be saved. You can leave this option blank and the program will automatically download to `Documents\YT Download` folder. The `Documents` folder is a defualt folder in the Windows OS.

<img width="1280" alt="custom location" src="https://user-images.githubusercontent.com/60891047/225437649-31a4a053-32d3-4dd2-8014-b0d733cdb909.png">

Next, just click `Download`. 

<img width="1280" alt="downloading" src="https://user-images.githubusercontent.com/60891047/225438384-54e39af8-de50-4af3-af46-d25bd1e3c7e6.png">

> 
> ### Downloading Playlists
> To download a playlist follow all of the above and bellow steps. Just make sure to click `Yes` on the popup. This popup is to warn the user that they are about to download a playlist. When downloading a playlist, YT Download will download all videos in the playlist to your chosen file path and as your chosen file type.
> 
> <img width="304" alt="Playlist Warning" src="https://user-images.githubusercontent.com/60891047/225441213-089e396e-b585-4721-8119-e13da2fe3902.png">
> 
  
Once your file is done downloading, a popup will appear showing the title of the youtube video you downloaded and where on your computer you saved it. (When downloading a playlist, this popup will only appear once the whole playlist is done downloading so please be patient.)

<img width="1280" alt="downloaded" src="https://user-images.githubusercontent.com/60891047/225439007-7dadec6c-623e-4445-8ac7-6bd664f8f972.png">

<img width="872" alt="file" src="https://user-images.githubusercontent.com/60891047/225439475-56294cf0-db5c-497d-bdc6-55af6150614b.png">  

## The Settings Menu
1.4.0 Introduced the Settings Menu which allows users to change YT Download's settings through a GUI. To open the settings menu, click the `Settings` button.  

By default, the settings menu should look like this:  
<img width="310" alt="settings_menu" src="https://github.com/Joey451-OG/YT-Download/assets/60891047/907eea0e-9539-48b6-bfaa-a508b4b50935">

> NOTE:
> - After clicking the `Apply` button, YT Download will automatically shutdown in order to apply user changes. You will need to restart the program manually.  
> - Clicking the `Exit` button will close the Settings Menu without restarting or saving any changes.

You can find a description of each setting starting [here](#directory-settings).

## The Config File  
1.3.0 Introduced the ability to change YT Download's settings by modifying the `config.yml` file. Here is a breakdown on what each option does.  

This is the default state of `config.yml`
```yaml
version: 1.4.0
Directory_Settings:
  use_default_directory: true
  custom_default_directory: paste\custom\default\directory\path\here
Popup_Settings:
  playlist_confirmation: true
  file_downloaded: true
Miscellaneous_Settings:
  default_as_audio: false
  color_theme: DarkAmber
```

The config file is broken up into three sub-sections: `Directory Settings`, `Popup Settings`, and `Miscellaneous Settings`. [Directory Settings](#directory-settings) controls how YT Download handles directories, [Popup Settings](#popup-settings) handles how YT Download uses popups, and [Miscellaneous Settings](#miscellaneous-settings) controls... well.. miscellaneous settings such as YT Download's color theme.

>Note: The `version` variable is used to display the version number on the main window and update the config file. Please do not change this variable.

### Directory Settings
As stated previously, `Directory Settings` controls how YT Download handles directories.  

`use_default_directory` | Input: *yes*, *no*  
If *yes* YT Download will use the default directory. For windows users the default directory is: `C:\users\%USERPROFILE%\Documents\YT Download` (or OneDrive equivalent). For linux users the default directory is: `~/Documents/YT-Download`. If *no*, then YT Download will use whatever directory is specified in `custom_default_directory` as the default directory.   
  
`custom_default_directory` | Input: *PATH str*  
Whatever directory path that is inputted here will be used as the default directory if 
`use_default_directory` is *no*.  

> Note: One common mistake when using this feature is not typing the directory in properly. The author strongly recommends pasting a directory path into this field. However, if one is unable to do such, remember to use backslashes ( `\` ) for windows and forward slashes ( `/` ) for linux. If the directory is inputted incorrectly, YT Download will make a new directory in the program's root directory.  
  
### Popup Settings
`Popup Settings` handles which popups YT Download shows.
> Note: `Popup Settings` cannot disable error popups

`playlist_confirmation` | Input: *yes*, *no*  
If *yes*, the [playlist confirmation popup](#downloading-playlists) will be shown. If *no*, the popup will not be shown. This will result in the playlist being downloaded without any extra user input.  

`file_downloaded` | Input: *yes*, *no*  
If *yes* the [file downloaded](https://user-images.githubusercontent.com/60891047/225439007-7dadec6c-623e-4445-8ac7-6bd664f8f972.png) popup will be shown. If *no*, the popup will not be shown.  

### Miscellaneous Settings
`Miscellaneous Settings` handles a mix of different settings.  

`default_as_audio` | Input: *yes*, *no*  
If *yes*, the `Download as audio file (mp3)?` box will already be selected when opening YT Download. If *no* the checkbox will not be selected by default.  

`color_theme` | Input: *str*  
Controls which PySimpleGUI color theme will be used. To change the color theme, simple pick a theme and copy its' name into the field. Make sure to mind the casing (e.g., *DarkAmber* is a valid theme but *darkamber* is not).  

![themes](https://user-images.githubusercontent.com/60891047/231323710-094b9efd-9f88-490d-b172-4e42cc56dd1b.png)

For an interactive version of this image follow the steps bellow.  

- Make sure Python is installed then run: `pip install PySimpleGUI` in a terminal window.  
- Start up Python by typing the command `python` (or `python3` for linux users).
- Paste the bellow code:  
```python
import PySimpleGUI

PySimpleGUI.theme_previewer()
```
### Making Changes
After you are finished editing the config file, simply save the file and restart YT Download for the changes to come into effect.

## Credits
Icon: Image by https://pixabay.com/images/id-1834016/

Dependencies:

YT-DLP: https://github.com/yt-dlp/yt-dlp

PySimpleGUI: https://github.com/PySimpleGUI/PySimpleGUI

FFmpeg: https://ffmpeg.org/

PyYAML: https://github.com/yaml/pyyaml  

YAML: https://yaml.org/  

Thank you for using YT Download!

