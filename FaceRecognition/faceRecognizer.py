import cv2
import numpy as np

recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer.load('trainner.yml')
faceCascade = cv2.CascadeClassifier("../haarcascade_frontalface_default.xml");

cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

img = cv2.imread('/home/khang/Downloads/test/17.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=faceCascade.detectMultiScale(gray, 1.2,5)

for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(225,0,0),2)
        Id = recognizer.predict(gray[y:y+h,x:x+w])
        if Id==1:
            Id="Truong giang"
        elif Id==2:
            Id="Tran thanh"
        elif Id==3:
            Id='Hoai Linh'    
        else:
            Id="Unknown"
        print(Id)

        #cv2.putText(img, str(Id), (x,y-40), font, 2, (255,255,255), 3)

print('Face {0}'.format(len(faces)))
cv2.namedWindow('img',cv2.WINDOW_NORMAL)
cv2.resizeWindow('img', 400,400)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


