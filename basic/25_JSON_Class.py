#!/usr/bin/python3
#encoding=utf8

import json

class student(object):
	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score
	def __str__(self):
		return 'name is ' + self.name + ' age is ' + str(self.age) + ' score is ' + str(self.score)


def studentToDict(stu):
	return {
		'name' : stu.name,
		'age' : stu.age,
		'score' : stu.score 
	}

def dictToStudent(dict):
	return student(dict['name'], dict['age'], dict['score'])


stu = student('xiaoming', 24, 100)
print(stu)

jsonStr = json.dumps(stu, default=studentToDict)
print(jsonStr)

stuObj = json.loads(jsonStr, object_hook=dictToStudent)
print(stuObj)
