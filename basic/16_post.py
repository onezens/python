#encoding=utf8

import urllib

params = urllib.urlencode({'spam':1, 'eggs':2, 'bacon': 0})

print(params)

f = urllib.urlopen('http://python.org/query', params)

print(f.read())