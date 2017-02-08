#!/usr/bin/python
#encoding=utf8

class person(object):

	def __init__(self, name, age):
		self.__name = name
		self.__age = age

	def __str__(self):
		msg = "My name is " + self.__name + " age is " + str(self.__age)
		return msg

	def setAge(self, age):
		self.__age = age

	def getAge(self):
		return self.__age

	def __runing(self):
		print('this is private methon')

	#对象销毁的时候调用
	def __del__(self):
		print("**********dealloc*************")

xiaoming = person('xiaoming', 20)

print(xiaoming.getAge())

xiaoming.setAge(24)

print(xiaoming.getAge())

print(xiaoming)

#手动销毁一个对象
del xiaoming

xiaohua = person('xiaohua', 20)

print(xiaohua)
