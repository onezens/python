#!/usr/bin/python3
#encoding=utf8

import pickle
import json

person = dict(name='xiaoming', age=20, sex='male')

b = pickle.dumps(person)

f = open('person.txt', 'wb')

pickle.dump(person,f)

f.close()

#person.txt 是乱码的，Python保存的对象内部信息

f = open('person.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)

#		JSON
jsonStr = json.dumps(person)
print(jsonStr)

personObject = json.loads(jsonStr)
print(personObject)
print(type (personObject))