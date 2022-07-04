# import pandas as pd
# df=pd.read_excel("survey.xls")
# # print(df)

# #result=pd.crosstab(df.Nationality,df.Handedness)

# #result=pd.crosstab(df.Sex,df.Handedness,margins=True)


# #multi index column and rows

# #result=pd.crosstab(df.Sex,[df.Handedness,df.Nationality],margins=True)

# #normlize index
# # result=pd.crosstab(df.Sex,df.Handedness,normalize="index")

# #Afffunc and values
# import numpy as np
# result=pd.crosstab(df.Sex,df.Handedness,values=df.Age,aggfunc=np.average)

# print(result)

import numpy as np
import pandas as pd
df=pd.read_csv("weather2.csv")
# print(df)

df=df.pivot_table(index="city",columns="date",margins=True,aggfunc=np.sum)
# result=df.pivot(index="city",columns="date",values="humidity")
print(df)