import numpy as np
import pandas as pd

df=pd.read_csv('cars.csv')
df.head(2)
df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=[np.mean,np.min], margins=True)
print(df)
