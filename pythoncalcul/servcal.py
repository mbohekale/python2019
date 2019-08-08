import socket

server = socket.socket()
server.bind(('', 3000))
print( 'Server ready at 127.0.0.1')
server.listen(1)
client, address = server.accept()
print ('Got connection from', address)
while True:
	data = []
	data1=client.recv(1024)
	if data == 'exit':
		print ('Exiting')
		server.close()
		client.close()
		break
	data2=client.recv(1024)
	data3=client.recv(1024)
	if data1 == '+':
			hasil =( int(data2) + int(data3))
			msg=hasil
	elif data1 == '-':
		hasil = (int(data2) - int(data3))
	elif data1 == '*':
		hasil = int(data[1]) * int(data[2])
	elif data1 == '/':
		hasil = int(data[1]) / int(data[2])
	print('hasil: ',(int(data2)+int(data3)))
	print('hasil: ',(int(data2)-int(data3)))
	client.send(bytes('data2','utf-8')+bytes('+','utf-8')+bytes('data3','utf-8'))