import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))
s.send(bytes("HELLO SERVER",'utf-8'))
data=s.recv(1024)
print(data)
s.close()