
import cv2
import time
cv2.namedWindow("preview")
vc = cv2.VideoCapture('rtsp://project:project1@10.10.133.225:554/live')
i=0

if vc.isOpened(): 
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    if rval == False:
        break
    
    #time.sleep(5);
 
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
cv2.destroyWindow("preview") 