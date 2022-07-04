import pandas as pd
df = pd.read_excel("survey.xls")
print(df)
# result=pd.crosstab(df.Nationality,df.Handedness)
# result=pd.crosstab(df.Sex,df.Handedness)
# print(result)
# 
# # margins
# result=pd.crosstab(df.Sex,df.Handedness, margins=True)
# print(result)

# # Multi Index Column and Rows
# result=pd.crosstab(df.Sex, [df.Handedness,df.Nationality])
# print(result)

# result=pd.crosstab([df.Nationality, df.Sex], [df.Handedness], margins=True)
# print(result)


# # Normalize for getting the percentage value
# result=pd.crosstab(df.Sex, df.Handedness, normalize='index')
# print(result)

# # Aggfunc and Values

# import numpy as np
# result=pd.crosstab(df.Sex, df.Handedness, values=df.Age, aggfunc=np.average)
# print(result)
