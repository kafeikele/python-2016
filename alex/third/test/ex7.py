#_*_coding:utf-8_*_
'''
Created on 2016年10月3日

@author: wxh
'''
#把参数封装成列表
def show1(*arg):
    for item in arg:
        print item
        
show1("wxh","whh","wdh","wwh") 


def show2(**kargs):
    for i in kargs.items():
        print i
show2(name="wxh",age="25")
    
    
    