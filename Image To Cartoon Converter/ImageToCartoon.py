import cv2
import os

#remove spaces from file path
os.chdir('C:/Users/KIIT/Desktop/ALL CODE ND STUFFS/PROJECTS-REPOS/Python Folder/20-beginner-python-projects/Image To Cartoon Converter')

img = cv2.imread('tommy.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray,5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)

cv2.imwrite('tommyCartoon.jpg',cartoon)

# cv2.imshow("Image", img)
# cv2.imshow("edges", edges)
# cv2.imshow("Cartoon", cartoon)
# cv2.waitKey(0)
# cv2.destroyAllWindows()