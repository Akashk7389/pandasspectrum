import pandas as pd 
# In pytz you can find a list of common (and less common) time zones using from pytz import common_timezones, all_timezones
# dateutil uses the OS timezones so there isn’t a fixed list available. For common zones, the names are the same as pytz
rng=pd.date_range(start="1/1/2017",periods=10,freq='H',tz='Europe/London')
print(rng)

rng=pd.date_range(start="1/1/2017",periods=10,freq='H',tz='dateutil/Europe/London')
print(rng)




rng = pd.date_range(start="2017-08-22 09:00:00",periods=10, freq='30min')
s = pd.Series(range(10),index=rng)

b = s.tz_localize(tz="Europe/Berlin")
print(b)

m = s.tz_localize(tz="Asia/Calcutta")
print(m)

# It will first convert individual timezones to UTC and then align datetimes to perform addition/subtraction etc. operations
print(b + m)
