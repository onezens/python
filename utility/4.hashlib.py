#!/usr/bin/python
#encoding=utf8

import hashlib

oriStr = 'Hello , This is test string'

# MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，
# 通常用一个32位的16进制字符串表示。
md5 = hashlib.md5()
md5.update(oriStr.encode('utf8'))
md5Str = md5.hexdigest()
print(md5Str)
print(type(md5))

###################
# SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。
# 比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长。
sha1 = hashlib.sha1()
sha1.update(oriStr.encode('utf8'))
sha1.update('hello'.encode('utf8'))
print(sha1.hexdigest())