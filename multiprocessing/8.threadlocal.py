#!/usr/bin/python
#encoding=utf8

import threading

# 不同的线程之间传递数据，防止数据混乱
######################################

global_dict = {}

class Student(object):
	def __init__(self, name):
		self.name = name


def std_thread(name):
	std = Student(name)
	global_dict[threading.current_thread()] = std
	do_task1()
	do_task2()

def do_task1():
	std = global_dict[threading.current_thread()]

def do_task2():
	std = global_dict[threading.current_thread()]


######################################
# 通过 ThreadLocal 替换上面的字典
# ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，
# HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。
# 创建全局ThreadLocal变量
local_school = threading.local()


def process_student():
	std = local_school.student
	print('Hello, %s in thread: %s'%(std, threading.current_thread().name))

def process_thread(name):
	local_school.student = name 
	process_student()

t1 = threading.Thread(target = process_thread, args=('xiaoming',), name='Thread_A')
t2 = threading.Thread(target = process_thread, args=('xiaohua',), name='Thread_B')
t1.start()
t2.start()
t1.join()
t2.join()

# 一个ThreadLocal变量虽然是全局变量，
# 但每个线程都只能读写自己线程的独立副本，互不干扰。
# ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。

