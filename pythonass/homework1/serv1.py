import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)
while True:
	conn,cltaddr=s.accept()
	print(cltaddr)
	
	f_client=''
	while True:
		data=conn.recv(1024)
		print("Received from client: ",data)
		if(data=="Hello server"):
			conn.send(bytes("Hello Client",'utf-8'))
			print("Reply have been sent and the process completed!")
		elif(data=="Disconnect"):
			conn.send(bytes("Goodbye",'utf-8'))
		else:
			conn.send(bytes("Hello Client",'utf-8'))
		conn.close()
		break
		print('client disconnect')