import pandas as pd
import numpy as np

arr1 = np.arange(10,20)
# print(arr1,type(arr1))
s1 = pd.Series(arr1)
print(s1)

dic1 = {
    'a':10,
    'b':20,
    'c':30,
    'd':40,
    'e':50
}
s2 = pd.Series(dic1)

arr2 = np.array(np.arange(12).reshape(4,3))
# df1[col][row] 访问具体某个值
df1 = pd.DataFrame(arr2)
dic1 = {
     'a':10,
     'b':20,
     'c':30,
     'd':40,
     'e':50
}
s2 = pd.Series(dic1)

arr2 = np.array(np.arange(12).reshape(4,3))
df1 = pd.DataFrame(arr2)

dic2={'a':[1,2,3,4],'b':[5,6,7,8],'c':[9,10,11,12]}
df3 = pd.DataFrame(dic2)

dic3 = {'one':{'a':1,'b':2,'c':3,'d':4},'two':{'a':5,'b':6,'c':7,'d':8},'there':{'a':9,'b':10,'c':11,'d':12}}
df3 = pd.DataFrame(dic3)

'''
对两个数据快进行操作，只有下标相同的数据才进行操作
'''
s5 = pd.Series(np.array([10,15,20,30,55,80]),index=['a','b','c','d','e','f'])
s6 = pd.Series(np.array([12,13,14,15,16,11]),index=['a','e','g','b','d','k'])



