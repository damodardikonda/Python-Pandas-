import pandas as pd

data=pd.DataFrame([{'name':'damodar','item_purchest':'IOt','cost':10000},
                    {'name':'adesh','item_purchest':"Dripper", 'cost':80},
                    {'name':'Aditya','item_purchest':'App','cost':5000}],

                    index=['store1','store2','store3'])

print(data)
print('\n\n Adding Date')
data['Date']=['january1','december10','aprill8']
print(data)

print('\n\n delivered\n\n')
data['delivered']=True
print(data)

print('\n\n feedback\n\n')
data['feedback']=['Positive',None,'Negetive']
print(data)

adf=data.reset_index()
adf['Date']=pd.Series({0:'December 2',2:'mid may'})
print(adf)

("staff data")

staff=pd.DataFrame([{'name':'koshti','roll':'History'},
                    {'name':'shashi','roll':'java'},
                    {'name':'badshah','roll':'survuve'}])
staff=staff.set_index('name')
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                           {'Name': 'Mike', 'School': 'Law'},
                           {'Name': 'Sally', 'School': 'Engineering'}])
student_df = student_df.set_index('Name')

print(staff)
print()
print(student_df)
print("merginnnnnnnnnnnnnnnnnnnnnggggggggggggggggg")

staff = staff.reset_index()
student_df = student_df.reset_index()
pd.merge(staff,student_df,how='left',left_on='name',right_on='Name' )


print()
print()
print(staff.head())
print()
print(student_df.head())
print("merging outer")
pd.merge(staff, student_df, how='outer', left_index=True, right_index=True)
print("inner")
pd.merge(staff, student_df, how='inner', left_index=True, right_index=True)
print("left")
pd.merge(staff, student_df, how='left', left_index=True, right_index=True)
print("right")
pd.merge(staff, student_df, how='left', left_index=True, right_index=True)
print("reset index")
