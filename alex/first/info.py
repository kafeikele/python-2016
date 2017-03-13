#!/usr/bin/env python
#_*_coding:utf-8 _*_
name = raw_input('Please input your name:')
age = input("age:")
job = raw_input("job:")
salary = raw_input("salary:")

if age > 40 :
	msg = 'You are too fucking old!'
elif age > 30 :
	msg = 'You are still have a few years to hook up'
else :
	msg = 'You are still young'
	
print '''
Personal information of %s:
	Name:   %s
	Age :   %d
	Job :   %s
	Salary: %s
---------------------
%s
''' % ( name,name,age,job,salary,msg)

test