
import cv2

vidcap = cv2.VideoCapture('rtsp://project:project1@10.10.133.225:554/live')
count = 0
success = True
fps =int(vidcap.get(cv2.CAP_PROP_FPS))

while success:
    s=10*fps
    success,image = vidcap.read()
    print('read a new frame:',success)
    if count%s == 0 :
         cv2.imwrite('D:/cam/testimages/frame%d.jpg'%count,image)
         print('successfully written 10th frame')
    count+=1