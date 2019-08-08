import socket
s=socket.socket()
s.connect((socket.gethostname(),1234))
while True:
	operator = input('Operator: ')
	operandA = input('Operand 1: ')
	operandB = input('Operand 2: ')
	s.send(bytes(operandA,'utf-8'))
	s.send(bytes(operator,'utf-8'))
	s.send(bytes(operandB,'utf-8'))
	print( 'Hasil:', s.recv(1024))
	if 'exit' == input('Type "exit" to exit, no input to continue '):
		s.send('exit')
		s.close()
		exit()
