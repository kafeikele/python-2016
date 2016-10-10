#coding:utf-8
'''
Created on 2016年10月10日

@author: wxh
'''

from dj.backend.db.sql_api import select
def home():
    print "welcome to home page"
    data = select('user','ddd')
    print ("query res:",data)
def movies():
    print "welcome to movies page"
    
def tv():
    print "welcome to tv page"
    

