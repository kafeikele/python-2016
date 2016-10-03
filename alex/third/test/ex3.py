#_*_coding:utf-8_*_
'''
Created on 2016年10月3日

@author: wxh
'''
#import sys
#sys.path.append('C:\\python-eclipse\\second-day\\')

import file.a 
#file和ex3的上级目录平行

print __name__
print __doc__
print __file__

if __name__ == '__main__':
    file.a.foo()
else:
    print "走开"