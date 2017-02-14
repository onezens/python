#!/usr/bin/python
#encoding=utf8


try:
	f = open('./test.txt', 'r')
	print(f.read())
finally:
	if f:
		f.close()

print('*'*30)
#但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：
with open('./test.txt', 'r') as f:
	print(f.read())

#如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；
#如果是配置文件，调用readlines()最方便：

f = open('./test.txt', 'r')

for line in f.readlines():
    print('--> %s'%line.strip()) # 把末尾的'\n'删掉


print('*'*30)
#二进制读取(图片、视频)
f = open('./test.txt', 'rb')
print(f.read())

#指定编码读取
f = open('./test.txt', 'r', encoding='gbk')