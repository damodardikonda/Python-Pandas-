import pandas as pd
import numpy as np

ipl_team={
'Team':['indians','indians','riders','devils','riders','kings','indians','kings','devils','riders','kings','devils'],
'ranks':[1,4,2,5,6,8,3,9,7,12,45,37],
'year':[2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
'points':[876,789,863,673,741,812,756,788,694,701,804,690]
}

data=pd.DataFrame(ipl_team)

print(data)

print("split data into group")
print(data.groupby(['Team','year']).groups)#op-devils,indians


print("iterating through")
itr=data.groupby('Team')

for ranks,year in itr:
    print(ranks,year)


print("geetting group by get group ")
grp=data.groupby('year')
print(grp.get_group(2014))


print("groupby year and do mean of points")
m=data.groupby('year')
print(m['points'].agg(np.mean))
print("size of all through year")
print(m.agg(np.size))

print("multiplr function")
print(m['points'].agg([np.mean,np.sum,np.std]))

print('filter')
print(data.groupby('Team').filter(lambda x: len(x)>=3))
