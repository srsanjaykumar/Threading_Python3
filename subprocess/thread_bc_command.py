from subprocess import PIPE , STDOUT , Popen
from threading import *

class process_thread(Thread):
    def __init__(self,proc ):
        Thread.__init__(self)
        self.proc = proc
    def run(self):
        while not self.proc.stdout.closed:
            print(self.proc.stdout.readline().decode())


# linux bc command with arguments 
p = Popen(['bc','-q','-i'],stdout=PIPE,stdin=PIPE,stderr=STDOUT,shell=True)
# remaining information of commads using bc 
out=process_thread(p)
out.start()

while not p.stdout.closed:
    print("Process id : "+str(p.pid))
    query=input(' > ')
    # stripe is used to remove unwanted things in command 
    if query.strip() == "quit" or query.strip() == "exit":
        # here we pass input to bc  stdin  via python sbprocess   as  exit or quit     => it will exit bc  
        p.communicate(query.encode(),timeout=1)
        # poll is like a cycle 
        if p.poll() is not None:
            break
    query = query+"\n"
    #  we pass a input  like terminal  stdin        as same as we use in python subprocess 
    # we write a input to stdin in bc   by using  python subprocess 
    p.stdin.write(query.encode())

    # what ever we are write and read in stdin and stdout we need to flush that   
    # flush will push the data from another side
    p.stdin.flush()
    #  we read the input pass via bc command  and send out in stdout         in top 5-10 lines you analyse that 
    # we  get the output via stdout in bc via python subprocess 
    # we wont put decode we get a binary fromat output   example : 5+6  =>  b'11'
    # print(p.stdout.readline().decode().rstrip())



