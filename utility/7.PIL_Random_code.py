#!/usr/bin/python
#encoding=utf8
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

def ranChar():
	return chr(random.randint(64, 90))

def ranBgColor():
	return (random.randint(64, 255), random.randint(64,255), random.randint(64,255))


def ranForeColor():
	return (random.randint(32,127), random.randint(32,127), random.randint(32,127))

height = 60
width = height*4
image = Image.new('RGB', (width, height), (255, 255, 255))

#创建font
font = ImageFont.truetype('Arial.ttf', 36)
#创建draw对象
draw = ImageDraw.Draw(image)
#填充每个像素
for x in range(width):
	for y in range(height):
		draw.point((x, y), fill=ranBgColor())

#输出文字
for t in range(4):
	draw.text((60 * t + 10, 10), ranChar(), font=font, fill=ranForeColor())

#模糊
image.save('code_ori.jpg', 'jpeg')
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')