#!/usr/bin/python3
#encoding=utf8

import os

#操作系统类型
print(os.name)

#操作系统的详细信息
print(os.uname)

#环境变量
print(os.environ)

#获取某个环境变量的值
print(os.environ.get('PATH'))

#当前目录的绝对路径
print(os.path.abspath('.'))

#添加一个路径的新路径
newDir = os.path.join(os.path.abspath('.'), 'os_path_join_dir')
print(newDir)

#创建一个目录
# os.mkdir(newDir)


#移除一个目录
#os.rmdir(newDir)

#拆分路径
print(os.path.split('/Users/michael/testdir/file.txt'))

#可以直接让你得到文件扩展名
print(os.path.splitext('/Users/michael/testdir/file.txt'))

# 对文件重命名:
# os.rename('test.txt', 'test.py')
# 删掉文件:
# os.remove('test.py')

#获取当前路径的所有文件和目录
print(os.listdir('.'))

#判断路径是不是文件夹
filePath =  os.path.join(os.path.abspath('.'), '1.html')
print(filePath)
print(os.path.isdir(filePath))
dirPath = os.path.join(os.path.abspath('.'), 'images')
print(dirPath)
print(os.path.isdir(dirPath))

#判断路径是不是文件
print(os.path.isfile(filePath))

#列出当前路径所有以py结尾的文件
files = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(files)





