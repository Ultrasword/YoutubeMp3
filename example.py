"""
MIT License
Copyright (c) 2021 Ultrasword

___      ___  __________   ___      __________  ______
\  \    /  / |____  ____| |   \    /  |   __   \___   \
 \  \  /  /      | |      |    \  /   |  |__|  |   \   \
  \  \/  /       | |      | |\  \/  / |        /___/   /
    |  |         | |      | | \____/| |  _____/___    /
    |  |         | |      | |       | | |       __\   \
    |  |         | |      | |       | | |      /      /
    |__|         |_|      |_|       |_|_|      \_____/ 



Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import youtubemp3 as ymp3

# an example involving playlists!


# get the link to the playlist that the user wants to download
link = input("Please input a youtube playlist link! Make sure that the link is for an unlisted or public playlist!:\n\n>")

# get the name of the folder that the user wants the audio to be stored
folder_name = input("""\nWhat would you like for the name of the \n'Album' or 'Playlist' to be on your device?
Remember, this is not from root directory!
Thus, do not try to input something such as...
'C:\\User\\Documents\\folder\\music'\nMake sure to input the directory with double '\\\\':\n\n>""")

# REMEMBER #
# the folder name will be native to the directory that this file is being run!
# DO NOT GIVE A FILE DIRECTORY FROM ROOT, IT WILL CAUSE PROBLEMS!

# sdata is a variable used to store the playlist information!
# ymp3.ydl is the youtube_dl object that the module uses
# take advantage of this and use it for this purpose as well!
sdata = ymp3.get_playlist_from_link(ymp3.ydl, link)

# now a for loop
# this will loop through every youtube video in the sdata variable
# we can use the variable block to collect each video from the sdata, which is a list of videos
for block in sdata:
    # make a new variable
    # this variable, song, will store the information returned from the ymp3.download_song
    # the download song function will download the song, but also return some information for you to use if you wish 
    # to convert the audio type
    # the audio type will be mp3
    song = ymp3.download_song(block, folder_name, 'mp3')

    # this is what allows you to stop the files from being downloaded twice
    if song == None:
        continue