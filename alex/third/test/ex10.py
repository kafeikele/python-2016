#_*_coding:utf-8_*_
'''
Created on 2016年10月4日

@author: wxh
'''
def foo(x,y):
    return x + y
print foo(4,10)

for i in range(10):
    print i*2
    
print [x*2 for x in range(10)]

#lambda
print map(lambda x:x*2, range(10))

a = lambda x,y:x+y
print a(4,10)

