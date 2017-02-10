#encoding = utf8

import urllib2

url = 'http://www.baidu.com'

send_headers = {
	'Accept' : '*/*',
	'Accept-Encoding' : 'gzip, deflate, sdch, br',
	'Accept-Language' : 'zh-CN,zh;q=0.8,en;q=0.6',
	'Connection' : 'keep-alive',
	'Host' : 'ss0.bdstatic.com',
	'Referer' : 'https://www.baidu.com/',
	'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

req = urllib2.Request(url, headers = send_headers)
res = urllib2.urlopen(req)

print(res.read())