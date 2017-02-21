#!/usr/bin/python
#encoding=utf8

from io import StringIO

#python3 的语法
#StringIO顾名思义就是在内存中读写str。
f = StringIO()

f.write('Hello')

f.write(' ')

f.write('world!')

print(f.getvalue())
print('*'*40)
#初始化一个StringIO

f = StringIO('Hello!\nWorld!\nGoodBye!')
while True:
	s = f.readline()
	if s == '':
		break
	print(s)