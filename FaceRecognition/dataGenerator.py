import numpy as np
import cv2
import os
from PIL import Image

prefixUrl='/home/khang/Downloads/'
face_cascade = cv2.CascadeClassifier('../haarcascade_frontalface_default.xml')

def dataGenerate(path,id):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    count=0

    for imgP in imagePaths:
       img = cv2.imread(imgP)
       gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
       faces = face_cascade.detectMultiScale(gray, 1.3, 5)

       for (x,y,w,h) in faces:
            count+=1
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.imwrite("Dataset/user."+str(id)+"."+str(count)+".jpg",gray[y:y+h,x:x+w])

       print(imgP+'Face {0}'.format(len(faces)))

dataGenerate(prefixUrl+'truonggiang',1)