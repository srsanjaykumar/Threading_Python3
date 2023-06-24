from threading import * 
l=RLock()
def recrusion(num):
    # l.acquire()
    if num ==0: 
        return 1 
    else : 
        # l.release()
        return num * recrusion(num-1)
        
       
def recr(num):
    print(recrusion(num))      
        


Thread(target=recr , args=(5,)).start()
Thread(target=recr , args=(15,)).start()
Thread(target=recr , args=(25,)).start()
# print(Thread(target=recr , args=(4,)).start())
