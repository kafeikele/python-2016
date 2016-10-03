#_*_coding:utf-8_*_
'''
Created on 2016年10月3日

@author: wxh
'''
def foo(name):
    print name,"去做饭"

def fpp(name,action):
    print name,"去",action
    
def fqq(name,action='吃饭',where="shanghai"):
    print name,"去",action,where
 
foo('wxh')
fpp('mln','洗碗')
fqq('xtz',where="beijing")


