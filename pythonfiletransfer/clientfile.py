import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1',1234))
print('Connected......')

filename = input(str('Please enter a filename : '))
file = open(filename,'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close()
print('File have been received successfully')
s.close()