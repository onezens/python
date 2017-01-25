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

#删除空格
name = '       xiaoming       '
print(name.strip())
print(name.rstrip())
print(name.lstrip())


#切割字符串partition
#与split相似
#区别partition包括根据切割的字符串

name = "Apple is red, pipe is yellogreen"
print(name.partition('is'))
#print(name.lpartition('is'))
print(name.rpartition('is'))

#判断字符串的类型

str = '    '
print(str.isspace()) #判断是否是纯空格
str = 'abd'
print(str.isalpha()) #判断是否是纯字母
str = '1231'
print(str.isdigit()) #判断是否是纯数字
str = 'abc234'
print(str.isalnum())  #是否是混合

#将数组转换为字符串
arr = ['xiaoming', 'danny', 'xiaowang']
joinStr = '_'
print(joinStr.join(arr))

