import wget
import os
import requests
import json

API_ENDPOINT = "http://api.openfpt.vn/text2speech/v4"

headers={
      'api_key':'44c319aae94d40229d7cc09f1ce759f1',
      'speed':'0',
      'voice': 'hatieumai',
      'prosody':'1',
      'Cache-Control':'no-cache'
}
data='Nhà có trộm kìa'
data = data.encode(encoding='utf-8')
r = requests.post(url = API_ENDPOINT,data=data,headers=headers)

url =r.json()['async']
filename = wget.download(url)
fileMp3='mpg321 '+filename
os.system('mv '+filename+' voice.mp3')
os.system("mpg321 voice.mp3")