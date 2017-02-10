#!/usr/bin/python
#encoding=utf8

#通用异常信息处理方式
try: #可能发生异常的代码
	 open('123.txt', 'r')
except Exception, e:  #发生异常后执行
	print(e)
else: #没有发生异常之后执行
	pass
finally:  #不管有没有发生异常都会执行
	pass


#指定异常信息处理

try:
	print(a)
except (IOError, NameError), errorMsg:
	print("error message: %s" %errorMsg)
