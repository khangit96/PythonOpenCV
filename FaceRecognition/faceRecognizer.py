import cv2
import cv2.face
import numpy as np
import sys

from picamera.array import PiRGBArray
from picamera import PiCamera
import time

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainner.yml')
faceCascade = cv2.CascadeClassifier("../haarcascade_frontalface_default.xml");

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
     
    img = frame.array
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)
        
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(225,0,0),2)
        Id, con = recognizer.predict(gray[y:y+h,x:x+w])
        if Id==1:
            Id="Ruby"
        elif Id==2:
            Id="Keen"
        elif Id==3:
            Id='Truong Giang'
        elif Id==4:
            Id='Me'
        elif Id==5:
            Id='Ba'
        else:
            Id="Unknown"
            
        print(Id)
        
        cv2.putText(img, str(Id), (100,100),cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)
        
        
    cv2.imshow("Frame", img)
    cv2.waitKey(100)
 
    rawCapture.truncate(0)
    
    #if key == ord("q"):
	   # break






