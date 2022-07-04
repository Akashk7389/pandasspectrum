# import pandas as pd 
# df=pd.read_csv("HistoricalData_apple.csv")
# print(df.head())

# #DatetimeIndex

# print(type(df.Date[0])) # string
#-------------------------------------------------------------------------#

# import pandas as pd 
# df=pd.read_csv("HistoricalData_apple.csv",parse_dates=["Date"])
# print(df.head())

# print(type(df.Date[0])) #date type
# #-------------------------------------------------------------------------#

# import pandas as pd 
# df=pd.read_csv("HistoricalData_apple.csv",parse_dates=["Date"],index_col='Date')
# print(df.head())
# #Index is now Date column

# print(df.index)
# #Retreive stock prices of 2021
# print(df['2021'])

# #Retreive stock prices of November,2021
# print(df["2021-11"])


# #Retreive stock price of 24th,November,2021
# print(df["2021-11-24"])

# # #Average price of Apple's stock in November,2021
# df["Close"]=df["Close"].str.replace('$','')
# print(df)

# df["Close"]=df["Close"].astype(float)

# print(df["2021-11"].Close.mean())

# #Date Range -- [end date : start date]
# print(df['2021-12-01':'2021-11-14'])

# #Resampling

# #Retrive monthly stock price
# # Resampling on Monthly basis
# # W : weekly frequency
# # M : month end frequency
# # SM : semi-month end frequency (15th and end of month)
# # Q : quarter end frequency

# print(df.Close.resample('M').mean())

# #Plot
# import matplotlib.pyplot as plt

# # df['Close'].plot()
# # plt.show()

# # df.Close.resample('W').mean().plot()
# # plt.show()

# df['Close'].resample('W').mean().plot(kind='bar')
# plt.show()

# #-------------------------------------------------------------------------#



















