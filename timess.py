import pandas as pd

print("current time")
print(pd.datetime.now())


print("create a timestamp")
print(pd.Timestamp(2017-10-23,unit='s'))


print("converting a Timestamp")
print(pd.to_datetime(pd.Series(['3 apr 2000','21-8-1999',None])))

print('cretae timedelta from string')
print(pd.Timedelta('5 days 2 hours 20 min 20 sec'))

print('by using integer')
print(pd.Timedelta(8,unit='s'))


print(pd.Timedelta(milliseconds=52))
