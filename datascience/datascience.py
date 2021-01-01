import numpy as np
import   pandas as pd
from  numpy.random import *
labels=['a','b','c','d']
my_data= [10,20,30,40]
arr=np.array(my_data)
d={'a':10,'b':20,'c':30}
# print(pd.Series(my_data))
# print(pd.Series(my_data,labels))
# print(pd.Series(my_data,labels))
# print(pd.Series(arr,labels))
# print(pd.Series(d))
series1=pd.Series([1,2,3,4],['India','Germany','japan','china'])
print(series1)
print(series1['Germany'])
# # print(Series1[''])
# # pd.read_csv('annual.csv')
# # data framesgit commit -m
#
df=pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)
print(df[['W','Z']])
#
df['new']=df['W']+  df['Z']
print(df)
# # df.drop('new',axis=1)
# # print(df)
# data=pd.read_csv('annual.csv')
# print(data)
# print(data.shape)
# print(data.info())