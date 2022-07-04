import pandas as pd
df = pd.read_csv("micro.csv", header=1,index_col='Date Time',parse_dates=True)
print(df)
print(df.index)

# # Two types of datetimes in python
# #     Naive (no timezone awareness)
# #     Timezone aware datetime

df=df.tz_localize(tz='US/Eastern')
print(df.index)
df=df.tz_convert(tz='Europe/Berlin')
print(df)

from pytz import all_timezones
print(all_timezones)

df=df.tz_convert(tz='Asia/Calcutta')
print(df)

