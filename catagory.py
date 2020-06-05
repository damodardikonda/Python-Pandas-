import pandas as pd

l=pd.Series([2,3,4,5,2,3,4], dtype="category")
print(l)


cata=pd.Categorical(['a','b','c','d','a','a','b','c'])
print(cata)


data=pd.Categorical(['a','b','c','d','a','a','b','c'],['a','b'],ordered=True)
print(data)

print(data.ordered)

l.cat.categories=["group %s" %g for g in l.cat.categories]
print(l.cat.categories)
print("appending in categories")
l=l.cat.add_categories([5])
print(l)

print("remove categories")
l=l.cat.remove_categories('group 2')
print(l)


cat1=pd.Series([1,3,5]).astype('category',categories=[1,2,3],ordered=True)
cat3 = pd.Series([2,2,2]).astype("category", categories=[1,2,3], ordered=True)
print(ca1>cat2)
