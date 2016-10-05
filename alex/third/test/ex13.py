#_*_coding:utf-8_*_
'''
Created on 2016年10月5日

@author: wxh
'''
import md5
hash = md5.new()
hash.update('admin')
print hash.hexdigest()
 
 
import hashlib
hash = hashlib.md5()
hash.update('admin')
print hash.hexdigest()
print hash.digest()