import socket
host='localhost'
hostname=socket.gethostname()
print(hostname)
hostname=socket.gethostbyaddr('inf.elte.hu')
print(hostname)
hostname, aliases, addrs = socket.gethostbyaddr('157.181.161.79')
print(hostname, aliases, addrs)

