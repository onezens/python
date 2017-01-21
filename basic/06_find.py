#!/usr/bin/python
#encoding=utf8

str = "This is a red Apple and I like eat Apple"

print(str.find("Apple"))

#find("搜索关键字", "开始位置", "搜索长度")
print(str.find("Apple",16,len(str)))

#right find 从右边开始查找
print(str.rfind("Apple"))

'''
index rindex 用法和find相同
区别：index 找不到关键字之后抛出异常
'''

print(str.index('Apple'))

print(str.rindex('Apple'))

print(str.rindex('iPhone'))
