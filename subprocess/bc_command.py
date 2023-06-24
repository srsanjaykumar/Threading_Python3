from subprocess import PIPE , STDOUT , Popen

# linux bc command with arguments 
p = Popen(['bc','-q','-i'],stdout=PIPE,stdin=PIPE,stderr=STDOUT,shell=True)
# remaining information of commads using bc 

# this wil read the output of bc command at first 4 line    use bc command    dont use bc -q -i 
# print(p.stdout.readline().strip())
# print(p.stdout.readline().strip())
# print(p.stdout.readline().strip())
# print(p.stdout.readline().strip())
# print(p.stdout.readline().strip())

#  communicate is used to  pass the input via stdin in bc  
# result = p.communicate('1+2\n'.encode())
# print("Result type : "+ str(type(result)))
# print(result[0].rstrip())




"""
print("Process ID : "+str(p.pid))
while True:
        # each and every time it will create new process id 
        # p = Popen(['bc','-q','-i'],stdout=PIPE,stdin=PIPE,stderr=STDOUT,shell=True)
        print("Process ID : "+str(p.pid))
        query=input(" > ")
        if query.strip()=="quit"or query.strip()=="exit":
            print("Closed .....")
            break
        else:
            query=query+"\n"
            result=p.communicate(query.encode(),timeout=1)
            print(result[0].rstrip())
          """
              
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
    print(p.stdout.readline().rstrip())



# we use subprocess to directly connunicate the stdin , stdout , stderr  to pass an input and output 