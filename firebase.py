import pyrebase

config = {
  "apiKey": "uTP6tlP930oA1s9zuwGIZvrz1ef8ZjVLegROgNN0",
  "authDomain": "smarthome-5d11a.firebaseapp.com",
  "databaseURL": "https://smarthome-5d11a.firebaseio.com",
  "storageBucket": "smarthome-5d11a.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def stream_handler(message):
      print('data changed')
    # print(message["event"]) # put
    # print(message["path"]) # /-K7yGTTEp7O549EzTYtI
    # print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}

my_stream = db.child("user").stream(stream_handler)
