import numpy as np

#series:-1D,homogeneous,sizeimmutable,values mutable
#dataframe:-2D,size-mutabel,heterogeneous colomn value mutable
#panel:-3D,size-mutable,value mutable

#panel is container of dataframe and dataframe is series

#series can be created by using array,dict and constatnt

#reating an empty series
import pandas as pd

print("panda import properly")
s=pd.Series();
print("checking working or not")
print(s)

#creating a series using ndarray
data=np.array([1,2,3,4,5])
series=pd.Series(data,dtype=float)
print(series)

#creating series withindex  and ndarray

arr=np.array(['a','s','d','f','g'])
ser=pd.Series(arr,index=([67,35,79,43,24]))#remember index  size should be same as array and unique
print(ser)


#create series with dict

#if we didnt provide any index then it takes

dic={'a':1,'f':2,'c':36,'d':4}
s=pd.Series(dic)
print(s)

#with index
d={1:100,2:200,3:30000}
se=pd.Series(d,index=[1,3,2])#if value of key is different from index then it prints index. if value mises print NaN
print(se)

#using scalar or fix value
x=pd.Series(5,index=[65,5,34,78,90]);print(x)


#Retrieve Data Using Label (Index)
print(x[65])
print(x[[5,34,78]])
