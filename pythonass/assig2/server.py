import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
sock.bind(server_address)
sock.listen(5)
while True:
          clientsocket,addr=sock.accept()
          print(addr)
          clientsocket.send(bytes("welcome to server","utf-8"))
          clientsocket.close()
         


