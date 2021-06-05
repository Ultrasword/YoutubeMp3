# youtubedl for downloading the audio in webm form
from youtube_dl import YoutubeDL
import youtube_dl

# os for folder creation and traversing directories
import os

# subprocess to access ffmpeg
import subprocess as s_process

# requests to check if a link works
from requests import get as r_get

illegal_chars = list(r'\/:*?"<>|')

youtube_dl.utils.bug_reports_message = lambda: ''

ydl_setting = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': False,
    'default_search': 'auto'
}

ydl = YoutubeDL(ydl_setting)

def remove_non_char(string):
    n = "".encode('utf-8')
    for char in string:
        if char in illegal_chars:
            n+=" ".encode('utf-8')
        else:
            n+=char.encode('utf-8')
    return " ".join(x.decode() for x in n.split()).encode('utf-8').decode('utf-8')

def r_exists(link):
    try:
        r = r_get(link)
        if r.status_code != 200:
            print("The link was not valid or your device was unable to connect!")
            return False
    except:
        print("\nThe link does not exists or does not work!")
        return False
    return True

def get_from_link(ydl, link):
    # check if the link exists
    if not r_exists(link):
        return None
    # get the extracted info from the youtube link with ydl
    try:
        return ydl.extract_info(link, download=False)['entries'][0]
    except:
        return ydl.extract_info(link, download=False)
    else:
        return None

def get_playlist_from_link(ydl, link):
    # check if link exists!
    if not r_exists(link):
        return None
    # get the extracted playlist information from link
    # returns a list of the videos in the playlist
    return ydl.extract_info(link, download=False)['entries']

def download_song(data: dict, path: str, audio_format: str):
    global ydl_setting
    try:
        # make a dict for video data
        video_data = {
            # video url
            'url': data['url'],
            # get song name without illegal filename chars
            'title': remove_non_char(data['title']),
            # get file extension
            'ext': data['ext'],
            # get author - in some cases channel name
            'author': data['uploader'],
            # description of video
            'description': data['description'],
            # first thumbnail info from thumbnail list
            'thumbnail': data['thumbnails'][0],
            # audio codec information for ffmpeg
            'acodec': data['acodec'],
            # name of playlist
            'playlist_name': data['playlist']
        }
        # video path is needed if you want to use ffmpeg to convert audio format
        video_data['filepath'] = os.path.join(os.getcwd(), path, video_data['title'] + "." + video_data['ext'])

        # now try downloading the song
        # notify user that you are downloading the song!
        print("Downloading:\t{}".format(video_data['title']))
        # make a copy of ydl settings
        copy = ydl_setting.copy()
        # change name of download, audio_format, codec, and other things
        copy['outtmpl'] = "{}\\{}.{}".format(path, video_data['title'], video_data['ext'])
        # download the video file as a webm or whatever extension was provided
        with YoutubeDL(copy) as ydl:
            ydl.extract_info(video_data['url'], download=True)
        return video_data
    except:
        print("An error occurred during the process!")
        return None

def convert_with_ffmpeg(desired_format, song_data, **kwargs):
    ffmpeg='ffmpeg'
    delete_after = False
    if 'ffmpeg' in kwargs:
        ffmpeg = kwargs['ffmpeg']
    if 'delete_after' in kwargs:
        delete_after = kwargs['delete_after']
    # get new filename with desired audio_format
    filename = ".".join(song_data['filepath'].split(".")[0:-1]) + "." +  desired_format
    # create string for ffmpeg to use
    ffmpeg_string = '{} -i "{}" -acodec "{}" -vn "{}"'.format(ffmpeg, song_data['filepath'], desired_format,
                                                filename)
    s_process.run(ffmpeg_string)
    # delete the previous file if delete_after has been verified
    if delete_after:
        if os.path.exists(song_data['filepath']):
            os.remove(song_data['filepath'])
            print("[post-processing] Successfully Removed: {}".format(song_data['filepath']))
