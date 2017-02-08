#!/usr/bin/python
#encoding=utf8

class dog:
	def bark(self):
		print("wang wang ....")

	def run(self):
		print("dog is running")


xiaohuang = dog();
xiaohuang.bark();
xiaohuang.run();

#添加属性
xiaohuang.name = "xiaohuang";
xiaohuang.weight = 12;


#获取属性
print(xiaohuang.name)
print(xiaohuang.weight)
