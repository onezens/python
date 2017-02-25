#!/usr/bin/python
#encoding=utf8
#SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
# 注意到构造MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype，
# 传入'plain'表示纯文本，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

#输入Email地址和口令
from_addr = 'zhenwang0246@163.com'
password = '123456'
#收件人地址
to_addr = 'dev@onezen.cc'
#输入SMTP地址
smtp_server = 'smtp.163.com'

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
#smtp 协议默认端口是25
# server = smtplib.SMTP(smtp_server, 25)
#######加密
smtp_port = 25
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()

####
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()