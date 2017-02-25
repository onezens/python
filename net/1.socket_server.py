#!/usr/bin/python
#encoding=utf8

import socket, threading, time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 9999))
# 传入的参数指定等待连接的最大数量
server.listen(5)
print('Waiting for connection...')


def tcplink(sock, addr):
	print('Accept new connection from %s:%s...' %addr)
	sock.send(b'Welcome!')
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf8') == 'exit':
			break
		sock.send(('Hello, %s!' %data.decode('utf8')).encode('utf8'))
	sock.close()
	print('Connection from %s:%s closed.' %addr)

while True:
	# 接受一个新连接
	sock, addr = server.accept()
	t = threading.Thread(target=tcplink, args=(sock, addr))
	t.start()


