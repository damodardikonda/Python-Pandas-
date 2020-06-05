import pandas as pd
import numpy as np



data=pd.DataFrame(np.random.randn(7,4),
     index=pd.date_range('01/01/2000',periods=7),
     columns=['c1','c2','c3','c4'])

print(data.rolling(window=3).mean())


print("expending")

agg=print(data.expanding(min_periods=3).mean())

print("aggregate on multi colunm")
print(agg[['c1','c3']].aggregate(np.sum))

print('agreegate on multi ple column and function')
print(agg[['c1','c2']].aggregate([np.sum,np.mean]))

print("Apply Different Functions to Different Columns of a Dataframe")
print(agg.aggregate({'c1':np.sum,'c2':np.mean}))
