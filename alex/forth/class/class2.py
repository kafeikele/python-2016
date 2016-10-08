#coding:utf-8
'''
Created on 2016��10��9��

@author: wxh
'''
class province:
    
    memo = '中国有23个省'
    
    def __init__(self,name,capital,leader):
        self.Name = name
        self.Capital = capital
        self.Leader = leader
ah = province('ah','hf','whh')
print ah.Name +' '+ ah.Capital
xj = province('xj','wlmq','mln')
print xj.Leader  
print province.memo
print ah.memo