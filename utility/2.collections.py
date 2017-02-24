#!/usr/bin/python3
#encoding=utf8

from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

Point = namedtuple('Point', ['x', 'y'])
# print(type(Point))

p = Point(1, 2)

print(p.x)
print(p.y)

# p.x = 3  AttributeError: can't set attribute
# print(p.x)
# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数
print(isinstance(p, Point))
print(isinstance(p, tuple))

#定义一个圆
Circle = namedtuple('Circle', ['x', 'y', 'r'])

#######################################################
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
# deque除了实现list的append()和pop()外，
# 还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

#######################################################
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。
# 如果希望key不存在时，返回一个默认值，就可以用defaultdict：
# 除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

#######################################################
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
# 如果要保持Key的顺序，可以用OrderedDict：
# 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d) #{'a': 1, 'c': 3, 'b': 2} key是无序的
print(type(d)) 

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)
od['z'] = 1
od['y'] = 3
od['x'] = 4
print(od)

print('*'*30)
# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
class LastUpdatedOrderedDict(OrderedDict):
	def __init__(self, capacity):
		super(LastUpdatedOrderedDict, self).__init__()
		self._capacity = capacity
	def __setitem__(self, key, value):
		containsKey = 1 if key in self else 0
		if len(self) - containsKey >= self._capacity:
			last = self.popitem(last=False)
			print('remove:', last)
		if containsKey:
			del self[key]
			print('set:', (key, value))
		else:
			print('add:', (key, value))
		OrderedDict.__setitem__(self, key, value)

updateDict = LastUpdatedOrderedDict(5)
updateDict['a'] = 1
updateDict['b'] = 1
updateDict['c'] = 1
updateDict['d'] = 1
updateDict['e'] = 1
print(updateDict)
updateDict['f'] = 1
updateDict['g'] = 1
print(updateDict)

#######################################################
# Counter是一个简单的计数器，例如，统计字符出现的个数：
c = Counter()
for ch in 'programming':
	c[ch] = c[ch]+1

print(c)















