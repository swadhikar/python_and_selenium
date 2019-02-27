# Python script to run a process in different thread
from time import sleep
from threading import Thread

def sleeper(i):
    print "Thread {} sleeps for 2 seconds".format(i)
    sleep(2)
    print "Thread {} woke up...".format(i)

for i in xrange(10):
    t = Thread(target=sleeper, args=(i,))
    t.start()
    sleep(0.025)

"""
Output:
c:\Users\swadhi\Documents\bitbucket\pyselenium\PySelenium\test\BoA\threads>python first_thread.py
Thread 0 sleeps for 2 seconds
Thread 1 sleeps for 2 seconds
Thread 2 sleeps for 2 seconds
Thread 3 sleeps for 2 seconds
Thread 4 sleeps for 2 seconds
Thread 5 sleeps for 2 seconds
Thread 6 sleeps for 2 seconds
Thread 7 sleeps for 2 seconds
Thread 8 sleeps for 2 seconds
Thread 9 sleeps for 2 seconds
Thread 0 woke up...
Thread 1 woke up...
Thread 2 woke up...
Thread 3 woke up...
Thread 4 woke up...
Thread 5 woke up...
Thread 6 woke up...
Thread 7 woke up...
Thread 8 woke up...
Thread 9 woke up...
"""
