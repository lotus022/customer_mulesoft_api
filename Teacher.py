import socket
s=socket.socket()
host =socket.gethostname()
port=8080
print('I am avilable at host',host)
s.bind((host,port))
s.listen(1)
conn,addr=s.accept()
if conn!=None:
    print('I am connected at',addr)
while True:
    message=input('Student>>>')
    message=message.encode()
    conn.send(message)
    imessage=conn.recv(1024)
    imessage=message.decode()
    print('Student:',imessage)