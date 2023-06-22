from threading import *
import os
#  Ways to acheive Threading 
# 1.Thread class in threading module 
# 2. without using thread class
# 3. by creating subclasses of thread class 

# get current thread name 
print(current_thread().getName())
# set name to current thread 
current_thread().setName("Sample thread")
print(current_thread().getName())

def cube(num,value=3):
    for i in range(1):
        # get the process id 
        print("Square Process id  1 : {}".format(os.getpid()))
        print("Cube : {} ".format(num**value))
def square(num):
    for i in range(1):
        print("Square Process id 2 : {}".format(os.getpid()))
        print("Square : {} ".format(num**2))
    

t1 = Thread(target=cube,args=(10,))
t1.start()

t2 = Thread(target=square,args=(10,))
t2.start()

# it will wait untill the thread reached ends 
t1.join()
t2.join()
print("Done ")
