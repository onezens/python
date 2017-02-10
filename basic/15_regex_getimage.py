#encoding=utf8

import re
import urllib

def getUrl(url):
	page = urllib.urlopen(url)
	return page.read()

def getImages(html):
	images = re.findall(r'src="(.*?\.(jpg|png))"', html)
	x = 1
	for imageurl in images :
		print('downloading %s'%imageurl[0])
		urllib.urlretrieve(imageurl[0], './images/%d.jpg'%x)
		x += 1

html = getUrl('http://www.tooopen.com/img/87.aspx')
getImages(html)
