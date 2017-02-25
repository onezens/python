#!/usr/bin/python
#encoding=utf8
from wsgiref.simple_server import make_server

def application(environ, start_response):
	start_response('200 OK', [('Content-type', 'text/html')])
	body = '<h1>Hello, %s!' %(environ['PATH_INFO'][1:] or 'web')
	return [body.encode('utf8')]


server_port = 8000

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', server_port, application)
print('Server HTTP on port %s ....'%server_port)
# 开始监听HTTP请求:
httpd.serve_forever()
