import socket

client = socket.socket()
ipaddr = input('Connect to IP: ')
client.connect((ipaddr, 3000))
print( 'Connected to server')
while True:
	operator =input('Operator: ')
	operandA = input('Operand 1: ')
	operandB = input('Operand 2: ')
	client.send(operator.encode())
	client.send(operandA.encode())
	client.send(operandB.encode())
	hasil= client.recv(1024)
	print (hasil)
	if 'exit' == input('Type "exit" to exit, no input to continue '):
		client.send('exit')
		client.close()
		exit()