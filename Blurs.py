import cv2
import numpy as np

pic = cv2.imread('manushi.jpg')

#Gussian
matrix=(7,7)
blur= cv2.GaussianBlur(pic,matrix,0)
resize=cv2.resize(blur,(500,500))
rOrg=cv2.resize(pic,(500,500))
#Median Blur
kernal=3
median=cv2.medianBlur(pic,kernal)


cv2.imshow('median',median)
cv2.imshow('guass',blur)
cv2.imshow('org',pic)
cv2.waitKey(0)
cv2.destroyWindow()
