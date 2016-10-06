#_*_coding:utf-8_*_
'''
Created on 2016年10月6日

@author: wxh
'''

def outer(fun):
    def wrapper(arg):
        print "验证"
        fun(arg)
        print "测试"
    return wrapper

@outer
def Func1(arg):
    print 'func1',arg
    
Func1('wxh')