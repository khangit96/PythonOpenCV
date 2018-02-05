import face_recognition
from PIL import Image
import cv2
import numpy as np
import sys
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

picture_of_me = face_recognition.load_image_file("/home/khang/Downloads/know.jpg")
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

#my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!

unknown_picture = face_recognition.load_image_file("/home/khang/Downloads/unknow.jpg")
unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

# Now we can see the two face encodings are of the same person with `compare_faces`!

results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

if results[0] == True:
    print("It's a picture of me!")
else:
    print("It's not a picture of me!")

# Load the jpg file into a numpy array

# def detectFace(imgPath):
#     image = face_recognition.load_image_file(imgPath)
#     face_locations = face_recognition.face_locations(image)

#     print("I found {} face(s) in this photograph.".format(len(face_locations)))

#     for face_location in face_locations:

#         # Print the location of each face in this image
#         top, right, bottom, left = face_location
#         print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

#         # You can access the actual face itself like this:
#         face_image = image[top:bottom, left:right]
#         pil_image = Image.fromarray(face_image)
#         pil_image.show()

<<<<<<< HEAD
# detectFace("/home/khang/Downloads/nh.jpg")
=======
#detectFace("/home/pi/Downloads/truonggiang.png")


face_cascade = cv2.CascadeClassifier('../haarcascade_frontalface_default.xml')

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
 
time.sleep(0.1)
 
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	
    img = frame.array
   # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   # faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
  #  for (x,y,w,h) in faces:
      #  print('Detect face')
       # img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_small_frame)

    print("I found {} face(s) in this photograph.".format(len(face_locations)))

    for face_location in face_locations:

        top, right, bottom, left = face_location
        print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

        # You can access the actual face itself like this:
        #face_image = image[top:bottom, left:right]
       # pil_image = Image.fromarray(face_image)
        #pil_image.show()

        
    cv2.imshow("Frame", img)
    key = cv2.waitKey(1) & 0xFF
 
    rawCapture.truncate(0)
 
    if key == ord("q"):
	    break
>>>>>>> ec80fb27ad8a5996673d66de4cee115cb4500026
