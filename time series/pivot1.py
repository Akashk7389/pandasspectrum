#pivot allows to transform or reshape the dataframe

import pandas as pd
import numpy as np
df = pd.read_csv("weather.csv")
# print(df)


# df=df.pivot(index='city',columns='date')
# print(df)

# # df=df.pivot(index='city',columns='date',values="humidity")
# # print(df)

# df.pivot(index='date',columns='city')

# df.pivot(index='humidity',columns='city')


# Pivot Table
#used to summarize and aggregate data inside dataframe

df = pd.read_csv("weather2.csv")
# print(df)

# df=df.pivot_table(index="city",columns="date")
# print(df)
# # Margins

df=df.pivot_table(index="city",columns="date", margins=True,aggfunc=np.sum)
print(df)

# # Grouper

# df = pd.read_csv("weather3.csv")
# df['date'] = pd.to_datetime(df['date'])

# df = df.pivot_table(index=pd.Grouper(freq='M',key='date'),columns='city')
# print(df)
