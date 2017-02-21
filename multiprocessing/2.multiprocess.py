#!/usr/bin/python3
#encoding=utf8

from multiprocessing import Process
import os

#sub process run code
def run_subProcess(name):
	print('Run child process name is %s (%s)' %(name ,os.getpid()))

if __name__ == '__main__' :
	print('Parent process %s.' %os.getpid())
	p = Process(target=run_subProcess, args=('test',))
	print('Child process will start!')
	p.start()
	p.join()
	print('Child process end.')