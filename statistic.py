import pandas as pd
import numpy as np

data={
'name':pd.Series(['damodar','ram','ra','shy','dd','sk','rk','rs']),
'age':pd.Series([20,34,24,56,34,67,43,32]),
'gender':pd.Series(['M','M','M','F','F','M','F','M'])
}

d=pd.DataFrame(data)
print("sum is")
print(d.sum())
print("only age")
print(d.sum(1))

print("for average value[mean()]")
print(d.mean())

print("Returns the Bressel standard deviation of the numerical columns.")
print(d.std())

print("count,mean,min,max,std")
print(d.describe())

print('summerised string object')
print(d.describe(include=['object']))

print("summerised Numeric object bydefault")
print(d.describe(include=['number']))

print("summerised all object")
print(d.describe(include='all'))
