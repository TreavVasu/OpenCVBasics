import cv2
import numpy as np

pic=cv2.imread('python.jpg')
column=pic.shape[1]
rows=pic.shape[0]
M=np.float32(
    [
    [1,0,-18],
    [0,1,70]
    ]
    )
shifted=cv2.warpAffine(pic,M,(column,rows))
#Img Shifting

center=(column/2,rows/2)
angle=45
M=cv2.getRotationMatrix2D(center,angle,0.5)
rotate=cv2.warpAffine(pic,M,(column,rows))
#Image Rotation

threshold_value=100
[T_value,binary_threshold]=cv2.threshold(pic,threshold_value,255,
                                         cv2.THRESH_BINARY_INV)


cv2.imshow('shifted',binary_threshold)
cv2.waitKey(0)
cv2.destroyWindow()
