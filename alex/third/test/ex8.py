#_*_coding:utf-8_*_
'''
Created on 2016年10月3日

@author: Administrator
'''

'''
print range(10)
print xrange(10)
for i in xrange(10):
    print i
'''

'''
def foo():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
re = foo()
for i in re:
    print i
'''

def wxhReadlines():
    seek = 0
    while True:
        with open('C:\\python-eclipse\\first-day\\read.txt','r') as f:
            f.seek(seek)
            data = f.readline()
            if data:
                seek = f.tell()
                yield data
            else:
                return
for item in wxhReadlines():
    print item
            
         
