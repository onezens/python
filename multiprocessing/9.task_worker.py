#!/usr/bin/python
#encoding=utf8

import time, sys, queue
from multiprocessing.managers import BaseManager

#创建一个子类
class QueueManager(BaseManager):
	pass

#由于QueueManager只从网络上获取Queue，所以注册时只提供名字
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

#连接到服务器，也就是task_master.py
server_addr = '127.0.0.1'
print('Connect to server %s ...' %server_addr)

#端口和验证码注意保持于task_master.py设置完全一致
#authkey有什么用？这是为了保证两台机器正常通信，不被其他机器恶意干扰
m = QueueManager(address=(server_addr, 5000), authkey=b'abc') 
# 从网络连接
m.connect()
# 获取queue对象
task = m.get_task_queue()
result = m.get_result_queue()

#从task队列取任务，并把结果写入result队列
for i in range(10):
	try:
		n = task.get(timeout=1)
		print('run task %d * %d  ....'%(n, n))
		r = '%d * %d = %d' %(n, n, n*n)
		time.sleep(1)
		result.put(r)
	except Queue.Empty:
		print('task queue is empty!')

#结束
print('worker exit.')