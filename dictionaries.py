d={'food':'chicken','name':'damodar','valuess':10}
print(d['food'])

#creating dictionary
dict={}
dict['name']='damodar'
dict['values']=10
dict['food']='chicken'

print(dict)

#nested dictionary

dict1={'name':{'first':'damodar','last':'dikonda'},
       'age':20,'job':['data scientist','student']}
print(dict1['name']['last'])
print(dict1['job'][-1])
dict1['job'].append('analysis')
print(dict1)


#grap key into list
li=list(dict1.keys())
print(li)
li.sort()
print(li)

#for key in li:
#    print(key,dict[key])

#insted of these 3 step use function

for i in sorted(d):
   print(i,':-',d[i])

#for loop

for a in 'spammmm':
    print(a.upper())

x=4
while x>0:
    print('spam'*x)
    x=x-1
