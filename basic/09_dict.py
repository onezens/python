#!/usr/bin/python
#encoding=utf8

info = {"name":"xiaoming", "age":23, "sex":"male"}
print(info)

#获取info的所有的key
print(info.keys())

#获取所有的value
print(info.values())

#以数组元素的形式输出
print(info.items())

#获取某一个key的值
name = info['name']
print('name: %s'%name)

#获取一个不存在的key，并且设置默认值
print(info.get('home', 'www.baidu.com'))

#删除指定的key
del info['sex']
print('del info sex: %s'%info)

#遍历
for name,age in info.items():
	print('name: %s age: %s'%(name,age))

#清空整个字典
info.clear()
print("info is clear: %s "%info)

#判断是否拥有某一个key
print("info has key name: %s"%(info.has_key('name')))
