#!/usr/bin/python
#encoding=utf8

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1', 9999))

print(client.recv(1024).decode('utf8'))
for data in [b'Xiaoming', b'Xiaohua', b'Xiaomwang']:
	client.send(data)
	print(client.recv(1024).decode('utf8'))


client.send(b'exit')
client.close()