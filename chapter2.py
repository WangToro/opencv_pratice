import cv2
import numpy as np



img = cv2.imread("Resources/lena.png")
kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# turn into gray picture
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
# make picture into Blur EX:(3,3)or(7,7)or(9,9).....more Blur
imgCanny = cv2.Canny(img,150,200)
# detect edge
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
# make line more thicker
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)
# make line more thinner

cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialation Image",imgDialation)
cv2.imshow("Eroded Image",imgEroded)
cv2.waitKey(0)