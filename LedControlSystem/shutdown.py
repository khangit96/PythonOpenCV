import RPi.GPIO as GPIO
import subprocess
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
count=0
while True:
    input_state = GPIO.input(26)
    if input_state == False:
        subprocess.call(['shutdown', '-h', 'now'], shell=False)
        time.sleep(0.2)

