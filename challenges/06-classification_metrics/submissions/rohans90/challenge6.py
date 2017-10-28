# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 21:18:43 2016

@author: Rohan
"""


import pandas as pd
import seaborn as sns
import numpy as np

df = pd.read_csv('house-votes-84.data.csv')

df.head()



for i in df.columns:
   print df[i].value_counts()
   
for i in df.columns:
    df[i] = df[i].replace('y','1')
    df[i] = df[i].replace('n','0')
   

dl = df.columns[1:]

for i in dl:
    print df[i].value_counts()
  
df.iloc[:,1] = df.iloc[:,1].replace('?', '0.429')
df.iloc[:,2] = df.iloc[:,2].replace('?', '0.448')
df.iloc[:,3] = df.iloc[:,3].replace('?', '0.581')
df.iloc[:,4] = df.iloc[:,4].replace('?', '0.406')  
df.iloc[:,5] = df.iloc[:,5].replace('?', '0.487')
df.iloc[:,6] = df.iloc[:,6].replace('?', '0.625')
df.iloc[:,7] = df.iloc[:,7].replace('?', '0.549')
df.iloc[:,8] = df.iloc[:,8].replace('?', '0.556')    
df.iloc[:,9] = df.iloc[:,9].replace('?', '0.475')  
df.iloc[:,10] = df.iloc[:,10].replace('?', '0.496')
df.iloc[:,11] = df.iloc[:,11].replace('?', '0.344')
df.iloc[:,12] = df.iloc[:,12].replace('?', '0.393')
df.iloc[:,13] = df.iloc[:,13].replace('?', '0.480') 
df.iloc[:,14] = df.iloc[:,14].replace('?', '0.570')
df.iloc[:,15] = df.iloc[:,15].replace('?', '0.535')
df.iloc[:,16] = df.iloc[:,16].replace('?', '0.618')

df.head()

from sklearn.cross_validation import train_test_split

X = df.values[:,1:]
y = df.values[:,0]

l = pd.get_dummies(y)
l = l.drop("republican",1)
y = l


X_train_full, X_holdout, y_train_full, y_holdout = train_test_split(X, y, test_size=0.3,
                                                    random_state=42)

X_train, X_test, y_train, y_test = train_test_split(X_train_full, y_train_full, test_size=0.3,
                                                    random_state=42)
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score 
from sklearn.metrics import f1_score
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import auc
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import roc_curve

model_lr = LogisticRegression()
model_lr.fit(X_train, y_train)
logacc = accuracy_score(y_test, model_lr.predict(X_test))
logacc #0.9565
precision_score(y_test, model_lr.predict(X_test))#0.948
recall_score(y_test, model_lr.predict(X_test))#0.982
f1_score(y_test, model_lr.predict(X_test))#0.964
precision, recall, threshold = precision_recall_curve(y_test, model_lr.predict(X_test))
fig, ax = plt.subplots(1, 1)
ax.plot(precision, recall)
ax.set_xlabel('Precision')
ax.set_ylabel('Recall')
ax.set_title('Precision Recall Curve')


fpr, tpr, thresholds = roc_curve(y_test, model_lr.predict(X_test))
fig, ax = plt.subplots(1, 1)
ax.plot(fpr, tpr)
ax.set_xlabel('FPR')
ax.set_ylabel('TPR')
ax.set_title('ROC curve with AUC = '+str(auc(fpr, tpr, reorder=True)))#0.949

clf = GaussianNB()
clf.fit(X_train, y_train)
yp1 = clf.predict(X_test)
accuracy_score(y_test, yp1)#0.913
precision_score(y_test, clf.predict(X_test))#0.9615
recall_score(y_test, clf.predict(X_test))#0.892
f1_score(y_test, clf.predict(X_test))#0.925

precision, recall, threshold = precision_recall_curve(y_test, clf.predict(X_test))
fig, ax = plt.subplots(1, 1)
ax.plot(precision, recall)
ax.set_xlabel('Precision')
ax.set_ylabel('Recall')
ax.set_title('Precision Recall Curve')

fpr, tpr, thresholds = roc_curve(y_test, clf.predict(X_test))
fig, ax = plt.subplots(1, 1)
ax.plot(fpr, tpr)
ax.set_xlabel('FPR')
ax.set_ylabel('TPR')
ax.set_title('ROC curve with AUC = '+str(auc(fpr, tpr, reorder=True)))#0.918

clf = SVC()
clf.fit(X_train, y_train)
accuracy_score(y_test, clf.predict(X_test))#0.934
precision_score(y_test, clf.predict(X_test))#0.98
recall_score(y_test, clf.predict(X_test))#0.911
f1_score(y_test, clf.predict(X_test))#0.944
precision, recall, threshold = precision_recall_curve(y_test, clf.predict(X_test))
fig, ax = plt.subplots(1, 1)
ax.plot(precision, recall)
ax.set_xlabel('Precision')
ax.set_ylabel('Recall')
ax.set_title('Precision Recall Curve')

fpr, tpr, thresholds = roc_curve(y_test, clf.predict(X_test))
fig, ax = plt.subplots(1, 1)
ax.plot(fpr, tpr)
ax.set_xlabel('FPR')
ax.set_ylabel('TPR')
ax.set_title('ROC curve with AUC = '+str(auc(fpr, tpr, reorder=True)))#0.918


clf = DecisionTreeClassifier(random_state=0)
clf.fit(X_train, y_train)
accuracy_score(y_test, clf.predict(X_test))#0.869
precision_score(y_test, clf.predict(X_test))#0.958
recall_score(y_test, clf.predict(X_test))#0.821
f1_score(y_test, clf.predict(X_test))#0.884
precision, recall, threshold = precision_recall_curve(y_test, clf.predict(X_test))
fig, ax = plt.subplots(1, 1)
ax.plot(precision, recall)
ax.set_xlabel('Precision')
ax.set_ylabel('Recall')
ax.set_title('Precision Recall Curve')

fpr, tpr, thresholds = roc_curve(y_test, clf.predict(X_test))
fig, ax = plt.subplots(1, 1)
ax.plot(fpr, tpr)
ax.set_xlabel('FPR')
ax.set_ylabel('TPR')
ax.set_title('ROC curve with AUC = '+str(auc(fpr, tpr, reorder=True)))#0.918

clf = RandomForestClassifier()
clf.fit(X_train, y_train)
accuracy_score(y_test,clf.predict(X_test))#0.9565
precision_score(y_test, clf.predict(X_test))#0.9615
recall_score(y_test, clf.predict(X_test))#0.928
f1_score(y_test, clf.predict(X_test))#0.962
precision, recall, threshold = precision_recall_curve(y_test, clf.predict(X_test))
fig, ax = plt.subplots(1, 1)
ax.plot(precision, recall)
ax.set_xlabel('Precision')
ax.set_ylabel('Recall')
ax.set_title('Precision Recall Curve')

fpr, tpr, thresholds = roc_curve(y_test, clf.predict(X_test))
fig, ax = plt.subplots(1, 1)
ax.plot(fpr, tpr)
ax.set_xlabel('FPR')
ax.set_ylabel('TPR')
ax.set_title('ROC curve with AUC = '+str(auc(fpr, tpr, reorder=True)))#0.918

colnames=['Age', 'Year', 'Number', 'Survive'] 
df = pd.read_csv('/Users/Rohan/Desktop/Code/haberman.data.csv', names =colnames, header = None)
df.head()




for i in range(len(df)):
    if df.Survive[i] >1:
        df.Survive[i] = 1
    else:
        df.Survive[i] = 0

y = df['Survive']
X = df.drop('Survive', axis = 1)

X_train, X_test, y_train, y_test = train_test_split(X, y,
    test_size=0.30, random_state=4444)
model_lr = LogisticRegression()
model_lr.fit(X_train, y_train)
model_lr.coef_
logacc = accuracy_score(y_test, model_lr.predict(X_test))
logacc #0.815

precision_score(y_test, model_lr.predict(X_test))#1.0
recall_score(y_test, model_lr.predict(X_test))#0.055
f1_score(y_test, model_lr.predict(X_test))#0.105
precision, recall, threshold = precision_recall_curve(y_test, model_lr.predict(X_test))
fig, ax = plt.subplots(1, 1)
ax.plot(precision, recall)
ax.set_xlabel('Precision')
ax.set_ylabel('Recall')
ax.set_title('Precision Recall Curve')


fpr, tpr, thresholds = roc_curve(y_test, model_lr.predict(X_test))
fig, ax = plt.subplots(1, 1)
ax.plot(fpr, tpr)
ax.set_xlabel('FPR')
ax.set_ylabel('TPR')
ax.set_title('ROC curve with AUC = '+str(auc(fpr, tpr, reorder=True)))#0.949
