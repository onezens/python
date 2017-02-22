#!/usr/bin/python
#encoding=utf8

from multiprocessing import Process, Queue
import os, time, random

#wirte data process execute code
def write(q):
	print('process to write : %s'%os.getpid())
	for value in ['A', 'B', 'C']:
		print('put %s to queue...'%value)
		q.put(value)
		time.sleep(random.random())

#execute code for read data process
def read(q):
	print('process to read : %s'%os.getpid())
	while True:
		value = q.get(True)
		print('Get %s from queue.'%value)

if __name__ == '__main__' :
	#父进程创建Queue，并传给各个子进程
	q = Queue()
	pw = Process(target=write, args=(q,))
	pr = Process(target=read, args=(q,))
	#启动子进程pw ，写入
	pw.start()
	#启动子进程pr，读取
	pr.start()
	#等待pw结束
	pw.join()
	#pr进程死循环，无法等待结束，强行终止
	pr.terminate()