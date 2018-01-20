import numpy as np
import wget
import sys
import cv2
import urllib.request
import pyrebase
import os
from gtts import gTTS
from mail import sendEmail
import requests
import json

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
      text=message['data']
      API_ENDPOINT = "http://api.openfpt.vn/text2speech/v4"

      headers={
            'api_key':'44c319aae94d40229d7cc09f1ce759f1',
            'speed':'0',
            'voice': 'hatieumai',
            'prosody':'1',
            'Cache-Control':'no-cache'
        }
      data = text.encode(encoding='utf-8')
      r = requests.post(url = API_ENDPOINT,data=data,headers=headers)

      url =r.json()['async']
      filename = wget.download(url)
      fileMp3='mpg321 '+filename
      os.system('mv '+filename+' voice.mp3')
      os.system("mpg321 voice.mp3")
      print(text)

my_stream = db.child("chat").stream(stream_handler)

#Image Detect
# url='http://192.168.43.1:8080/shot.jpg?rnd=51290'

# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# while True:
#     imgResp = urllib.request.urlopen(url)
#     imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)   
#     img = cv2.imdecode(imgNp,-1)

#     # Detect Face
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)

#     for (x,y,w,h) in faces:
#         print('Face {0}'.format(len(faces)))
#         os.system("mpg321 nhacotrom.mp3")
#         img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#         cv2.imwrite('face_detected.jpg',img)
#         sendEmail('face_detected.jpg')
#         roi_gray = gray[y:y+h, x:x+w]
#         roi_color = img[y:y+h, x:x+w]
#         eyes = eye_cascade.detectMultiScale(roi_gray)
#         for (ex,ey,ew,eh) in eyes:
#             cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

#     cv2.namedWindow('img',cv2.WINDOW_NORMAL)
#     cv2.resizeWindow('img', 600,600)
#     cv2.imshow('img',img)
  
#    #Exit loop
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

