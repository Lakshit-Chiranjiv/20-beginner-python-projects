import moviepy.editor as mp
from tkinter.filedialog import *

def convertToAudio(vid):
    video = mp.VideoFileClip(vid)
    audio = video.audio
    audio.write_audiofile("audio.mp3")

def selectVideo():
    vid = askopenfilename()
    convertToAudio(vid)

selectVideo()