# -*- coding: utf-8 -*-
"""
Created on Fri Oct 07 13:27:11 2016

@author: Sarick
"""

# -*- coding: utf-8 -*-
import pandas as pd
from dateutil.parser import parse
import os
os.chdir("C:\\Users\\Sarick\\Documents\\Python Scripts\\Document_Clustering")
#%%

import re
r = re.compile(r'%')  
file = "finish.csv"
#def scrubber(file):
df = pd.read_csv(file)
df = df[~df[df.columns[4]].duplicated()]
df.columns = range(len(df.columns))
df.drop([0], axis = 1, inplace = True)
df.columns = range(len(df.columns))
df.drop([0, 1, 7, 11, 12, 13, 14, 15, 17, 20, 24, 25, 32, 33, 40, 41, 48], axis = 1, inplace = True)
#GPT = gross per theater
#TG = total gross

columns=['Release Date','Title','Production Budget','Domestic Gross','Worldwide Gross','Genre','Runtime','MPAA','Critic Rating','Weekend 1 Rank','Weekend 1 Gross','Weekend 1 Theaters','Weekend 1 GPT','Weekend 1 TG', 'Weekend 2 Rank','Weekend 2 Gross','Weekend 2 Change','Weekend 2 Theaters','Weekend 2 GPT','Weekend 2 TG', 'Weekend 3 Rank','Weekend 3 Gross','Weekend 3 Change','Weekend 3 Theaters','Weekend 3 GPT','Weekend 3 TG', 'Weekend 4 Rank','Weekend 4 Gross','Weekend 4 Change','Weekend 4 Theaters','Weekend 4 GPT','Weekend 4 TG']

#df.drop([47, 46, 45, 44, 43, 42, 39, 38, 37 ,36, 35, 34], axis = 1, inplace=True)


df.columns = columns
df.dropna(inplace=True, thresh = 26)    
#df3 = df2[(df2['Weekend 2 Change'].str.contains('%')) | (df2['Weekend 3 Change'].str.contains('%')) | (df2['Weekend 4 Change'].str.contains('%'))]

df = df[(df['Weekend 3 Change'].str.contains('%'))]
df = df[(df['Weekend 2 Change'].str.contains('%'))]
for column in columns:
    try:
        df[column] = df[column].map(lambda x: x.replace(',',''))
        df[column] = df[column].map(lambda x: x.replace('$',''))
        df[column] = df[column].map(lambda x: x.replace('G(Rating', 'G'))
        df[column] = df[column].map(lambda x: x.replace('GG', 'G'))
        df[column] = df[column].map(lambda x: x.replace('n/c', '0'))
    except (AttributeError):
        pass    

df.fillna(0, inplace=True)

df['Weekend 2 Theaters'] = df['Weekend 2 Theaters'].replace(',','').astype(int)
df['Weekend 3 Theaters'] = df['Weekend 3 Theaters'].replace(',','').astype(int)
df.drop(['Weekend 4 Theaters'], axis = 1, inplace = True)
df.drop(['Weekend 4 Rank','Weekend 4 Gross','Weekend 4 Change','Weekend 4 GPT','Weekend 4 TG'], axis = 1, inplace = True)

df['Runtime'] = df['Runtime'].map(lambda x: int(str(x).split()[0]))    
df['MPAA'] = df['MPAA'].map(lambda x: str(x).split()[0])
df['Weekend 1 Rank'] = df['Weekend 1 Rank'].map(lambda x: str(x))
df['Weekend 2 Change'] = df['Weekend 2 Change'].map(lambda x: int(x.replace('%','')))
df['Weekend 3 Change'] = df['Weekend 3 Change'].map(lambda x: int(x.replace('%','')))
df['Release Date'] = df['Release Date'].apply(lambda x: parse(str(x)))
df.to_csv('thenumbers_5000_scrubbed_v2.csv',index=False)
#%%
import re
df = pd.read_csv('thenumbers_5000_scrubbed_v2.csv')
list_of_rating = df['Critic Rating'].tolist()

total_rating = [] 
for rating_string in list_of_rating:
    if rating_string == 'nan' or len(rating_string)==0 or re.findall('\d+%', rating_string)==[]:
        total_rating.append([0,0])
    else:
        list_pair = re.findall('\d+%',rating_string)
        total_rating.append(list_pair)
       
for i in total_rating:
    if len(i)<2:
        a = total_rating.index(i)
        total_rating.remove(i)
        df.drop(a, axis = 0, inplace=True)

        
critic_rate, audience_rate = zip(*total_rating)
df['Critic Rate'] = critic_rate
df['Audience Rate'] = audience_rate
df.to_csv('thenumbers_5000_scrubbed_v3.csv',index=False) 


df['Critic Rate'] = df['Critic Rate'].map(lambda x: int(str(x).replace('%','')))
df['Audience Rate'] = df['Audience Rate'].map(lambda x: int(str(x).replace('%','')))


#%%
#Linear Regression
import seaborn as sns
import numpy as np

#Check Column Types
df.columns.to_series().groupby(df.dtypes).groups
#Finish converting all columns to numeric
df[['Production Budget', 'Domestic Gross', 'Worldwide Gross', 'Weekend 1 Rank','Weekend 1 Gross','Weekend 1 Theaters','Weekend 1 GPT','Weekend 1 TG', 'Weekend 2 Rank','Weekend 2 Gross','Weekend 2 Change','Weekend 2 Theaters','Weekend 2 GPT','Weekend 2 TG', 'Weekend 3 Rank','Weekend 3 Gross','Weekend 3 Change','Weekend 3 Theaters','Weekend 3 GPT','Weekend 3 TG', 'Runtime']]= df[['Production Budget', 'Domestic Gross','Worldwide Gross', 'Weekend 1 Rank','Weekend 1 Gross','Weekend 1 Theaters','Weekend 1 GPT','Weekend 1 TG', 'Weekend 2 Rank','Weekend 2 Gross','Weekend 2 Change','Weekend 2 Theaters','Weekend 2 GPT','Weekend 2 TG', 'Weekend 3 Rank','Weekend 3 Gross','Weekend 3 Change','Weekend 3 Theaters','Weekend 3 GPT','Weekend 3 TG', 'Runtime']].apply(pd.to_numeric, errors='coerce')


df3 = df[['Production Budget', 'Domestic Gross','Worldwide Gross', 'Weekend 1 Rank','Weekend 1 Gross','Weekend 1 Theaters','Weekend 1 GPT','Weekend 1 TG', 'Weekend 2 Rank','Weekend 2 Gross','Weekend 2 Change','Weekend 2 Theaters','Weekend 2 GPT','Weekend 2 TG', 'Weekend 3 Rank','Weekend 3 Gross','Weekend 3 Change','Weekend 3 Theaters','Weekend 3 GPT','Weekend 3 TG', 'Runtime', 'Critic Rate', 'Audience Rate']].replace(0 , df[['Production Budget', 'Domestic Gross','Worldwide Gross', 'Weekend 1 Rank','Weekend 1 Gross','Weekend 1 Theaters','Weekend 1 GPT','Weekend 1 TG', 'Weekend 2 Rank','Weekend 2 Gross','Weekend 2 Change','Weekend 2 Theaters','Weekend 2 GPT','Weekend 2 TG', 'Weekend 3 Rank','Weekend 3 Gross','Weekend 3 Change','Weekend 3 Theaters','Weekend 3 GPT','Weekend 3 TG', 'Runtime', 'Critic Rate', 'Audience Rate']].mean(), inplace = True)


#Do thie call below for every variable to fill the dataframe up
df['Audience Rate'].replace(0, df['Audience Rate'].mean(), inplace = True)
df4 = df.dropna()
df4.to_csv("movies_5000_zeros_filledv5")
#%%
# -*- coding: utf-8 -*-

def adj_r2_score(model,y,ypred):
	adj = 1 - float(len(y)-1)/(len(y)-len(model.coef_)-1)*(1 - metrics.r2_score(y,ypred))
	return adj

df = pd.read_csv('movies_5000_zeros_filled.csv')
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
from sklearn.model_selection import train_test_split
df4.drop(['Critic Rating'], axis = 1, inplace = True)
df4['MPAA'] = df4['MPAA'].astype(str)

translator = {'M/PG':'PG-13','R(Rated':'R','GG(Rating':'G','Open':'G','G(Rating':'G','Not':'PG-13'}
df4['MPAA']=df4['MPAA'].replace(translator)

df4.to_csv('movies_5000_zeros_filledv6')

df_dummies = pd.get_dummies(df4['Genre'], drop_first=True) 
df_dummies = pd.concat([df_dummies, pd.get_dummies(df4['MPAA'], drop_first=True)], axis=1)
df_regression = df4[['Production Budget', 'Weekend 2 Change', 'Weekend 3 Change', 'Weekend 1 Theaters', 'Weekend 2 Theaters', 'Weekend 3 Theaters', 'Weekend 1 GPT', 'Weekend 2 GPT', 'Weekend 3 GPT', 'Critic Rate', 'Audience Rate']]
df_regression = pd.concat([df_regression, df_dummies], axis =1, join_axes=[df_regression.index])


#Coefficient Plot


plt.plot(range(3), [0.494189, 0.512570,0.591596])
plt.xticks(range(3), ['Weekend 1', 'Weekend 2', 'Weekend 3'])
plt.ylabel("Correlation Coefficient")



#Plot of R2
width = .35
plt.bar(range(4), [0.55459218078608719, 0.64049897239556585, .675,0.856], width)
plt.xticks(range(4), [ 'Elastic Net+WW','Elastic Net+Domestic','RF + WW', 'RF+Domestic'])
plt.ylabel("R2 Score")

width = .35
plt.bar(range(4), [0.55459218078608719,0.79389354806433121,  0.71255505295054022,  0.77758631466092465], width, position = 'center')
plt.xticks(range(4), [ 'G','PG','PG-13', 'R'])
plt.ylabel("R2 Score")



X,y = df_regression,df4['Domestic Gross']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
from sklearn.linear_model import LinearRegression
model = LinearRegression().fit(X_train, y_train)
y_pred = model.predict(X_test)
metrics.r2_score(y_test, y_pred)
metrics.mean_squared_error(y_test, y_pred)
model.coef_
model.residuals_


         

# build a classifier
clf = RandomForestRegressor(n_estimators = 100, max_depth = 7, max_features = 11)
clf.fit(X_train, y_train)
clf.feature_importances_


import matplotlib.pyplot as plt 
import seaborn as sns

plt.barh(range(11), clf.feature_importances_)
plt.yticks(range(11),['Production Budget', 'Weekend 2 Change', 'Weekend 3 Change', 'Weekend 1 Theaters', 'Weekend 2 Theaters', 'Weekend 3 Theaters', 'Weekend 1 GPT', 'Weekend 2 GPT', 'Weekend 3 GPT', 'Critic Rate', 'Audience Rate'])
plt.xlabel('Importances')
plt.ylabel('Features')

plt.scatter(df4['Weekend 3 Theaters'], df4['Worldwide Gross'])
plt.xlabel('Weekend 3 Theaters')
plt.ylabel('Worldwide Gross')

plt.scatter(df4['Weekend 2 Theaters'], df4['Worldwide Gross'])
plt.xlabel('Weekend 2 Theaters')
plt.ylabel('Worldwide Gross')


plt.scatter(df4['Weekend 1 Theaters'], df4['Worldwide Gross'])
plt.xlabel('Weekend 1 Theaters')
plt.ylabel('Worldwide Gross')

from scipy.stats import randint as sp_randint
# specify parameters and distributions to sample from
param_dist = {"max_depth": sp_randint(1, 10),
              "max_features": sp_randint(1, 10)}  

clf = RandomForestRegressor(n_estimators=100)
n_iter_search = 20
random_search = RandomizedSearchCV(clf, param_distributions=param_dist, n_iter=n_iter_search, cv = 5)
random_search.fit(X_train, y_train)
y_pred2=random_search.predict(X_test)
metrics.r2_score(y_test, y_pred2)
metrics.mean_squared_error(y_test, y_pred2)
import matplotlib.pyplot as plt
plt.scatter(y_pred2, y_test)

#Append df_dummies_genre to each and then regress
df_dummies_genre = pd.get_dummies(df4['Genre'], drop_first=True) 
df_R = df4[df4['MPAA']=='R']
df_R= df_R[['Production Budget','Worldwide Gross', 'Weekend 2 Change', 'Weekend 3 Change', 'Weekend 1 Theaters', 'Weekend 2 Theaters', 'Weekend 3 Theaters', 'Weekend 1 GPT', 'Weekend 2 GPT', 'Weekend 3 GPT', 'Critic Rate', 'Audience Rate']]
df_R = pd.concat([df_R, df_dummies_genre], axis =1, join_axes=[df_R.index])

X,y = df_R.drop('Worldwide Gross', axis = 1),df_R['Worldwide Gross']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
param_dist = {"max_depth": sp_randint(1, 10),
              "max_features": sp_randint(1, 10)}  

clf = RandomForestRegressor(n_estimators=100)
n_iter_search = 20
random_search = RandomizedSearchCV(clf, param_distributions=param_dist, n_iter=n_iter_search, cv = 5)
random_search.fit(X_train, y_train)
y_pred2=random_search.predict(X_test)
metrics.r2_score(y_test, y_pred2)
metrics.mean_squared_error(y_test, y_pred2)
import matplotlib.pyplot as plt
plt.scatter(y_pred2, y_test)
plt.xlabel('Predicted')
plt.ylabel('Observed')




df_PG13 = df4[df4['MPAA']=='PG-13']
df_PG13= df_PG13[['Production Budget','Worldwide Gross', 'Weekend 2 Change', 'Weekend 3 Change', 'Weekend 1 Theaters', 'Weekend 2 Theaters', 'Weekend 3 Theaters', 'Weekend 1 GPT', 'Weekend 2 GPT', 'Weekend 3 GPT', 'Critic Rate', 'Audience Rate']]
df_PG13 = pd.concat([df_PG13, df_dummies_genre], axis =1, join_axes=[df_PG13.index])

X,y = df_PG13.drop('Worldwide Gross', axis = 1),df_PG13['Worldwide Gross']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
param_dist = {"max_depth": sp_randint(1, 10),
              "max_features": sp_randint(1, 10)}  

clf = RandomForestRegressor(n_estimators=100)
n_iter_search = 20
random_search = RandomizedSearchCV(clf, param_distributions=param_dist, n_iter=n_iter_search, cv = 5)
random_search.fit(X_train, y_train)
y_pred2=random_search.predict(X_test)
metrics.r2_score(y_test, y_pred2)
metrics.mean_squared_error(y_test, y_pred2)
import matplotlib.pyplot as plt
plt.scatter(y_pred2, y_test)
plt.xlabel('Predicted')
plt.ylabel('Observed')



df_PG = df4[df4['MPAA']=='PG']
df_PG= df_PG[['Production Budget','Worldwide Gross', 'Weekend 2 Change', 'Weekend 3 Change', 'Weekend 1 Theaters', 'Weekend 2 Theaters', 'Weekend 3 Theaters', 'Weekend 1 GPT', 'Weekend 2 GPT', 'Weekend 3 GPT', 'Critic Rate', 'Audience Rate']]
df_PG = pd.concat([df_PG, df_dummies_genre], axis =1, join_axes=[df_PG.index])

X,y = df_PG.drop('Worldwide Gross', axis = 1),df_PG['Worldwide Gross']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
param_dist = {"max_depth": sp_randint(1, 10),
              "max_features": sp_randint(1, 10)}  

clf = RandomForestRegressor(n_estimators=100)
n_iter_search = 20
random_search = RandomizedSearchCV(clf, param_distributions=param_dist, n_iter=n_iter_search, cv = 5)
random_search.fit(X_train, y_train)
y_pred2=random_search.predict(X_test)
metrics.r2_score(y_test, y_pred2)
metrics.mean_squared_error(y_test, y_pred2)
import matplotlib.pyplot as plt
plt.scatter(y_pred2, y_test)
plt.xlabel('Predicted')
plt.ylabel('Observed')

df_G = df4[df4['MPAA']=='G']
df_G= df_G[['Production Budget','Worldwide Gross', 'Weekend 2 Change', 'Weekend 3 Change', 'Weekend 1 Theaters', 'Weekend 2 Theaters', 'Weekend 3 Theaters', 'Weekend 1 GPT', 'Weekend 2 GPT', 'Weekend 3 GPT', 'Critic Rate', 'Audience Rate']]
df_G = pd.concat([df_G, df_dummies_genre], axis =1, join_axes=[df_G.index])

X,y = df_G.drop('Worldwide Gross', axis = 1),df_G['Worldwide Gross']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
param_dist = {"max_depth": sp_randint(1, 10),
              "max_features": sp_randint(1, 10)}  

clf = RandomForestRegressor(n_estimators=100)
n_iter_search = 20
random_search = RandomizedSearchCV(clf, param_distributions=param_dist, n_iter=n_iter_search, cv = 5)
random_search.fit(X_train, y_train)
y_pred2=random_search.predict(X_test)
metrics.r2_score(y_test, y_pred2)
metrics.mean_squared_error(y_test, y_pred2)
import matplotlib.pyplot as plt
plt.scatter(y_pred2, y_test)
plt.xlabel('Predicted')
plt.ylabel('Observed')
#%%
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
metrics.r2_score(y_test, y_pred)



df_regression = df4[['Production Budget', 'Weekend 3 Theaters', 'Weekend 1 GPT', 'Weekend 2 GPT', 'Weekend 3 GPT']]
df_regression = pd.concat([df_regression, df_dummies], axis =1, join_axes=[df_regression.index])
X,y = df_regression,df4['Worldwide Gross']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
metrics.r2_score(y_test, y_pred)








