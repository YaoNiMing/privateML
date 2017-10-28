# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 19:09:24 2016

@author: Sarick
"""

import os
os.chdir("C:\Users\Sarick\Documents\Python Scripts")
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import seaborn as sns
#%%
df=pd.read_csv('house-votes-84.csv', header = None)
df = df.replace(['y', 'n', '?'], [1, 0, np.NaN])
df.fillna(df.mean(), inplace = True)
#%%
X = df.drop(0, axis = 1)
y = df[0]
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=.2)
#%%
def knn_predict(test):
    score=[]
    for i in range(1,20):
        knn = KNeighborsClassifier(n_neighbors = i)
        knn.fit(X_train, y_train)
        y_pred = knn.predict(test)
        score.append(accuracy_score(y_test, y_pred))
    return score
#%%
score = knn_predict(X_test)
score.index(max(score))+1
plt.plot(range(1,20),score)
#%%
model = LogisticRegression().fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy_score(y_test, y_pred)
#%%
party_df = df[0].value_counts()
plt.bar(range(2), party_df, align = 'center')
plt.xticks(range(2),['Democrat', 'Republican'])
#%%
def demlist(x):
    dem = ['democrat'] * x
    return dem

def replist(x):
    rep = ['republican'] * x
    return rep
#%%
dem = demlist(87)
rep = replist(87)

#%%
dem_score=[]
rep_score=[]
for i in range(19):
    dem_score.append(accuracy_score(y_test, dem))
    rep_score.append(accuracy_score(y_test, rep))

plt.plot(range(19), score)
plt.plot(range(19), dem_score)
plt.plot(range(19), rep_score)
#%%
from sklearn.learning_curve import learning_curve
train_sizes, train_scores, valid_scores = learning_curve(LogisticRegression(), X, y, cv=5)
error_train = np.mean(train_scores, axis=1)
error_test = np.mean(valid_scores, axis=1)

plt.plot(train_sizes, error_train)
plt.plot(train_sizes, error_test)
#%%
knn = KNeighborsClassifier(n_neighbors = 10)
train_sizes, train_scores, valid_scores = learning_curve(knn, X, y, cv=5)
error_train = np.mean(train_scores, axis=1)
error_test = np.mean(valid_scores, axis=1)
plt.plot(train_sizes, error_train)
plt.plot(train_sizes, error_test)
#%%
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB().fit(X_train, y_train)
y_pred = gnb.predict(X_test)
accuracy_score(y_test, y_pred)
#%%
from sklearn.svm import SVC
svc= SVC().fit(X_train, y_train)
y_pred = svc.predict(X_test)
accuracy_score(y_test, y_pred)
#%%
from sklearn.tree import DecisionTreeClassifier
dtc= DecisionTreeClassifier().fit(X_train, y_train)
y_pred = dtc.predict(X_test)
accuracy_score(y_test, y_pred)
#%%
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier().fit(X_train, y_train)
y_pred = rfc.predict(X_test)
accuracy_score(y_test, y_pred)
#%%
from sklearn.cross_validation import cross_val_score
np.mean(cross_val_score(gnb, X, y, cv = 5))
np.mean(cross_val_score(svc, X, y, cv = 5))
np.mean(cross_val_score(dtc, X, y, cv = 5))
np.mean(cross_val_score(rfc, X, y, cv = 5))
#%%
df = pd.read_csv('house-votes-84.csv', header = None)
df.drop(0, axis=1, inplace =True)
df = df.replace(['y', 'n', '?'], [1, 0, np.NaN])
for i in range(1,17):
    df[i].fillna(df[i].mode()[0], inplace=True)
X, y = df.drop(1, axis = 1), df[1]
model = LogisticRegression()
np.mean(cross_val_score(model, X, y, cv = 5))
#%%
df=pd.read_csv('movies.csv')
df_counts = df['Rating'].value_counts()
plt.bar(range(4), df_counts, align='center')
plt.xticks(range(4), ['PG13', 'R', 'PG', 'G'])
#%%
from sklearn.preprocessing import MinMaxScaler
df.fillna(df.mean(), inplace = True)
df.dropna(inplace=True)
X = df[['Budget', 'DomesticTotalGross', 'Runtime']]
y = df['Rating']
X = MinMaxScaler().fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=.25)
score = max(knn_predict(X_test))
#%%
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred=model.predict(X_test)
accuracy_score(y_test, y_pred)
#%%
pg13 = ['PG-13']*24
accuracy_score(pg13, y_pred)
model.coef_
#%%
columns = ['Age', 'Year', 'Nodes', 'Survival']
df=pd.read_csv('haberman.data', names=columns)
df.Age.describe()
#%%
df_greater = df[df['Survival'] == 1]
df_greater.Age.describe()
df_less = df[df['Survival'] == 2]
df_less.Age.describe()
#%%
plt.hist(df['Age'])
plt.hist(df['Nodes'])
#%%
min(df['Year'])
max(df['Year'])
#%%
X = df.drop(['Survival'], axis = 1)
y = df['Survival']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)
model=LogisticRegression().fit(X_train, y_train)
y_pred=model.predict(X_test)
accuracy_score(y_test, y_pred)
model.coef_
train_sizes, train_scores, valid_scores = learning_curve(model, X, y, cv=5)
train_score = np.mean(train_scores, axis=1)
valid_score = np.mean(valid_scores, axis=1)
plt.plot(train_sizes, train_score)
plt.plot(train_sizes, valid_score)
#%%