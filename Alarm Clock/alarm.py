from playsound import playsound
import time
import os

CLEAR = '\033[2J'
CLEAR_AND_RETURN = '\033[H'

os.chdir('C:/Users/KIIT/Desktop/ALL CODE ND STUFFS/PROJECTS-REPOS/Python Folder/mini-python-projects/Alarm Clock')

def alarm(duration_in_secs):
    time_elapsed = 0
    print(CLEAR, end='')
    while time_elapsed < duration_in_secs:
        time.sleep(1)
        time_elapsed += 1

        time_left = duration_in_secs - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f'{CLEAR_AND_RETURN}Alarm will go off in {minutes_left:02d}:{seconds_left:02d}')

    # block parameter is set to True so that the program doesn't continue until the sound is done playing
    playsound('alarm.mp3', block=True)
    
min_input = int(input('Enter the number of minutes to wait before the alarm goes off: '))
sec_input = int(input('Enter the number of seconds to wait before the alarm goes off: '))

duration_in_secs = min_input * 60 + sec_input
alarm(duration_in_secs)