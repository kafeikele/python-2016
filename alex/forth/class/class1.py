#coding:utf-8
'''
Created on 2016��10��8��

@author: wxh
'''
   
class Person:
    def __init__(self,name,age):
        self.Name = name
        self.Age = age
        
p1 = Person('liyang',18)
print p1.Name + str(p1.Age)
p2 = Person('laoge',26)
print p2.Name


class province:
    def __init__(self,name,capital,leader):
        self.Name = name
        self.Capital = capital
        self.Leader = leader
ah = province('ah','hf','whh')
print ah.Name +' '+ ah.Capital
xj = province('xj','wlmq','mln')
print xj.Leader




