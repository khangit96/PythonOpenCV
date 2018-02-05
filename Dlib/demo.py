import face_recognition
from PIL import Image
import cv2

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

# detectFace("/home/khang/Downloads/nh.jpg")