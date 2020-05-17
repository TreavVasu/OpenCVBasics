import cv2
import numpy

pic = cv2.imread('manushi.jpg')

threshlod1=50
threshlod2=100
canny=cv2.Canny(pic,threshlod1,threshlod1)
cv2.imshow('Canny',canny)
cv2.waitKey(0)
cv2.destroyWindow()