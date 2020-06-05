import pandas as pd
import numpy as np

df=pd.read_csv('census.csv')
print(df)

print(df.where(df['SUMLEV']==50)
.dropna()
.set_index(['STNAME','CTYNAME'])
    .rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'}))

print("or you can use where as like below")

df=df[df['SUMLEV']==50]
print(df.set_index(['STNAME','CTYNAME']))
print(df.rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'}))



def min_max(row):
    data=row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2010']]


    return pd.Series({'min':np.min(data),'max':np.max(data)})

df.apply(min_max, axis=1)
