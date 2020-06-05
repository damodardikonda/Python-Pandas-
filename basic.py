import numpy as np
import pandas as pd
#basic functionalities of series
data=np.random.randn(4)
d=pd.Series(data)
print(d.axes)


s=pd.Series(data)
print("Is the object is empty???")
print(s.empty)
print("dimension of object")
print(s.ndim)

print("size of an object")
print(s.size)

print("actual values are ")
print(s.values)

print("the first 2 row is")
print(s.head(2))

print("the last 2 rw is")
print(s.tail(2))


# basic functionalities of DataFrame

Data={'name':pd.Series(['damodar','tanmay','niket','adesh','aditya']),
       'age':pd.Series([25,45,34,10,26]),
       'roll':pd.Series([20,21,22,23,24])}
df=pd.DataFrame(Data)
print(df)

print("Transpose")
print(df.T)

print("axes is")
print(df.axes)

print(df.dtypes)

print("Is the object is empty???")
print(df.empty)
print("dimension of object")
print(df.ndim)

print("size of an object")
print(s.size)

print("actual values are ")
print(s.values)

print("the first 2 row is")
print(s.head(2))

print("the last 2 rw is")
print(s.tail(2))

print("the shape of object")
print(df.shape)
