import pandas as pd
import numpy as np

unsort=pd.DataFrame(np.random.randn(6,3),index=[1,4,2,7,5,3] , columns=['c3','c1','c2'])
print(unsort)

print('by label,by index')

sort=unsort.sort_index( ascending='True',axis=1)#axis help to do soring by columns
print(sort)


unsorted_df = pd.DataFrame({'col1':[2,1,1,1],'col2':[1,3,2,4]})
sorted_df = unsorted_df.sort_values(by='col1',kind='mergesort')

print(sorted_df)


unsort_df = pd.DataFrame({'col1':[2,1,1,1],'col2':[1,3,2,4]})
sort_df = unsort_df.sort_values(by='col1')

print(sort_df)
