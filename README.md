<div align="center">
<h1>YT Download</h1>

A GUI based YouTube downloader made with [yt-dlp](https://www.github.com/yt-dlp/yt-dlp)

![winget](https://user-images.githubusercontent.com/60891047/227323272-91f61384-b3af-4710-bac1-5d8f976333bd.png)
</div>

## Table of Contents  
* [Change Log](#change-log)
* [Installation](#installation)  
    * [Windows](#windows)  
    * [Linux](#linux)
* [User Manual](#user-manual)  
    * [Launching on Linux](#launching-on-linux)
    * [Downloading Playlists](#downloading-playlists)
* [Changing Settings](#changing-settings)
    * [Directory Settings](#directory-settings)
    * [Popup Settings](#popup-settings)
    * [Miscellaneous Settings](#miscellaneous-settings)
* [Credits](#credits)

## Change Log
STILL IN DEV

## Installation    
### Windows
You can install YT Download with `winget` by typing `winget install yt-download` in a powershell window. Alternatively, you can download the latest installer from the [Release tab.](https://github.com/Joey451-OG/YT-Download/releases)  

### Linux  
STILL IN DEV  

## User Manual  
After installing the program with the .msi or `winget`, open YT Download.

<img width="600" alt="opening" src="https://user-images.githubusercontent.com/60891047/225435630-903ae087-debf-4dbf-919b-db6555c6c089.png">  

> ### Launching on Linux
> STILL IN DEV

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

## Changing Settings  
1.3.0 Introduced the ability to change YT Download's settings by modifying the `config.yml` file. Here is a breakdown on what each option does.  

This is the default state of `config.yml`
```yaml
# Directory Settings
use_default_directory: yes
custom_default_directory: paste\custom\default\directory\path\here

# Popup Settings
playlist_confirmation: yes
file_downloaded: yes

# Miscellaneous Settings
default_as_audio: no
color_theme: DarkAmber # For a full list of available themes, see 'themes.png' in YT Download's install location
```

The config file is broken up into three sub-sections: `Directory Settings`, `Popup Settings`, and `Miscellaneous Settings`. [Directory Settings](#directory-settings) controls how YT Download handles directories, [Popup Settings](#popup-settings) handles how YT Download uses popups, and [Miscellaneous Settings](#miscellaneous-settings) controls... well.. miscellaneous settings such as YT Download's color theme.  

### Directory Settings
As stated previously, `Directory Settings` controls how YT Download handles directories.  
  
<u>`use_default_directory` | Input: *yes*, *no*</u>  
If *yes* YT Download will use the default directory. For windows users the default directory is: `C:\users\%USERPROFILE%\Documents\YT Download`. For linux users the default directory is: `~/Documents/YT-Download`. If *no*, then YT Download will use whatever directory is specified in `custom_default_directory` as the default directory.   

<u>`custom_default_directory` | Input: *PATH str*</u>  
Whatever directory path that is inputted here will be used as the default directory if 
`use_default_directory` is *no*.  

> Note: One common mistake when using this feature is not typing the directory in properly. The author strongly recommends pasting the directory path into this field. However, if one is unable to do such, remember to use backslashes ( `\` ) for windows and forward slashes ( `/` ) for linux. If the directory is inputted incorrectly, YT Download will make a new directory in the program's root directory.  

### Popup Settings
`Popup Settings` handles which popups YT Download shows.
> Note: `Popup Settings` cannot disable error popups

<u>`playlist_confirmation`</u> | Input: *yes*, *no*  
If *yes*, the [playlist confirmation popup](#downloading-playlists) will be shown. If *no*, the popup will not be shown. This will result in the playlist being downloaded without any extra user input.  

<u>`file_downloaded`</u> | Input: *yes*, *no*  
If *yes* the [file downloaded](https://user-images.githubusercontent.com/60891047/225439007-7dadec6c-623e-4445-8ac7-6bd664f8f972.png) popup will be shown. If *no*, the popup will not be shown.  

### Miscellaneous Settings
`Miscellaneous Settings` handles a mix of different settings.  

<u>`default_as_audio`</u> | Input: *yes*, *no*  
If *yes*, the `Download as audio file (mp3)?` box will already be selected when opening YT Download. If *no* the checkbox will not be selected by default.  

<u>`color_theme`</u> | Input: *str*  
`color_theme` controls which PySimpleGUI color theme will be used. 

## Credits
Icon: Image by https://pixabay.com/images/id-1834016/

Dependencies:

YT-DLP: https://github.com/yt-dlp/yt-dlp

PySimpleGUI: https://github.com/PySimpleGUI/PySimpleGUI

FFmpeg: https://ffmpeg.org/

Thank you for using YT Download!

