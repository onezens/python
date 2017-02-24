#!/usr/bin/python
#encoding=utf8

from PIL import Image, ImageFilter

#打开一个jpg图片
im = Image.open('cat.jpg')
#获取大小
w,h=im.size
print('Original image to: %sx%s'%(w,h))
#缩放到50%
im.thumbnail((w*0.5, h*0.5))
print('Resize image to: %s x %s'%(w*0.5,h*0.5))
im.save('cat_thumbnail.jpg', 'jpeg')

#模糊
imBlur = im.filter(ImageFilter.BLUR)
imBlur.save('cat_blur.jpg', 'jpeg')

