#_*_coding:utf-8_*_
'''
Created on 2016年10月6日

@author: Administrator
'''
import pickle
a = ['wxh',22,60,'wdh']
dumpsed = pickle.dumps(a)
print dumpsed

loadsed = pickle.loads(dumpsed)
print loadsed 

'''
#import pickle
data = {'k1':123,'k2':'hello'}

p_str = pickle.dumps(data)
print p_str

with open('D:/result.pk','w') as fp:
    pickle.dump(data,fp)
    
import json
j_str = json.dumps(data)
print j_str

with open('D:/result.json','w') as fp:
    pickle.dump(data,fp)
'''