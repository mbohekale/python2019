import socket
s=socket.socket()
s.bind((socket.gethostname(),1234))
s.listen(5)
print('ready to connect......')

conn,addr = s.accept()
print(addr)
while True:
	data = []
	data.append(conn.recv(1024))
	if data[0] == 'exit':
		print ('Exiting')
		s.close()
		conn.close()
		break
	data.append(conn.recv(1024))
	data.append(conn.recv(1024))
	if data[1] == '+':
		hasil = int(data[0]) + int(data[2])
	elif data[1] == '-':
		hasil = int(data[0]) - int(data[2])
	elif data[1] == '*':
		hasil = int(data[0]) * int(data[2])
	elif data[1] == '/':
		hasil = int(data[0]) / int(data[2])
	print( data[0], data[1], data[2], '=', hasil)
	conn.send(bytes(hasil,'utf-8'))
conn.close()