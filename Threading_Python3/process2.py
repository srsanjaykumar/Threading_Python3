from threading import * 

class sumo():
    def java(self):
        for i in range(10):
            print(i)


s=sumo()

# two apporach  
Thread(target=s.java())

Thread(target=s.java).start()
