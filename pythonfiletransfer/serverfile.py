import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1',1234))
s.listen(5)
print('waiting for connection.....')
clt,addr=s.accept()
print(addr)

filename = input(str('Please enter file name : '))
file = open(filename, 'rb')
file_data = file.read(1024)
clt.send(file_data)
print('Data has been transitted successfully...')
clt.close()

