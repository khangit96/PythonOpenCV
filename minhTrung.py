import pyrebase
import RPi.GPIO as GPIO
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
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(13,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(9,GPIO.OUT)
GPIO.setup(10,GPIO.OUT) #relay3
GPIO.setup(22,GPIO.OUT) #relay2
GPIO.setup(27,GPIO.OUT) #relay1

GPIO.output(13,GPIO.LOW)
GPIO.output(6,GPIO.LOW)
GPIO.output(5,GPIO.LOW)
GPIO.output(11,GPIO.LOW)
GPIO.output(9,GPIO.LOW)
GPIO.output(10,GPIO.LOW)
GPIO.output(22,GPIO.LOW)
GPIO.output(27,GPIO.LOW)

#Thread
count1=0
count2=0

class Relay1Thread (threading.Thread):
     def __init__(self,threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

     def run(self):
        blinkRelay1(self.name)

class Relay2Thread (threading.Thread):
     def __init__(self,threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

     def run(self):
        blinkRelay2(self.name)

def blinkRelay1(threadName):
   global count1
   while count1<=8:
      print('relay 1')
      count1+=1
      time.sleep(1)

def blinkRelay2(threadName):
       global count2
       while count2<=8:
        print('relay 2')
        count2+=1
        time.sleep(1)

# Create new threads

#Relay1
def stream_relay1(message):
      if message['path']== '/TurnOn':
          if message['data']==True:
              GPIO.output(27,GPIO.HIGH)
              print('Relay1-TurnOn-true')
          else:
              GPIO.output(27,GPIO.LOW)
              print('Relay1-TurnOn-false')

      if message['path']== '/Blink':
          global count1
          if message['data']==True:
              count1+=1
              thread1 = Relay1Thread(count1, "Relay1Thread")
              thread1.start()
              print('Relay1-Blink-true')
          else:
              print('Relay1-Blink-false')
#Relay2
def stream_relay2(message):
    if message['path']== '/TurnOn':
          if message['data']==True:
              print('Relay2-TurnOn-true')
          else:
              print('Relay2-TurnOn-false')

    if message['path']== '/Blink':
         global count2
         if message['data']==True:
              count2+=2
              thread2 = Relay2Thread(count2, "Relay2Thread")
              thread2.start()
              print('Relay2-Blink-true')
         else:
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
