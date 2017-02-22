#!/usr/bin/python
#encoding=utf8

import time, threading

# 进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程
# execute code for new thread
def loop():
	print('thread %s is running...' %threading.current_thread().name)
	n = 0
	while n<5:
		n += 1
		print('thread %s >>> %s' %(threading.current_thread().name, n))
		time.sleep(1)
	print('thread %s ended.' % threading.current_thread().name)

print('threading %s is running......' %threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended...' %threading.current_thread().name)