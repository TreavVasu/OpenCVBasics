import cv2
import numpy

cap=cv2.VideoCapture('video.mp4')
codec=cv2.VideoWriter_fourcc(*'XVID')
fps=30
i=1;
frameszie=(720,480)
out = cv2.VideoWriter('output.avi',codec,fps,frameszie)
while(cap.isOpened()):
    ret,frame=cap.read()
    cv2.imshow('frame',frame)
    i+=1
    print("Frame",i)
    if cv2.waitKey(0) & 0xFF==ord('q'):
        break
out.release()
cap.release()
cv2.destroyAllWindows()