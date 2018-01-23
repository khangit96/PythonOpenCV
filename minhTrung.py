import pyrebase
#import RPi.GPIO as GPIO
import time
import threading

#init Firebase
config = {
  "apiKey": "uTP6tlP930oA1s9zuwGIZvrz1ef8ZjVLegROgNN0",
  "authDomain": "smarthome-5d11a.firebaseapp.com",
  "databaseURL": "https://smarthome-5d11a.firebaseio.com",
  "storageBucket": "smarthome-5d11a.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

#init GPIO
# GPIO.setmode(GPIO.BCM)

# GPIO.setwarnings(False)

# GPIO.setup(13,GPIO.OUT)
# GPIO.setup(6,GPIO.OUT)
# GPIO.setup(5,GPIO.OUT)
# GPIO.setup(11,GPIO.OUT)

# GPIO.setup(9,GPIO.OUT)
# GPIO.setup(10,GPIO.OUT) #relay3
# GPIO.setup(22,GPIO.OUT) #relay2
# GPIO.setup(27,GPIO.OUT) #relay1

# GPIO.output(13,GPIO.LOW)
# GPIO.output(6,GPIO.LOW)
# GPIO.output(5,GPIO.LOW)
# GPIO.output(11,GPIO.LOW)
# GPIO.output(9,GPIO.LOW)
# GPIO.output(10,GPIO.LOW)
# GPIO.output(22,GPIO.LOW)
# GPIO.output(27,GPIO.LOW)

#Thread
checkRelay1=True
checkRelay2=True

def worker1():
    global checkRelay1
    while checkRelay1==True:
        print('worker1: '+str(checkRelay1))
        time.sleep(1)

def worker2():
    global checkRelay2
    while checkRelay2==True:
        print('worker2: '+str(checkRelay2))
        time.sleep(1)
#Relay1
def stream_relay1(message):
      if message['path']== '/TurnOn':
          if message['data']==True:
              #GPIO.output(27,GPIO.HIGH)
              f=open('/home/pi/Desktop/PythonOpenCV/log.txt','w')
              f.write('Relay1-TurnOn')
              f.close()
              print('Relay1-TurnOn-true')
          else:
             # GPIO.output(27,GPIO.LOW)
              f=open('/home/pi/Desktop/PythonOpenCV/log.txt','w')
              f.write('Relay1-TurnOff')
              f.close()
              print('Relay1-TurnOn-false')

      if message['path']== '/Blink':
          if message['data']==True:
             global checkRelay1
             checkRelay1=True
             t = threading.Thread(name='1',target=worker1)
             t.start()
             print('Relay1-Blink-true')
          else:
              global checkRelay1
              checkRelay1=False
              print('Relay1-Blink-false')
#Relay2
def stream_relay2(message):
    if message['path']== '/TurnOn':
          if message['data']==True:
              print('Relay2-TurnOn-true')
          else:
              print('Relay2-TurnOn-false')

    if message['path']== '/Blink':
         if message['data']==True:
             global checkRelay2
             checkRelay2=True
             t = threading.Thread(name='2',target=worker2)
             t.start()
             print('Relay2-Blink-true')
         else:
              global checkRelay2
              checkRelay2=False
              print('Relay2-Blink-false')
#Relay3
def stream_relay3(message):
     if message['path']== '/TurnOn':
          if message['data']==True:
              print('Relay3-TurnOn-true')
          else:
              print('Relay3-TurnOn-false')

     if message['path']== '/Blink':
         if message['data']==True:
              print('Relay3-Blink-true')
         else:
              print('Relay3-Blink-false')

relay1 = db.child("MinhTrung/Relay1").stream(stream_relay1)
relay2 = db.child("MinhTrung/Relay2").stream(stream_relay2)
relay3 = db.child("MinhTrung/Relay3").stream(stream_relay3)
