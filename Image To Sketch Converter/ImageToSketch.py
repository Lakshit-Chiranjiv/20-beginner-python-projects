import cv2
import os
#remove spaces from file path
os.chdir('C:/Users/KIIT/Desktop/ALL CODE ND STUFFS/PROJECTS-REPOS/Python Folder/20-beginner-python-projects/Image To Sketch Converter')
# print(dir)
image = cv2.imread('tommy.jpg')

grey_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_img)
blur = cv2.GaussianBlur(invert,(21,21),0)
inverted_blur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_img,inverted_blur,scale=256.0)

cv2.imwrite('tommysketch.png',sketch)