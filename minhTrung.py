import pyrebase

#init Firebase
config = {
  "apiKey": "uTP6tlP930oA1s9zuwGIZvrz1ef8ZjVLegROgNN0",
  "authDomain": "smarthome-5d11a.firebaseapp.com",
  "databaseURL": "https://smarthome-5d11a.firebaseio.com",
  "storageBucket": "smarthome-5d11a.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

#Relay1
def stream_relay1(message):
      if message['path']== '/TurnOn':
          if message['data']==True:
              print('Relay1-TurnOn-true')
          else:
              print('Relay1-TurnOn-false')

      if message['path']== '/Blink':
          if message['data']==True:
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
         if message['data']==True:
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