import cv2
import numpy

cap = cv2.VideoCapture('video.avi')
while(cap.isOpened()):
    ret,frame = cap.read()
    cv2.imshow('video',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
