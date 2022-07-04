import pandas as pd
import numpy as np

# def adder(a,b):
#  return a+b
# #On Series
# s = pd.Series([1,2,3,4,5])
# print(s)
# s = s.pipe(adder,2)
# print(s)
# #On DataFrame
# df = pd.DataFrame([[1,2,3],[2,5,4],[0,9,7],[2,5,6],[8,6,1]],columns=["col1",'col2','col3'])
# print(df)
# df = df.pipe(adder,2)
# print(df)

#apply

# def sqr(a):
#  return a*a
# #On Series
# s = pd.Series([1,2,3,4,5])
# print(s)
# s = s.apply(sqr)
# print(s)

# #On DataFrame
# df = pd.DataFrame([[1,2,3],[2,5,4],[0,9,7],[2,5,6],[8,6,1]],columns=["col1",'col2','col3'])
# print(df)
# df = df.apply(sqr)
# print(df)

# df1 = pd.DataFrame([[1,2,3],[2,5,4],[0,9,7],[2,5,6],[8,6,1]],columns=["col1",'col2','col3'])
# df1 = df1.apply(np.mean)
# print(df1)

# df2 = pd.DataFrame([[1,2,3],[2,5,4],[0,9,7],[2,5,6],[8,6,1]],columns=["col1",'col2','col3'])
# df2 = df2.apply(np.mean,axis=1)
# print(df2)

# df3 = pd.DataFrame([[1,2,3],[2,5,4],[0,9,7],[2,5,6],[8,6,1]],columns=["col1",'col2','col3'])
# df3 = df3.apply(lambda x: x.max() - x.min())
# print(df3)

# #apply map

# df4 = pd.DataFrame([[1,2,3,],[2,5,4],[0,9,7],[2,5,6],[8,6,1]],columns=["col1",'col2','col3'])
# print(df4)
# df4 = df4.applymap(lambda x:x*100)
# print(df4)

# df5 = pd.DataFrame([[1,2,3],[2,5,4],[0,9,7],[2,5,6],[8,6,1]],columns=["col1",'col2','col3'])
# df5['col1']=df5['col1'].map(lambda x:x*100)
# print(df5)

#Concatenation
# one = pd.DataFrame({'Name':['Alex','Amy','Allen','Alice','Ayoung'],'subject_id':['sub1','sub2','sub4','sub6','sub5'],'Marks_scored':[98,90,87,69,78]},index=[1,2,3,4,5])

# two = pd.DataFrame({'Name':['Billy','Brian','Bran','Bryce','Betty'],'subject_id':['sub2','sub4','sub3','sub6','sub5'],'Marks_scored':[89,80,79,97,88]},index=[1,2,3,4,5])

# print(pd.concat([one,two]))

# print(pd.concat([one,two],keys=['x','y']))

# print(pd.concat([one,two],keys=['x','y'],ignore_index=True))

# print(pd.concat([one,two],axis=1))

# print(one.append(two))

# print(one.append([two,one,two]))

#Merging
# left = pd.DataFrame({'id':[1,2,3,4,5],'Name':['Alex','Amy','Allen','Alice','Aypung'],'subject_id':['sub1','sub2','sub4','sub6','sub5']})

# right = pd.DataFrame({'id':[1,2,3,4,5],'Name':['Billy','Brian','Bran','Bryce','Betty'],'subject_id':['sub2','sub4','sub3','sub6','sub5']})

# print(pd.merge(left,right,on='id'))

# print(pd.merge(left,right,on=['id','subject_id']))

# print(pd.merge(left,right,on='subject_id',how='left'))

# print(pd.merge(left,right,on='subject_id',how='right'))

# print(pd.merge(left,right,how='outer',on='subject_id'))

# print(pd.merge(left,right,on='subject_id',how='inner'))

#groupby

ipl_data ={'Team':['Riders','Riders','Devils','Devils','Kings','kings','Kings','Kings','Riders','Royals','Royals','Riders'],'Rank':[1,2,2,3,3,4,1,1,2,4,1,2],'Year':[2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}

df = pd.DataFrame(ipl_data)

print(df)

print(df.groupby('Team'))

print(df.groupby('Team').groups)

print(df.groupby(['Team','Year']).groups)


