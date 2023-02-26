from ascii_magic import AsciiArt
import os

os.chdir('C:/Users/KIIT/Desktop/ALL CODE ND STUFFS/PROJECTS-REPOS/Python Folder/mini-python-projects/ASCII image generator')

my_art = AsciiArt.from_craiyon('Dhoni and Messi standing')
my_art.to_html_file('msd_ms.html', columns=200)