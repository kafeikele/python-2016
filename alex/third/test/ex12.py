#_*_coding:utf-8_*_
'''
Created on 2016年10月5日

@author: wxh
'''
import random
#from random import randint
print random.random()
print random.randint(1,6)
print random.randrange(1,10)

#随机生成一个大写字母 
a = chr(random.randint(65,91))
print a

#随机生成六位数，包括大写字母和数字
'''
for i in range(6):
    if i == random.randint(1,5):
        print random.randint(1,5)
    else:
        temp = random.randint(65,91)
        print chr(temp)
'''        
code = []
for i in range(6):
    if i == random.randint(1,3):
        code.append(str(random.randint(1,5)))
    else:
        temp = random.randint(65,90)
        code.append(chr(temp))
print ''.join(code)


#随机生成六位数，包括大写字母和数字
import random
checkcode = ''
for i in range(6):
    current = random.randrange(0,6)
    if current != i:
        temp = chr(random.randint(65,90))
    else:
        temp = random.randint(0,9)
    checkcode += str(temp)
print checkcode