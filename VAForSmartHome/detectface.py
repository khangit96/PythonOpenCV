import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('../haarcascade_frontalface_default.xml')

img = cv2.imread('/home/pi/Downloads/truonggiang.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

print('Face {0}'.format(len(faces)))
cv2.namedWindow('img',cv2.WINDOW_NORMAL)
cv2.resizeWindow('img', 600,600)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

