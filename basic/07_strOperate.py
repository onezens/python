#!/usr/bin/python
#encoding=utf8

str = 'This is a red Apple and I like eat Apple'
#将所有的关键字替换
print(str.replace('Apple', 'Orange'))
#替换一个关键字
print(str.replace('Apple', 'Orange', 1))

str = 'hehehe hahaha heiheiehei'

#将字符串根据空格分开
print(str.split(' '))
#只分割一个
print(str.split(' ', 1))

#将字符串的首字母转换为大写
print(str.capitalize())

#将字符串中的所有的单词大写
print(str.title())

#转换为大写
print(str.upper())

#转换为小写
newStr = str.upper()
print(newStr.lower())

#判断是否以某一个东西开始或者结束
print(str.startswith('hehehe'))
print(str.endswith('hei'))

#补空格
print(str.ljust(10))
print(str.rjust(20))
print(str.center(20))

newstr = str.center(20)
print(newstr)
