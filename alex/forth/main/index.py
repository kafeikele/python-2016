#_*_coding:utf-8_*_
'''
Created on 2016年10月6日

@author: wxh
'''

str1 = 'demo'
str2 = 'Foo'

module = __import__(str1)
func = getattr(module, str2)

func()