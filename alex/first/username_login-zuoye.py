#!/usr/bin/env python
#_*_coding: utf-8 _*_
import sys
retry_limit = 3
retry_count = 0
account_file = 'account.txt'
lock_file = 'account_lock.txt'
while retry_count < retry_limit:  #只要重试不超过三次就不断循环
  username = raw_input('\033[32;1mUsername:\033[0m')
  lock_check = file(lock_file) #file:打开文件，当用户输入用户名后，打开Lock文件以检查是否此用户已经lock
  for line in lock_check.readlines(): #循环lock文件
    line = line.split()
    if username == line[0]:
      sys.exit('033[31;1mUser %s is locked!\033[0m' % username)
      #如果locked就直接退出
  password = raw_input('\033[32;1mPassword;\033[0m')
  f = file(account_file,'rb')#打開帳號文件
  match_flag = False  #默認為false,如果用戶match上了，就設置為true
  for line in f.readlines():
    user,password = line.strip('\n').split()
    #去掉每行多余的\n并把这一行按空格分成两列，分别赋值为user,password两个变量
    if username == user and password == password:
      print 'Match!',username
      match_flag = True
      #相等就把循环外的match_flag变量改为True
      break   #然后就不用继续循环了，直接跳出，因为已经match
  f.close()
  if match_flag == False:
    #如果match_flag还为false，代表上面的循环中根本就没有match上用户名和密码，所以还需要继续循环
    print 'User unmatched!'
    retry_count +=1
  else:
    print "Welcome Login system"
else:
  print 'your account is locked!'
  f = file(lcok_file,'ab')
  f.write(username)
  f.close()  
    
  
