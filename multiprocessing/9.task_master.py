#!/usr/bin/python
#encoding=utf8

import random, time, queue
from multiprocessing.managers import BaseManager

# 发送任务队列
task_queue = queue.Queue()
# 接受结果的队列
result_queue = queue.Queue()

#从BaseManager继承QueueManager
class QueueManager(BaseManager):
	pass

# 把两个Queue都注册到网络上， callable参数关联了Queue对象
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
#绑定端口
manager = QueueManager(address=('', 5000), authkey=b'abc')
# 启动Queue
manager.start()
# 获得通过网络访问的Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()
# 添加几个任务
for i in range(10):
	n = random.randint(0, 10000)
	print('Put task %d...'%n)
	task.put(n)

# 从result队列读取结果
print('Try get results....')
for i in range(10):
	r = result.get(timeout=20)
	print('Result: %s' %r)

# 关闭
manager.shutdown()
print('master exit.')