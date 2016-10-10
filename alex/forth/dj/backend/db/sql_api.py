#coding:utf-8
'''
Created on 2016年10月10日

@author: wxh
'''
from dj.config import settings 

def db_auth(configures):
    if configures.DATABASE["user"] =="root" and configures.DATABASE["password"]==123:
        print "db login success"
    else:
        print "db login error"

def select(table,column):
    db_auth(settings)
    if table == "user":
        user_info = {
            "001":['wxh',22,'enginge'],
            "002":['whh',23,'enginger'],
            "003":['wdh',24,'engingerr']
        }
        return user_info