#encoding=utf8
import urllib

f = urllib.urlopen('http://www.baidu.com')

firstLine = f.readline()

print(firstLine)
