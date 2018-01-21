import threading
import time

count1= 0
count2= 0


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
   while count1<=5:
      print('relay 1')
      count1+=1
      time.sleep(1)

def blinkRelay2(threadName):
       global count2
       while count2<=5:
        print('relay 2')
        count2+=1
        time.sleep(1)

# Create new threads
thread1 = Relay1Thread(1, "Relay1Thread")
thread2 = Relay2Thread(2, "Relay2Thread")

# Start new Threads
thread1.start()
thread2.start()
