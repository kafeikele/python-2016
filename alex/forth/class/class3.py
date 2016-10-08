#coding:utf-8
'''
Created on 2016年10月9日

@author: wxh
'''
class province:
    #静态字段
    memo = '中国有23个省'
    
    def __init__(self,name,capital,leader):
        #动态字段
        self.Name = name
        self.Capital = capital
        self.Leader = leader
        
    #动态方法    
    def sports_meet(self):
        print self.Name + '正在开运动会'
    #静态方法
    @staticmethod     
    def Foo():
        print '每个省要带头反腐'
        
  
ah = province('ah','hf','whh')
xj = province('xj','wlmq','mln')

ah.sports_meet()
xj.sports_meet()

province.Foo()