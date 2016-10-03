#_*_coding:utf-8_*_
'''
Created on 2016年10月3日

@author: wxh
'''
def login(username):
    if username == 'wxh':
        return '登陆成功'
    else:
        return "登陆失败"

def detail(user):
    print 'name = wxh age = 25'
    
if __name__ == '__main__':
    user = raw_input("请输入用户名: ")
    res = login(user)
    if res == "登陆成功":
        detail(user)
    else:
        print "登陆失败,请重新输入"
    
    