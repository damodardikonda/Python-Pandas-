import numpy as np
import pandas as pd

data=pd.DataFrame(np.random.rand(4,5),index=['a','c','d','g'], columns=['c','c2','c3','c4','c5'])

data=data.reindex(['a','b','c','d','e','f','g','h','i'])

print(data)

print("null then true")
print(data['c'].isnull())


print('nul then false')
print(data['c2'].notnull())

print("addition of vlue")
print(data['c2'].sum())


print('fillna fill NAN value to 0')

print(data.fillna(0))


print('pad/fill:--- fill method forword,,,if b is empty then it replace with a value')
print(data.fillna(method='pad'))


print('bfill/backfill:--- fill method backword,,,if b is empty then it replace with c value')
print(data.fillna(method='backfill'))

print("for dropping null value,axis =1 then it drop whole row which has null value")
print(data.dropna())

print('it also has replace value')
