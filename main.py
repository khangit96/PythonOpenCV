import numpy as np
import sys
import cv2
import urllib.request
import pyrebase

#Firebase
config = {
  "apiKey": "uTP6tlP930oA1s9zuwGIZvrz1ef8ZjVLegROgNN0",
  "authDomain": "smarthome-5d11a.firebaseapp.com",
  "databaseURL": "https://smarthome-5d11a.firebaseio.com",
  "storageBucket": "smarthome-5d11a.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def stream_handler(message):
      print('data changed')

my_stream = db.child("user").stream(stream_handler)

# Image Detect
url='http://192.168.1.13:8080/shot.jpg?rnd=51290'
count=0

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

while True:
    imgResp = urllib.request.urlopen(url)
    imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)   
    img = cv2.imdecode(imgNp,-1)

    # Detect Face
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        count+=1
        print('Face {0}'.format(len(faces)))
        cv2.imwrite('face_'+str(count)+'.png',img)
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.namedWindow('img',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('img', 600,600)
    cv2.imshow('img',img)
  
   #Exit loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
