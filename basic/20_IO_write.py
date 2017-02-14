#!/usr/bin/python
#encoding=utf8

#替换原先的文本
with open('./test1.txt', 'w') as f :
	f.write('Hello world! ----> write')


with open('./test.txt', 'r') as f :
	print(f.read())