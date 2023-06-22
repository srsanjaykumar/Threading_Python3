from threading import * 
import time 

# In real time we use to login with a single device  like netflix used in tv or mobile phone => once it will lock the partcular device 
#  incase we won't use Lock() we get a deadlock probelm 

# RLock  is reccursive lock 
l=Lock()
def display(name):
    l.acquire() # Thread acquire this lock 
    print("HI : ",end="")
    print(current_thread())
   
    for i in range(15):
        print(i)
    time.sleep(1)
    print(name)
    l.release() # Thread release this lock 

name1="sanjay"
name2="Kumar"

# here we doesnot get a proper input in order way  . so we lock the particular thread 
Thread(target=display, args=(name1,)).start()

Thread(target=display , args=(name2,)).start()

# it will work in sequence order
# Thread(target=display(name1)).start()
# Thread(target=display(name2)).start()
