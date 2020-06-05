import pandas as pd
data=pd.DataFrame()
print(data)


#creating dataframe ffrom list
list=[10,20,30,4,5]
lists=pd.DataFrame(list)
print(lists)

#multiple lists
mulist=(['damodar',10],['aditya',20],['tanmay',676],['adesh',24])
multi=pd.DataFrame(mulist,columns=['name','roll'],dtype=float)
print(multi)


#create a dict from list/np.array
dict={'Name':['damodar','aditya','adesh','tanmay'],'roll':[12,65,34,98]}
di=pd.DataFrame(dict,dtype=int,index=['r1','r2','r4','r3'])
print(di)


#Create a DataFrame from List of Dicts

l=[{'a':1,'b':1},{'c':3,'d':4}]
s=pd.DataFrame(l,index=[40,50])
print(s)

#create adatafrem from dict of Series

dic={'one':pd.Series([1,2,3,4], index=['a','b','c','d']),
'two':pd.Series([4,5,6],index=['e','f','g'] )}
d=pd.DataFrame(dic)
print(d)



d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)

# Adding a new column to an existing DataFrame object with column label by passing new series

print ("Adding a new column by passing as Series:")
df['three']=pd.Series([10,20,30,40], index=['a','b','c','d'])
print(df)

print ("Adding a new column using the existing columns in DataFrame:")
df['four']=df['one']+df['three']

print(df)
print('want to del')
df['five']=pd.Series([87,89,54,34],index=['a','b','c','d'])
print(df)
del(df['five'])

print(df)
