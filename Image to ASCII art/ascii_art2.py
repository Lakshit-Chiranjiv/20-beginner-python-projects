import ascii_magic as am
import os

os.chdir('C:/Users/KIIT/Desktop/ALL CODE ND STUFFS/PROJECTS-REPOS/Python Folder/mini-python-projects/Image to ASCII art')

def ascii_art(image_path):
    output = am.from_image(image_path)
    output.to_terminal(columns = 100, char = '#')
    output.to_file('output2.txt')
    output.to_html_file('output2.html')

ascii_art('messi.jpg')