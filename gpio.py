import RPi.GPIO as GPIO

import time 

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(13,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(9,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

print ('led on')

GPIO.output(13,GPIO.HIGH)
GPIO.output(6,GPIO.HIGH)
GPIO.output(5,GPIO.HIGH)
GPIO.output(11,GPIO.HIGH)
GPIO.output(9,GPIO.HIGH)
GPIO.output(10,GPIO.HIGH)
GPIO.output(22,GPIO.HIGH)
GPIO.output(27,GPIO.HIGH)

time.sleep(3)

GPIO.output(13,GPIO.LOW)
GPIO.output(6,GPIO.LOW)
GPIO.output(5,GPIO.LOW)
GPIO.output(11,GPIO.LOW)
GPIO.output(9,GPIO.LOW)
GPIO.output(10,GPIO.LOW)
GPIO.output(22,GPIO.LOW)
GPIO.output(27,GPIO.LOW)



print ('led off')


