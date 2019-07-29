import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))
s.send(bytes("Hello Server\n",'utf-8'))
Message=s.recv(16)
print("Received from server:",Message)
s.close()