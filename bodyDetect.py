import cv2
import numpy as np

classifier = cv2.CascadeClassifier('./haarcascade_mcs_upperbody.xml') # an opencv classifier

frame = cv2.imread('/home/khang/Downloads/pedestrian-detection/images/person_095.bmp')
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
# def inside(r, q):
#     rx, ry, rw, rh = r
#     qx, qy, qw, qh = q
#     return rx > qx and ry > qy and rx + rw < qx + qw and ry + rh < qy + qh


# def draw_detections(img, rects, thickness = 1):
#     for x, y, w, h in rects:
#         # the HOG detector returns slightly larger rectangles than the real objects.
#         # so we slightly shrink the rectangles to get a nicer output.
#         pad_w, pad_h = int(0.15*w), int(0.05*h)
#         cv2.rectangle(img, (x+pad_w, y+pad_h), (x+w-pad_w, y+h-pad_h), (0, 255, 0), thickness)

# hog = cv2.HOGDescriptor()
# hog.setSVMDetector( cv2.HOGDescriptor_getDefaultPeopleDetector() )

# frame = cv2.imread('/home/khang/Downloads/test.jpg')    
# found,w=hog.detectMultiScale(frame, winStride=(8,8), padding=(32,32), scale=1.05)
# draw_detections(frame,found)
# cv2.imshow('feed',frame)
# cv2.waitKey(0)      
# cv2.destroyAllWindows()