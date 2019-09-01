import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1025))
s.listen(5)
while (1):
	clt, adr = s.accept()
	print("Connection to  established")
	clt.send(bytes("socket progra,,ong","utf-8"))
