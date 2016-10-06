#_*_coding:utf-8_*_
'''
Created on 2016年10月6日

@author: wxh
'''

def outer(fun):
    def wrapper():
        print "验证"
        fun()
        print "测试"
    return wrapper

@outer
def Func1():
    print 'func1'
 
@outer   
def Func2():
    print 'func2'

@outer    
def Func3():
    print 'func3'
    
Func1()
Func2()
Func3()
