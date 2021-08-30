import socket
conn=socket.socket()
host=input('teachers name:')
port=8080
conn.connect((host,port))
while True:
    imessage=conn.recv(1024)
    imessage=imessage.decode()
    print('Teacher:',imessage)
    omessage=input('studen>>>')
    omessage=omessage.encode()
    conn.send(omessage)
#learn:-
#Tkinker
#dialogflow
