import cv2
import numpy as np

pic = np.zeros((500,500,3),dtype ='uint8')
cv2.rectangle(
    pic,        #source
    (0,0),     #begin Side
    (500,200),  #End side
    (10,10,98), #color
            7, #Thickness
    lineType=8,
    shift=0
)
cv2.line(pic,
         (0,0),
         (500,200),
         (100,225,16),
         5,
         lineType=5,
         shift=0
         )

cv2.circle(pic,
           (250,150),
           50,
           (255,0,255),
           10)

font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(pic,
            "Hi Up Folks",
            (50,100),
            fontFace=font,
            fontScale=2,
            color=(255,32,250),
            thickness=5,
            lineType=cv2.LINE_8
            )


cv2.imshow('dark',pic)


cv2.waitKey(0)
cv2.destroyAllWindows()
