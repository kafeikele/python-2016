#!/usr/bin/env python
#_*_coding:utf-8 _*_
name = raw_input('Please input your name:')
age = raw_input("age:")
job = raw_input("job:")
salary = raw_input("salary:")

if age > 30:
	msg="You are too fucking old!"
else:
	msg="you are still young"
print '''
Personal information of %s:
        Name:   %s
        Age :   %s
        Job :   %s
        Salary: %s
---------------------
%s
''' % ( name,name,age,job,salary,msg)

