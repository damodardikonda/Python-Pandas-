import numpy as np
import pandas as pd

left=pd.DataFrame({
'name':['damodar','tanmay','adesh','adi','niket'],
'id':[1,2,3,4,6],
'roll':[10,20,30,40,70]
})

right=pd.DataFrame({
'name':['niket','vaibhav','dev','aditya','rutya'],
'id':[1,2,3,4,5],
'sub':['ds','analytic','ml','dl','nlp']
})

print(left)
print(right)
print("\n\n\n")
print(pd.merge(left,right,on='id'))
print('\n multiplr values\n')
print(pd.merge(left,right,on=['id','name']))

print('left join')
print(pd.merge(left,right,on='id',how='left'))

print('right join')
print(pd.merge(left,right,on='id',how='right'))

print('outer join')
print(pd.merge(left,right,on='id',how='outer'))
