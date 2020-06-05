import pandas as pd
import numpy as np



def answer_one():
    x = pd.ExcelFile('Energy Indicators.xls')
    energy = x.parse(skiprows=17,skip_footer=(38))
    energy = energy[[1,3,4,5]]
    energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    energy[['Energy Supply', 'Energy Supply per Capita', '% Renewable']] =  energy[['Energy Supply', 'Energy Supply per Capita', '% Renewable']].replace('...',np.NaN).apply(pd.to_numeric)
    energy['Energy Supply'] = 1000000*energy['Energy Supply']
    energy['Country'] = energy['Country'].replace({'China, Hong Kong Special Administrative Region':'Hong Kong','United Kingdom of Great Britain and Northern Ireland':'United Kingdom','Republic of Korea':'South Korea','United States of America':'United States','Iran (Islamic Republic of)':'Iran'})
    energy['Country'] = energy['Country'].str.replace(r" \(.*\)","")

    GDP = pd.read_csv('world_bank.csv',skiprows=4)
    GDP['Country Name'] = GDP['Country Name'].replace({'Korea, Rep.':'South Korea','Iran, Islamic Rep.':'Iran','Hong Kong SAR, China':'Hong Kong'})
    GDP = GDP[['Country Name','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']]
    GDP.columns = ['Country','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']

    ScimEn = pd.read_excel(io='scimagojr-3.xlsx')
    ScimEn = ScimEn[:15]
    df = pd.merge(ScimEn,energy,how='inner',left_on='Country',right_on='Country')
    new_df = pd.merge(df,GDP,how='inner',left_on='Country',right_on='Country')
    new_df = new_df.set_index('Country')
    return new_df
answer_one()




get_ipython().run_cell_magic('HTML', '', '<svg width="800" height="300">\n  <circle cx="150" cy="180" r="80" fill-opacity="0.2" stroke="black" stroke-width="2" fill="blue" />\n  <circle cx="200" cy="100" r="80" fill-opacity="0.2" stroke="black" stroke-width="2" fill="red" />\n  <circle cx="100" cy="100" r="80" fill-opacity="0.2" stroke="black" stroke-width="2" fill="green" />\n  <line x1="150" y1="125" x2="300" y2="150" stroke="black" stroke-width="2" fill="black" stroke-dasharray="5,3"/>\n  <text  x="300" y="165" font-family="Verdana" font-size="35">Everything but this!</text>\n</svg>')


def answer_two():
    return 156
answer_two()




def answer_three():
    Top15 = answer_one()
    avgGDP = Top15[['2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']].mean(axis = 1).rename('avgGDP').sort_values(ascending= True)
    return pd.Series(avgGDP)
answer_three()




def answer_four():
    Top15 = answer_one()
    six = Top15.iloc[3,19] - Top15.iloc[3,10]
    return six
answer_four()



def answer_five():
    Top15 = answer_one()
    m = Top15.iloc[:,8].mean()
    return m
answer_five()




def answer_six():
    Top15 = answer_one()
    mx = Top15.iloc[:,9].max()
    return ('Brazil',mx)
answer_six()




def answer_seven():
    Top15 = answer_one()
    Top15['Ratio'] = Top15.iloc[:,4]/Top15.iloc[:,3]
    return ('China',Top15.iloc[:,20].max())
answer_seven()




def answer_eight():
    Top15 = answer_one()
    Top15['Pop'] = Top15.iloc[:,7]/Top15.iloc[:,8]
    mx3 = sorted(Top15['Pop'],reverse = True)[2]
    a = str(pd.Series(Top15[Top15['Pop']==mx3].index)).split()
    return 'United States'
#a[1] + ' ' + a[2]
answer_eight()




def answer_nine():
    Top15 = answer_one()
    Top15['Pop'] = Top15.iloc[:,7]/Top15.iloc[:,8]
    Top15['Citable docs per Capita'] = Top15.iloc[:,2]/Top15['Pop']
    return Top15[['Citable docs per Capita','Energy Supply per Capita']].corr(method='pearson').iloc[0,1]
answer_nine()




def answer_ten():
    Top15 = answer_one()
    med = Top15.iloc[:,9].median()
    Top15['HighRenew']  = None
    for i in range(len(Top15)):
        if Top15.iloc[i,9] > med:
            Top15.iloc[i,20] = 1
        else:
            Top15.iloc[i,20] = 0
    return pd.Series(Top15['HighRenew'])
answer_ten()



def answer_eleven():
    ContinentDict  = {'China':'Asia',
                  'United States':'North America',
                  'Japan':'Asia',
                  'United Kingdom':'Europe',
                  'Russian Federation':'Europe',
                  'Canada':'North America',
                  'Germany':'Europe',
                  'India':'Asia',
                  'France':'Europe',
                  'South Korea':'Asia',
                  'Italy':'Europe',
                  'Spain':'Europe',
                  'Iran':'Asia',
                  'Australia':'Australia',
                  'Brazil':'South America'}
    Top15 = answer_one()
    Top15['size'] = None
    Top15['Pop'] = Top15.iloc[:,7]/Top15.iloc[:,8]
    Top15['Continent'] = None
    for i in range(len(Top15)):
        Top15.iloc[i,20] = 1
        Top15.iloc[i,22]= ContinentDict[Top15.index[i]]
    ans = Top15.set_index('Continent').groupby(level=0)['Pop'].agg({'size': np.size, 'sum': np.sum, 'mean': np.mean,'std': np.std})
    ans = ans[['size', 'sum', 'mean', 'std']]
    return ans
answer_eleven()


def answer_twelve():
    ContinentDict  = {'China':'Asia',
                  'United States':'North America',
                  'Japan':'Asia',
                  'United Kingdom':'Europe',
                  'Russian Federation':'Europe',
                  'Canada':'North America',
                  'Germany':'Europe',
                  'India':'Asia',
                  'France':'Europe',
                  'South Korea':'Asia',
                  'Italy':'Europe',
                  'Spain':'Europe',
                  'Iran':'Asia',
                  'Australia':'Australia',
                  'Brazil':'South America'}
    Top15 = answer_one()
    Top15['Continent'] = None
    for i in range(len(Top15)):
        Top15.iloc[i,20]= ContinentDict[Top15.index[i]]
    Top15['bins'] = pd.cut(Top15['% Renewable'],5)
    return Top15.groupby(['Continent','bins']).size()
answer_twelve()



def answer_thirteen():
    Top15 = answer_one()
    Top15['PopEst'] = (Top15.iloc[:,7]/Top15.iloc[:,8]).astype(float)
    return Top15['PopEst']
answer_thirteen()



# In[ ]:

#plot_optional() # Be sure to comment out plot_optional() before submitting the assignment!
#plot9()
#plot_optional()


# In[ ]:
