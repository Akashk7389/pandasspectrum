import pandas as pd
dates = ['2017-01-05', 'Jan 5, 2017', '01/05/2017', '2017.01.05', '2017/01/05','20170105']
print(pd.to_datetime(dates))

dt = ['2017-01-05 2:30:00 PM', 'Jan 5, 2017 14:30:00', '01/05/2016', '2017.01.05', '2017/01/05','20170105']
print(pd.to_datetime(dt))

# European style dates with day first 
#5th, January
print(pd.to_datetime('5-1-2016'))
print(pd.to_datetime('5-1-2016', dayfirst=True))


# Custom date time format

print(pd.to_datetime('2017$01$05', format='%Y$%m$%d'))
print(pd.to_datetime('2017#01#05', format='%Y#%m#%d'))


# Handling invalid dates

print(pd.to_datetime(['2017-01-05', 'Jan 6, 2017', 'abc'], errors='ignore'))
print(pd.to_datetime(['2017-01-05', 'Jan 6, 2017', 'abc'], errors='coerce'))


# Epoch
# Epoch or Unix time means number of seconds that have passed since Jan 1, 1970 00:00:00 UTC time

current_epoch = 1638984138
print(pd.to_datetime(current_epoch, unit='s')) # to seconds

print(pd.to_datetime(current_epoch*1000, unit='ms')) # to milli seconds

t = pd.to_datetime([current_epoch], unit='s')