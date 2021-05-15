#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 7 20:18:52 2021

@author: Group 11
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("CrimeData.csv")
print(df.shape)
print(df.columns)
print(df.dtypes)

Countries = df.groupby("CountryCode")["CountryName"].apply(lambda x: x.values)
Crimes = df.groupby("EventRootCode")["EventRootDescr"].apply(lambda x: x.values)
#print(Crimes)



#Has crime increased/ decreased in the past 4 decades? Is the trend different in different parts of the world?
g = df.groupby("EventRootDescr").size().to_frame(name='count')
g = g.sort_values(by='count', ascending=0).head(6)
print("Here is the list of types of crimes by total number of instances")
print (g)

while True:
    Country = input("Enter Name of Country: ") 
    crime = input("Enter Crime Type: ")    
    
    if crime == "EXIT":
        break
    
    if Country != "ALL":
        a = df[(df.CountryName == Country)]
    
    if crime != "ALL":
        a = df[(df.EventRootDescr == crime)]
        
    xaxis = []
    data = []
    
    for Years in range(7):
        sYears = Years * 6 + 1979
        eYears = sYears + 6
        f = a[(a.Year >= sYears) & (a.Year < eYears)]
        
        xaxis.append(str(sYears) + " - " + str(eYears))
        data.append(sum(f.SumEvents))
     
    plt.plot(xaxis, data)
    plt.xticks(xaxis, rotation='vertical')
    plt.title("Crime Frequency Report for " + crime + " in " + Country)
    plt.show()
 



#With time, which kind of crime activities show an uptrend or downtrend?
crimeType = input("Which kind crime would you like to check for trend? ").upper()
country = input("Please specify the country: ")

if country != "All":
    sumOfYears = df[(df["EventRootDescr"] == crimeType) & (df["CountryName"] == country)] \
        .groupby("Year").sum().reset_index()
else:
    sumOfYears = df[df["EventRootDescr"] == crimeType].groupby("Year").sum().reset_index()

crimeTrend = sumOfYears.SumEvents
print(crimeTrend)

#To print the crime trend in the country in a line chart
x, y = [], []
for year in range(min(df.Year), max(df.Year) + 1):
    x.append(year)
    y.append(sumOfYears[sumOfYears.Year == year].SumEvents)

titleSentence= "Crime " + crimeType + " Trend in " + country + " from 1979 to 2021"
plt.title(titleSentence)

plt.plot(x, y)
plt.xticks(np.arange(min(df.Year), max(df.Year), 4))
plt.show()  

#To print the crime ration of all kinds of crimes ratio trend in the country in a bar chart
sumOfYears["Ratio"] = sumOfYears.SumEvents / sumOfYears.TotalEvents * 100

titleSentence= "Crime " + crimeType + " Percentage of All Kinds of Crimes Trend in " + country + " from 1979 to 2021"
plt.title(titleSentence)

sumOfYears.Ratio.plot.bar()



#Which crime category is the most common in a given period of time? Does the ratio change with time?
ff = df[(df.CountryCode == "US")]
ff = ff.groupby(ff.EventRootDescr).sum()["SumEvents"]

print(ff)

global1 = df[(df.Year <= 2020) & (df.Year > 2000)]
global1 = global1.groupby(global1.EventRootDescr).sum()["SumEvents"]

chart1 = global1.plot.pie(x='EventRootDescr', y='Total Events', title = "Types of Crime 2000-2020", rot=0, autopct='%1.1f%%')

global2 = df[(df.Year <= 2000) & (df.Year > 1980)]
global2 = global2.groupby(global2.EventRootDescr).sum()["SumEvents"]

chart2 = global2.plot.pie(x='EventRootDescr', y='Total Events', title = "Types of Crime 1980-2000", rot=0, autopct='%1.1f%%')



#Have mass shootings become more common in the U.S. in the past 20 years?
sf = df[(df["EventCode"] == 202) & (df["CountryCode"] == "US") & (df["Year"] >= 2000)]
cf = sf.groupby(["Year"]).sum().reset_index()
cff = cf.SumEvents
#print(cf)
print(cff)

plt.plot(cff)
plt.title("Mass Shooting in US over last 20 years")
plt.xlabel("Last 20 years")
plt.ylabel("Sum of Mass Shootings per year")
plt.show()

















