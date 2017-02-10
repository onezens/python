#!/usr/bin/python
#encoding=utf8

class ShortInputException(Exception):
	def __init__(self, length, atLast):
		Exception.__init__(self)
		self.length = length
		self.atLast = atLast


def testFun():
	try:
		s = raw_input('please random input a string: ')
		#如果s的长度小于3则抛出异常
		if len(s) < 3 :
			raise ShortInputException(len(s), 3)
	except EOFError:
		print("你输入一个结束标记EOF")
	except ShortInputException,error:
		print("ShortInputException: 输入长度: %d ， 长度至少: %d"%(error.length, error.atLast))
	except Exception, error:
		print(error)
	else:
		print("have no except")

while True:
	testFun()