#!/usr/bin/python3
#encoding=utf8

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
# print(type(Point))

p = Point(1, 2)

print(p.x)
print(p.y)

p.x = 3
print(p.x)
