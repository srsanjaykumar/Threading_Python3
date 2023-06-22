from threading import * 

l=RLock()

def display():
    l.acquire()
    