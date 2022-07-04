import pandas as pd 
df=pd.read_csv("HistoricalData_apple_nodates.csv")
print(df.head())

df["Close"]=df["Close"].str.replace('$','')
df["Close"]=df["Close"].astype(float)

rng = pd.date_range(start="11/01/2021",end="11/28/2021",freq='B') #B for Business
print(rng)
df.set_index(rng, inplace=True) #inplace=True for modifying the original dataframe
print(df)

# daily_index = pd.date_range(start="6/1/2016",end="6/30/2016",freq='D') #D for Daily

from matplotlib import pyplot as plt
df.Close.plot()
plt.show()

#mean of Closing Price for first 10 days
print(df["2021-11-01":"2021-11-10"].Close.mean())

#To include the weekends
df.asfreq('D',method='pad')
print(df)
df=df.asfreq('H',method='pad')
print(df)

#Situation where we know the start date and just the periods
rng = pd.date_range(start="11/01/2021",periods=72,freq='B')
print(rng)

#Can be used to create random sample data
import numpy as np
ts = pd.Series(np.random.randint(0,10,len(rng)), index=rng)
print(ts.head(20)) 

#Date range cannot handle holidays but only weekends.




