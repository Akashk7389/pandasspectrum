import pandas as pd
df = pd.read_csv("walmart.csv")
# print(df)

df.set_index('Line Item',inplace=True)
df=df.T
print(df)
df.index = pd.PeriodIndex(df.index, freq="Q-JAN")
print(df.index)
df['start_Date']=df.index.map(lambda x:x.start_time)
df['end_Date']=df.index.map(lambda x:x.end_time)

print(df)