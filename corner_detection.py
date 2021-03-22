
import numpy as np
import cv2

img = cv2.imread('2.png')
img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)     #resized image to fit into the screen
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)        #changed cocor to gray scale

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)   #Shi-Tomasi Corner Detector & Good Features to Track method used here
                                                         #(gray, 100, .01, 10) = (source image, no. of corners, accuracy(0-1), min eucleadian distance btw corners)
corners = np.int0(corners)                                

for corner in corners:
	x, y = corner.ravel()                            #[[x,y]].ravel=x,y
	cv2.circle(img, (x, y), 5, (255, 0, 0), -1)      #(img, (x, y), 5, (255, 0, 0), -1) = (source image, point to draw circle, radius, BGR, fill the circle)

cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
