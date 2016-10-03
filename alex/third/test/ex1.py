#_*_coding:utf-8_*_
'''
Created on 2016年10月2日

@author: wxh
'''
#import sys
#sys.path.append('C:\\python-eclipse\\first-day\\file')

from file import b


print __name__
print __doc__
print __file__

if __name__ == '__main__':
    b.fuu()
else:
    print "走开"