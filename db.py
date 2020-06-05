import pandas as pd

reads=df.read_csv('url.csv')

print(df[['total_bill','tip','sex','smoker','day','time','size']]).head(5)

print([reads[reads['sex']=='Male']]).head(5)


print("head is nothing but top rows")
print(reads.groupby('sex')).head(5)
