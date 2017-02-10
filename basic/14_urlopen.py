#encoding=utf8
import urllib

f = urllib.urlopen('http://www.baidu.com')

firstLine = f.readline()

print(firstLine)

print('status code: ' + str(f.getcode()))

print('url: ' + f.geturl())

print('headers: %s'%f.info().headers)

#将获取的html保存到指定的路径
 urllib.urlretrieve('http://www.baidu.com', '/Users/wangzhen/Desktop/Zhen/git/python/basic/1.html')


