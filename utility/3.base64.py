#!/usr/bin/python
#encoding=utf8
import base64
oriStr = 'Hello world'
print(oriStr)
testStr = base64.b64encode(oriStr)
print(testStr)
decodeStr = base64.b64decode(testStr)
print(decodeStr)

# 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，
# 所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：

oriStr = b'i\xb7\x1d\xfb\xef\xff'
print(oriStr)
print(base64.b64encode(oriStr))
testStr = base64.urlsafe_b64encode(oriStr)
print(testStr)
print(base64.urlsafe_b64decode(testStr))

# Base64是一种通过查表的编码方法，不能用于加密，即使使用自定义的编码表也不行。
# Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等。
# 由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉：
# 需要加上=把Base64字符串的长度变为4的倍数，就可以正常解码了。
# Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。