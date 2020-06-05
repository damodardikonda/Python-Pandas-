import pandas as pd
import numpy as np

df=pd.read_csv("files.csv",index_col=['Name'])
print(df)


print('\n\n changingthe type of float, ')
df1=pd.read_csv("files.csv",dtype={'Salary':np.float})
print(df1.dtypes)

print("df headers")
df2=pd.read_csv("files.csv",names=['A','B','C','D','E'],skiprows=2)
print(df2)
