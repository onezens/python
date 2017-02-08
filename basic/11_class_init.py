#/usr/bin/pyhton3
#encoding=utf8

class dog:

	def __init__(self):
		self.weight = 10
		self.color = 'yellow'
		self.name = 'dog'

	def eat(self):
		self.weight+= 10
	#对类的描述信息的重写
	def __str__(self):
		msg = 'My name is ' + self.name + ' weight is ' + str(self.weight) + ' color is ' + self.color
		return msg

xiaogou = dog();

print(xiaogou.weight);
print(xiaogou.color);

xiaogou.eat();

print(xiaogou.weight)

print(xiaogou)
