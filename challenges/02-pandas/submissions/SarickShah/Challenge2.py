# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 17:31:57 2016

@author: Sarick
"""
#%%
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from dateutil import parser
import numpy as np
os.chdir("C:\\Users\\Sarick\\Documents\\Python Scripts")
#%%
df = pd.read_csv('2013_movies(1).csv')
df.sort_values('ReleaseDate', inplace = True)
y = df['DomesticTotalGross']
X = df['ReleaseDate']

plt.figure(figsize=(20,10))
plt.xticks(range(100), X, rotation = 90)
plt.bar(range(100), y, color="#b3ccff", align = "center")
#%%
df.sort_values('Runtime', inplace = True)
plt.figure(figsize=(20,10))
plt.xticks(range(100), df['Runtime'], rotation = 90)
plt.bar(range(100), y, color="#b3ccff", align = "center")
#%%
df_ratings_DTG = df.groupby(['Rating'])['DomesticTotalGross'].sum()
df_ratings_RT = df.groupby(['Rating'])['Runtime'].mean()
df_rating = pd.concat([df_ratings_DTG, df_ratings_RT], axis=1, join_axes=[df_ratings_DTG.index]) 
#%%
dfG = df[df['Rating']=="G"]
dfPG=df[df['Rating']=="PG"]
dfPG13=df[df['Rating']=="PG-13"]
dfR=df[df['Rating']=="R"]
#%%
dt_converter = lambda x: parser.parse(x)
df['ReleaseDate'] = df['ReleaseDate'].map(dt_converter)
f, axarr = plt.subplots(2, 2, sharex = True)
axarr[0, 0].scatter(np.array(dfG['ReleaseDate']), dfG['DomesticTotalGross'])
axarr[0, 1].scatter(np.array(dfPG['ReleaseDate']), dfPG['DomesticTotalGross'])
axarr[1, 0].scatter(np.array(dfPG13['ReleaseDate']), dfPG13['DomesticTotalGross'])
axarr[1, 1].scatter(np.array(dfR['ReleaseDate']), dfR['DomesticTotalGross'])
plt.tight_layout()
#%%
df2 = df.groupby(['Director'])['DomesticTotalGross'].sum()
df3 = df.groupby('Director')['Title'].count()
df4 = df2/df3
df4.idxmax()
#'Francis Lawrence'
#%%
df['month'] = pd.DatetimeIndex(df['ReleaseDate']).month
mdtg = df.groupby(['month'])['DomesticTotalGross'].sum()
mdtg_std = df.groupby(['month'])['DomesticTotalGross'].std()
plt.errorbar(range(12), mdtg, mdtg_std)
plt.bar(range(12), mdtg)

import seaborn as sns
sns.barplot(x = "month", y ='DomesticTotalGross', data = df)
#%%