# -*- coding: utf-8 -*-
"""
Created on Fri May 14 00:57:13 2021

@author: Jeff Song
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("conflict.csv")

df1 = df[['CountryName', 'Year','SumEvents']]


df1 = pd.DataFrame(data = df1)



heatmap1_data = pd.pivot_table(df1, values = 'SumEvents', 
                               index = ['CountryName'],
                               columns = 'Year')

pd.isnull(heatmap1_data).any()

usdf = df1[(df1["CountryName"] == "United States")]

usdf= pd.DataFrame(usdf)
usdf.reset_index(inplace = True)
del usdf['CountryName']
del usdf['index']

print(usdf)





plt.figure(figsize=(8, 12))
heatmap2_data = pd.pivot_table(df1,values='SumEvents', index=['CountryName'], columns='Year')
heatmap2_data.head(n=5)
sns.heatmap(heatmap2_data, cmap="Spectral_r")


# total event for 2021 in different country
yeardf = df[(df["Year"] == 2021)]
yeardf = pd.DataFrame(yeardf)
yeardf = yeardf.dropna()
#print(len(yeardf))



countrycase = yeardf.groupby("CountryName")["TotalEvents"].apply(lambda x: x.mean())
countrycase = pd.DataFrame(countrycase)

countrycase.reset_index(inplace = True)
countrycase = pd.DataFrame(countrycase)

largest = countrycase.nlargest(20, ['TotalEvents'])
largest.reset_index(inplace = True)
largest = pd.DataFrame(largest)
del largest['index']

print(largest)


smallest = countrycase.nsmallest(20, ['TotalEvents'])
smallest.reset_index(inplace = True)
smallest = pd.DataFrame(smallest)
del smallest['index']
print(smallest)
