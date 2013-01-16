/usr/bin/env python2.7
/etc/init.d

import socket
import hashlib

HOST = ''
PORT = 1337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)

while 1:
	conn, addr = s.accept()
	while 1:
		data = conn.recv(4096)
		x = data.find('|')
		if x < 0 or ((' ' in data) == True):
			conn.send('Invalid Input: "|" or " "\n')
		else:
			hash = hashlib.sha256(data).hexdigest()
			conn.send(data)
			conn.send(hash + "\n")
	s.sock.close()