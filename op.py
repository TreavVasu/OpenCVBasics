import cv2
import numpy as np


img = cv2.imread('python.png',2)
cv2.imwrite('python.jpg',img)
cv2.imshow('Image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()


