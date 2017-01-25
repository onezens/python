#encoding=utf8
list = ['xiaoming', 'xiaohua', 'xiaozhang']

print('original list items: %s'%list)

print('*'*20)
#增
list.append('xiaoli')#拼接到最后面
list.insert(0,'xiaoqi') #插入到指定索引的位置
print('list items: %s'%list)
list1 = [1, 2, 3]
list.extend(list1) #将list1中所有德尔元素，拼接到list的后面
print('list items for extend : %s'%list)
print('*'*20)

#删
del list[0] #删除指定索引的元素
print(list)

list.pop()  #最后面删除
print(list)

list.remove('xiaoli') #根据元素进行删除
print(list)

print('*'*20)
#改
list[1]='second'
print(list)

print('*'*20)
#查

if 'xiaoming' in list:
	print('xiaoming in list')
else:
	print('xiaoming not in list')

if 'xiaoming' not in list:
	print('xiaoming not in the list')
else:
	print('xiaoming in the list')

position = list.index('second')

print('second index of list : %d'%position)

#listLen = count(list)
#print('list length: %d'%listLen)
