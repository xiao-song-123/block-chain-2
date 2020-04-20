#!/usr/bin/python3

import threading
import time

exitFlag = 0

def song(threadID,name,counter):
    print(threadID,name,counter)
    for i in range(5):
        print("song")
        time.sleep(1)




# class myThread (threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#     def run(self):
#         print ("开始线程：" + self.name)
#         print_time(self.name, self.counter, 5)
#         print ("退出线程：" + self.name)

# def run():
#     threading.Thread(target=song,kwargs={"threadID":1,"name":'Thread-1', " counter":1})
#     threading.Thread(target=song,kwargs={"threadID":2,"name":'Thread-2', " counter":2})
#     print_time(song.name, song.counter, 5)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

threading.Thread(target=print_time, args=("Thread-1", 1, 5)).start()

# # 创建新线程
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
#print ("退出主线程")