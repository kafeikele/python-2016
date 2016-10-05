#_*_coding:utf-8_*_
'''
Created on 2016年10月4日

@author: wxh
'''
from IPython.utils._process_common import arg_split
print chr(65)
print chr(90)
print chr(97)
print chr(122)
print ord('a')
print hex(20)
print bin(2)
print oct(2)


print sum([1,3])
print max([1,3])
print divmod(9,4)
print bool(-1)
print abs(-9)
print pow(2,10)

print all([1,2,3.4])
print all([0,1,2,3])
print any([0,0,0,0])
print any([0,1,2,3])

li = ['手表','汽车','房']
for item in li:
    print item
    
for item in enumerate(li,1):
    print item[0],item[1]
    
s = 'I am {0},{1}'
print s.format("wxh",'25')



