from threading import * 

class sanjaykumar(Thread):
    # we override the thread class run method 
    def run(self):
        for i in range(10):
            print("Sanjay kumar")

sk=sanjaykumar()
# here we acheive multi threading   %%%%
# child thread (start)    start method call run method internally
sk.start()

for i in range(10):
    print(i)