import  socket
from subprocess import PIPE , STDOUT , Popen
from threading import *

class process_thread(Thread):
    def __init__(self,proc ,conn):
        Thread.__init__(self)
        self.proc = proc
        self.conn = conn
    def run(self):
        while not self.proc.stdout.closed:
            conn.sendall(self.proc.stdout.readline())



HOST=''
PORT=6161
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR ,1 );
s.bind((HOST,PORT))
s.listen()
conn,addr=s.accept();

print("{} Conection with Back Port {}  ".format(addr[0],addr[1]) )
conn.sendall("You are Connected to Math server : Please give some Expression to execute : \n\n:> $".encode())
p = Popen(['bc'],stdout=PIPE,stdin=PIPE,stderr=STDOUT,shell=True)
out=process_thread(p,conn)
out.start()
print(p.stdout.closed)
while not p.stdout.closed:
# while True:
    data = conn.recv(1024);
    if not data:
        print("data Not avliable ")
        break
    else:
        print("Decoded data")
        query =data.decode().strip()
        if query.strip() == "quit" or query.strip() == "exit":
            print("Client pass exit ")
            p.communicate(query.encode(),timeout=1)
            if p.poll() is not None:
                break
        query = query+"\n"
        p.stdin.write(query.encode())
        p.stdin.flush()
print("bc command stdout  Closed  : ",p.stdout.closed)
# in line 11 and 12 we get a error using  while True  because  we pass exit  the bc command process is exited and thread is running    
s.close() 




