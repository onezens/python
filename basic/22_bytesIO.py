#!/usr/bin/python
#encoding=utf8

#StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。

from io import BytesIO

f = BytesIO()

f.write('中文'.encode('utf8'))

print(f.getvalue())

print('*'*40)
#和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取：

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')

print(f.read())