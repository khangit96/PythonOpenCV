import numpy as np
import sys
import cv2
import urllib.request

url='http://192.168.43.1:8080/shot.jpg?rnd=51290'

count=0
while True:
    # Use urllib to get the image from the IP camera
    print('ok')
    count+=1

    imgResp = urllib.request.urlopen(url)
    
    # Numpy to convert into a array
    imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
    
    # Finally decode the array to OpenCV usable format ;) 
    img = cv2.imdecode(imgNp,-1)
	
    # imgName='demo'+'.png'
	# put the image on screen
    cv2.imwrite('demo'+str(count)+'.png',img)
    cv2.imshow('IPWebcam',img)
  

    #To give the processor some less stress
    #time.sleep(0.1) 

    # Quit if q is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
