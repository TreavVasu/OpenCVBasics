import cv2
import numpy as np

pic = cv2.imread("manushi.jpg")
px = 7
color = 200
space = 100

filter = cv2.bilateralFilter(
    pic,
    px,
    color,
    space
)
cv2.imshow('org',pic)
cv2.imshow('filter',filter)
cv2.waitKey(0)
cv2.destroyWindow()