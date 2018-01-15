from gtts import gTTS
import os

tts = gTTS(text='Tên gì hả?', lang='vi', slow=False)
tts.save("good.mp3")
os.system("mpg321 good.mp3")

