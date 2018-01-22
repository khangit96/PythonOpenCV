import threading
import time
from queue import Queue

# count1= 0
# count2= 0


# class Relay1Thread (threading.Thread):
#      def __init__(self,threadID, name):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name

#      def run(self):
#         blinkRelay1(self.name)

# class Relay2Thread (threading.Thread):
#      def __init__(self,threadID, name):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name

#      def run(self):
#         blinkRelay2(self.name)

# def blinkRelay1(threadName):
#    global count1
#    while count1<=5:
#       print('relay 1')
#       count1+=1
#       time.sleep(1)

# def blinkRelay2(threadName):
#        global count2
#        while count2<=5:
#         print('relay 2')
#         count2+=1
#         time.sleep(1)

# # Create new threads

# threadList = ["Thread-1", "Thread-2", "Thread-3"]
# threads = []
# threadID = 1
# workQueue = Queue(10)

# for tName in threadList:
#        thread1 = Relay1Thread(threadID, "Relay1Thread",workQueue)
#        thread1.start()
#        threads.append(thread1)
#        threadID += 1
count=0

def worker():
    global count
    while count<=5:
        print('worker')
        count+=1
        if count==5:
           count=0
           t2 = threading.Thread(name='2',target=worker)
           t2.start()
           print('stop')

        time.sleep(1)

def worker1():
    global count
    while count<=5:
        print('worker')
        time.sleep(1)
    
t = threading.Thread(name='1',target=worker)
t.start()