import pandas as pd
import numpy as np

N=20

df = pd.DataFrame({
   'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),

   'x': np.linspace(0,stop=N-1,num=N),

   'y': np.random.rand(N),
   'C': np.random.choice(['Low','Medium','High'],N).tolist(),
   'D': np.random.normal(100, 10, size=(N)).tolist()
})


print(df['A'])
print(df['x'])
print(df['y'])
print(df['C'])
print(df['D'])
#reindex the DataFrame
df_reindexed = df.reindex(index=[0,2,5], columns=['A', 'C', 'B'])
print(df_reindexed)


df1=pd.DataFrame(np.random.rand(10,2),columns=['c','c2','c3'])
df2=pd.DataFrame(np.random.rand(10,2),columns=['c','c1','c3'])

df1=df1.reindex_like(df2)
print(df1)
