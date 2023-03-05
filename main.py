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
        'preferredcodec': 'mp3',
    }]
}

# Handels downlaoding and retriving information
def YoutubeDownloader(settings, url, isDownload=False):

    if isDownload: # Downloads the audio or video file
        with YoutubeDL(settings) as ydl:
            ydl.download(url)
    else:
        with YoutubeDL() as ydl: # Returns the title of video the url points to. 
            try:
                info = ydl.extract_info(url, download=False)
                return info['title']
            except utils.DownloadError:
                return 'ERROR'
            
            

# Main logic. Sets directory when specified and calls YoutubeDownloader()
def logic(URL, ISaudio, DIR='skip'):
    
    dir = DIR

    if dir == 'skip': # No directory was specified.
        pass
    else: # Format both the video and audio options with the specified directory. 
        audio_options['outtmpl'] = dir + '/%(title)s.%(ext)s'
        video_options['outtmpl'] = dir + '/%(title)s.%(ext)s'
    
    if ISaudio: # Download as audio or video
        YoutubeDownloader(audio_options, URL, True)
    else:
        YoutubeDownloader(video_options, URL, True)
    
def return_title(url): # Returns the title of video the url points to.
    return YoutubeDownloader(None, url)


'''
Usefull testing things:

https://youtu.be/I8sUC-dsW8A
'''