#!/usr/bin/python3
#encoding=utf8

#windows 下面不能运行
import os

print('Processing (%s) starting...' %os.getpid())

# Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次
# 但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），
# 然后，分别在父进程和子进程内返回。

# 子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，
# 一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，
# 而子进程只需要调用getppid()就可以拿到父进程的ID。 pid = os.fork()

if pid == 0 :
	print('I am child process (%s) and my parent is (%s) '%(os.getpid(), os.getppid()))
else:
	print('I (%s) just created a child process (%s)' %(os.getpid(), pid))

# 有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，
# 常见的Apache服务器就是由父进程监听端口，
# 每当有新的http请求时，就fork出子进程来处理新的http请求。