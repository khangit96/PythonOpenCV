import cv2
import numpy as np

classifier = cv2.CascadeClassifier("facial_recognition_model.xml") # an opencv classifier

frame = cv2.imread('truonggiang.jpg')
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

objects = classifier.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
for (x, y, w, h) in objects:
  cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

print('size '+str(len(objects)))

cv2.namedWindow('img',cv2.WINDOW_NORMAL)
cv2.resizeWindow('img', 600,600)
cv2.imshow('img',frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
# if len(objects) > 0:
#    found_objects = True

#         # Draw a rectangle around the objects
#   for (x, y, w, h) in objects:
#   cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

#   ret, jpeg = cv2.imencode('.jpg', frame)