import numpy as np
import pandas as pd




df=pd.DataFrame(np.random.rand(4,3),columns=['c1','c2','c3'])
print(df)

for k,v in df.iteritems():
    print(k,v)


print("\n\nthrough row \n\n")

for row,row_index in df.iterrows():
    print(row,row_index)

print("\n\n giving tuple asa value. first it print an index\n\n")
for r in df.itertuples():
    print(r)

#Note − Do not try to modify any object while iterating. Iterating is meant for reading and the
# iterator returns a copy of the original object (a view), thus the changes will not reflect on the original object.

for i in df.iterrows();
   i['a']=30
   print(i)#it wont changes
