import pandas as pd 
# y=pd.Period('2016')
# print(y) #Annual ending in december
# print(dir(y))
# print(y.start_time)
# print(y.end_time)
# print(y.is_leap_year)

# m=pd.Period('2017-12')
# print(m)
# print(m.start_time)
# print(m.end_time)
# m=m+1
# print(m)

# d=pd.Period("2017-02-28")
# print(d)
# d=d+1
# print(d)

# d2=pd.Period("2016-02-28")
# print(d2)
# d2=d2+1
# print(d2)


# Hourly Period
# h = pd.Period('2017-08-15 23:00:00',freq='H')
# print(h)
# print(h.start_time)
# print(h.end_time)

# h=h+1

# print(h)

# h=h+pd.offsets.Hour(6)
# print(h)


# # Quarterly Period - 3 months 
# q1= pd.Period('2017Q1')
# print(q1)
# q1=q1+1

# print(q1)

# #different fiscal year -- start:Feb end:Jan

# q2= pd.Period('2017Q1', freq='Q-JAN')#ending in january
# print(q2.start_time)
# print(q2.end_time)

# # q1.asfreq('M',how='start') #monthly freq using start time
# # print(q1)

# qt1=pd.Period('2017Q1',freq='Q-JAN')
# qt2=pd.Period('2018Q2',freq='Q-JAN')

# print(qt2-qt1)

# w = pd.Period('2017-07-05',freq='W-SAT')
# print(w)

idx = pd.period_range('2011', '2017', freq='q')
print(idx)
idx = pd.period_range('2011', '2017', freq='q-JAN')
print(idx)

# print(idx[0].start_time)