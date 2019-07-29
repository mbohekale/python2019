import socket
host="localhost"
port=10000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host,port))
Message = ""
while True:
    msg=sock.recv(8)
    if len(msg) <=0:
        break
		Message += msg.decode("utf-8")
    print(msg.decode('utf-8'))

