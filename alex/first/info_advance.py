#!/usr/bin/env python
#_*_coding:utf-8 _*_
name = raw_input('Please input your name:')
job = raw_input("job:")
salary = raw_input("salary:")
real_age = 29
for i in range(10) :	
	age = input('age:')
	if age > 29 :
		print 'big!'
	elif age == 29 :
		print '\033[32;1mright!\033[0m'
		break
	else :
		print 'small'

	print 'You still got %s shots!' % (9 - i)

	
print '''
Personal information of %s:
	Name:   %s
	Age :   %d
	Job :   %s
	Salary: %s
---------------------
''' % (name,name,age,job,salary)
