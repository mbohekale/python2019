import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)
conn,cltaddr=s.accept()
data=conn.recv(1024)
conn.send(bytes("HELLO CLIENT",'utf-8'))
print(data)
conn.close()