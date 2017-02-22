#!/usr/bin/python
#encoding=utf8

import time, threading

#银行卡余额
balance = 0

lock = threading.Lock()

#先存后取
def change_it(n):
	global balance
	balance = balance + n
	balance = balance - n

#代码执行的时候因为多线程的关系，会造成数据混乱
def run_thread(n):
	for i in range(100000):
		change_it(n)

def run_thread_new(n):
	for i in range(100000):
		#获取锁
		lock.acquire()
		try:
			change_it(n)
		finally:
			#释放锁
			lock.release()

# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
t1 = threading.Thread(target=run_thread_new, args=(5,))
t2 = threading.Thread(target=run_thread_new, args=(8,))

t1.start()
t2.start()
t1.join()
t2.join()
print(balance)