#encoding=utf8
from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

print('html content:  ' + html)

#转换成 BeautifulSoup 对象
soup = BeautifulSoup(html)

#获取html标签的title
print(soup.title)

#获取内容
print(soup.title.string)

#获取所有的a标签的内容
for link in soup.find_all('a'):
	print(link)

#获取所有一个标签的属性
linkAttrs = soup.a.attrs

print(linkAttrs)

#从文档中获取所有文字内容:
print(soup.get_text())

#选择器
print(soup.select('#link3'))

print(soup.select('.sister'))

print(soup.select('title'))

print(soup.select('a[href="http://example.com/tillie"]'))

print(soup.select('p[class="story"]'))