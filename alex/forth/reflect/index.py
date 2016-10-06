#_*_coding:utf-8_*_
'''
Created on 2016年10月6日

@author: wxh
'''
'''
from backend import account
#account.login()
data = raw_input("请输入地址: ")
if data == 'account/login':
    account.login()
elif data == 'account/logout':
    account.logout()

'''

data = raw_input('请输入网址: ')
array = data.split('/')

userspance = __import__('backend.'+array[0])
model =getattr(userspance, array[0])
func = getattr(model,array[1])
func()


