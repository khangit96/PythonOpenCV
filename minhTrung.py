import pyrebase
import RPi.GPIO as GPIO
import time
import threading
import urllib.request

#Check WifiConnect
checkWifiConnect=False

while not checkWifiConnect:
  try:
    url = "https://www.google.com"
    urllib.request.urlopen(url)
    checkWifiConnect = True
  except:
    checkWifiConnect= False

print('startee')

#init Firebase
config = {
  "apiKey": "uTP6tlP930oA1s9zuwGIZvrz1ef8ZjVLegROgNN0",
  "authDomain": "smarthome-5d11a.firebaseapp.com",
  "databaseURL": "https://smarthome-5d11a.firebaseio.com",
  "storageBucket": "smarthome-5d11a.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

#Init Relay
RELAY_1=27
RELAY_2=22
RELAY_3=10
RELAY_4=9
RELAY_5=11
RELAY_6=5

#init GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(RELAY_1,GPIO.OUT)
GPIO.setup(RELAY_2,GPIO.OUT)
GPIO.setup(RELAY_3,GPIO.OUT)
GPIO.setup(RELAY_4,GPIO.OUT)
GPIO.setup(RELAY_5,GPIO.OUT)
GPIO.setup(RELAY_6,GPIO.OUT)

#Blink Relay
def blinkRelay(gpio):
      GPIO.output(gpio,GPIO.LOW)
      time.sleep(1)
      GPIO.output(gpio,GPIO.HIGH)
      time.sleep(1)
      print('')

#TurnOn
def turnOn(gpio):
    GPIO.output(gpio,GPIO.HIGH)
    print('')

#TurnOff
def turnOff(gpio):
    GPIO.output(gpio,GPIO.LOW)
    print('')
    
#Worker Relay1
def worker1():
    global checkRelay1
    while checkRelay1:
         print('worker 1')
         blinkRelay(RELAY_1)

#Worker Relay2
def worker2():
    global checkRelay2
    while checkRelay2:
        print('worker 2')
        blinkRelay(RELAY_2)

#Worker Relay3        
def worker3():
    global checkRelay3
    while checkRelay3:
        print('worker 3')
        blinkRelay(RELAY_3)

#Worker Relay4
def worker4():
    global checkRelay4
    while checkRelay4:
        print('worker 4')
        blinkRelay(RELAY_4)

#Worker Relay5        
def worker5():
    global checkRelay5
    while checkRelay5:
        print('worker 5')
        blinkRelay(RELAY_5)

#Worker Relay6
def worker6():
    global checkRelay6
    while checkRelay6:
        print('worker 6')
        blinkRelay(RELAY_6)
#Set GPIO
def setGPIO(gpio,child):
    blink=db.child(child+'Blink').get()
    turnon=db.child(child+'TurnOn').get()
    
    if  turnon.val():
        turnOn(gpio)
        print('turnOn true:'+child)
               
    if blink.val():
        if gpio==RELAY_1:
            global checkRelay1
            checkRelay1=True
            t = threading.Thread(name='1',target=worker1)
            t.start()
        elif gpio==RELAY_2:
            global checkRelay2
            checkRelay2=True
            t = threading.Thread(name='1',target=worker2)
            t.start()
        elif gpio==RELAY_3:
            global checkRelay3
            checkRelay3=True
            t = threading.Thread(name='1',target=worker3)
            t.start()
        elif gpio==RELAY_4:
            global checkRelay4
            checkRelay4=True
            t = threading.Thread(name='1',target=worker4)
            t.start()
        elif gpio==RELAY_5:
            global checkRelay5
            checkRelay5=True
            t = threading.Thread(name='1',target=worker5)
            t.start()
        elif gpio==RELAY_6:
            global checkRelay6
            checkRelay6=True
            t = threading.Thread(name='1',target=worker6)
            t.start()

        #blinkRelay(gpio)

#Restore GPIO
setGPIO(RELAY_1,'MinhTrung/Relay1/')
setGPIO(RELAY_2,'MinhTrung/Relay2/')
setGPIO(RELAY_3,'MinhTrung/Relay3/')
setGPIO(RELAY_4,'MinhTrung/Relay4/')
setGPIO(RELAY_5,'MinhTrung/Relay5/')
setGPIO(RELAY_6,'MinhTrung/Relay6/')

#Thread
checkRelay1=False
checkRelay2=False
checkRelay3=False
checkRelay4=False
checkRelay5=False
checkRelay6=False
    
#Stream Relay1
def stream_relay1(message):
      if message['path']== '/TurnOn':
          if message['data']:
              turnOn(RELAY_1)
              print('Relay1-TurnOn-true')
              
          else:
              turnOff(RELAY_1)
              print('Relay1-TurnOn-false')

      if message['path']== '/Blink':
          if message['data']:
             if GPIO.input(RELAY_1)==1:
                 global checkRelay1
                 checkRelay1=True
                 t = threading.Thread(name='1',target=worker1)
                 t.start()
                 print('Relay1-Blink-true')
          else:
              global checkRelay1
              checkRelay1=False
              print('Relay1-Blink-false')

#Stream Relay2
def stream_relay2(message):
    if message['path']== '/TurnOn':
          if message['data']:
              turnOn(RELAY_2)
              print('Relay2-TurnOn-true')
          else:
              turnOff(RELAY_2)
              print('Relay2-TurnOn-False')
        
    if message['path']== '/Blink':
         if message['data']:
             if GPIO.input(RELAY_2)==1:
                 global checkRelay2
                 checkRelay2=True
                 t = threading.Thread(name='1',target=worker2)
                 t.start()
                 print('Relay2-Blink-True')
         else:
            global checkRelay2
            checkRelay2=False
            print('Relay2-Blink-False')

            
            
#Relay3
def stream_relay3(message):
    if message['path']== '/TurnOn':
          if message['data']:
              turnOn(RELAY_3)
              print('Relay3-TurnOn-true')
          else:
              turnOff(RELAY_3)
              print('Relay3-TurnOn-False')
        
    if message['path']== '/Blink':
         if message['data']:
             if GPIO.input(RELAY_3)==1:
                 global checkRelay3
                 checkRelay3=True
                 t = threading.Thread(name='1',target=worker3)
                 t.start()
                 print('Relay3-Blink-True')     
         else:
            global checkRelay3
            checkRelay3=False
            print('Relay3-Blink-False')  
#Relay4
def stream_relay4(message):
    if message['path']== '/TurnOn':
          if message['data']:
              turnOn(RELAY_4)
              print('Relay4-TurnOn-true')
          else:
              turnOff(RELAY_4)
              print('Relay4-TurnOn-False')  
        
    if message['path']== '/Blink':
         if message['data']:
             if GPIO.input(RELAY_4)==1:
                 global checkRelay4
                 checkRelay4=True
                 t = threading.Thread(name='1',target=worker4)
                 t.start()     
                 print('Relay4-Blink-True')  
         else:
            global checkRelay4
            checkRelay4=False
            print('Relay4-Blink-False')  

#Relay5
def stream_relay5(message):
    if message['path']== '/TurnOn':
          if message['data']:
              turnOn(RELAY_5)
              print('Relay5-TurnOn-true')
          else:
              turnOff(RELAY_5)
              print('Relay5-TurnOn-False')
        
    if message['path']== '/Blink':
         if message['data']:
             if GPIO.input(RELAY_5)==1:
                 global checkRelay5
                 checkRelay5=True
                 t = threading.Thread(name='1',target=worker5)
                 t.start()
                 print('Relay5-Blink-true')     
         else:
              global checkRelay5
              checkRelay5=False
              print('Relay5-Blink-False')
                          
#Relay6
def stream_relay6(message):
    if message['path']== '/TurnOn':
          if message['data']:
              turnOn(RELAY_6)
              print('Relay6-TurnOn-true')
          else:
              turnOff(RELAY_6)
              print('Relay6-TurnOn-False')
        
    if message['path']== '/Blink':
         if message['data']:
             if GPIO.input(RELAY_6)==1:
                 global checkRelay6
                 checkRelay6=True
                 t = threading.Thread(name='1',target=worker6)
                 t.start()
                 print('Relay6-Blink-true')     
         else:
            global checkRelay6
            checkRelay6=False
            print('Relay6-Blink-False')

relay1 = db.child("MinhTrung/Relay1").stream(stream_relay1)
relay2 = db.child("MinhTrung/Relay2").stream(stream_relay2)
relay3 = db.child("MinhTrung/Relay3").stream(stream_relay3)

relay4 = db.child("MinhTrung/Relay4").stream(stream_relay4)
relay5 = db.child("MinhTrung/Relay5").stream(stream_relay5)
relay6 = db.child("MinhTrung/Relay6").stream(stream_relay6)
