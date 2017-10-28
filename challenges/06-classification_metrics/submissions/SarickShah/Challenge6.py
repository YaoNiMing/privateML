# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 14:07:57 2016

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
from sklearn.metrics import classification_report
from sklearn.metrics import precision_recall_curve, roc_curve

#%%
df=pd.read_csv('house-votes-84.csv', header = None)
df = df.replace(['y', 'n', '?'], [1, 0, np.NaN])
df.fillna(df.mean(), inplace = True)
#%%
X = df.drop(0, axis = 1)
y = df[0]
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=.2)
#%%
knn = KNeighborsClassifier(n_neighbors = 10)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print classification_report(y_test, y_pred)
#%%
model = LogisticRegression().fit(X_train, y_train)
y_pred = model.predict(X_test)
print classification_report(y_test, y_pred)
#%%
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB().fit(X_train, y_train)
y_pred = gnb.predict(X_test)
print classification_report(y_test, y_pred)
#%%
from sklearn.svm import SVC
svc= SVC(probability=True).fit(X_train, y_train)
y_pred = svc.predict(X_test)
accuracy_score(y_test, y_pred)
#%%
from sklearn.tree import DecisionTreeClassifier
dtc= DecisionTreeClassifier().fit(X_train, y_train)
y_pred = dtc.predict(X_test)
print classification_report(y_test, y_pred)
#%%
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier().fit(X_train, y_train)
y_pred = rfc.predict(X_test)
print classification_report(y_test, y_pred)
#%%
list1 = [knn, model, gnb, svc, dtc, rfc]
for i in list1:
    precision, recall, threshold = precision_recall_curve(y_test, i.predict_proba(X_test)[:,0], pos_label = 'democrat')
    plt.plot(precision, recall)

for i in list1:
    fpr, tpr, thresholds  = roc_curve(y_test, i.predict_proba(X_test)[:,0], pos_label = 'democrat')
    plt.plot(fpr, tpr)
#%%
from sklearn.metrics import auc
auc(fpr, tpr)
#%%
columns = ['Age', 'Year', 'Nodes', 'Survival']
df=pd.read_csv('haberman.data', names=columns)
X = df.drop(['Survival'], axis = 1)
y = df['Survival']
X_train, X_test, y_train, y_test = train_test_split(X, y)
model = LogisticRegression().fit(X_train, y_train)

precision, recall, threshold = precision_recall_curve(y_test, model.predict_proba(X_test)[:,0], pos_label = 1)
plt.plot(precision, recall)
fpr, tpr, threshold2 = roc_curve(y_test, model.predict_proba(X_test)[:,0], pos_label = 1)
plt.plot(fpr, tpr)