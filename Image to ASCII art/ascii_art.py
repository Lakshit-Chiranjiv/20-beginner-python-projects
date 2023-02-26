import pywhatkit as pwk
import os

os.chdir('C:/Users/KIIT/Desktop/ALL CODE ND STUFFS/PROJECTS-REPOS/Python Folder/mini-python-projects/Image to ASCII art')

def ascii_art(image_path, output_path):
    pwk.image_to_ascii_art(image_path, output_path)

ascii_art('messi.jpg', 'output.txt')