# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 11:00:07 2016

@author: Rohan Challenge 5
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

X_train, X_test, y_train, y_test = train_test_split(X, y,
    test_size=0.30, random_state=4444)
    

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score 
b=[]
for i in range(1,51):
    neigh = KNeighborsClassifier(n_neighbors=i)
    neigh.fit(X_train, y_train) 
    y_pred = neigh.predict(X_test)
    b.append(accuracy_score(y_pred, y_test))  

n =[]
n = [i for i in range(1,51)]

plt.plot(n,b)


#k is highest at 10

X_train_full, X_holdout, y_train_full, y_holdout = train_test_split(X, y, test_size=0.3,
                                                    random_state=42)

X_train, X_test, y_train, y_test = train_test_split(X_train_full, y_train_full, test_size=0.3,
                                                    random_state=42)
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression

model_lr = LogisticRegression()
model_lr.fit(X_train, y_train)
logacc = accuracy_score(y_test, model_lr.predict(X_test))
logacc #0.9565

l = pd.get_dummies(y)

np.sum(l.democrat)
np.sum(l.republican)

def democrat(X):
    y = 'democrat' * len(X)
    return y
def republican(X):
    y = 'republican' * len(X)
    return y
    

from sklearn.learning_curve import learning_curve

j =learning_curve(model_lr, X, y, train_sizes=np.linspace(0.1, 1.0, 10),
                    scoring=None,
                   exploit_incremental_learning=False,
                   n_jobs=1, pre_dispatch="all", verbose=0)
plt.show()

train_cv_err = np.mean(j[1], axis=1)
test_cv_err = np.mean(j[2], axis=1)

plt.plot(j[0], train_cv_err)
plt.plot(j[0], test_cv_err)


from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

clf = GaussianNB()
clf.fit(X_train, y_train)
yp1 = clf.predict(X_test)
accuracy_score(y_test, yp1)#0.913

clf = SVC()
clf.fit(X_train, y_train)
accuracy_score(y_test, clf.predict(X_test))#0.934

clf = DecisionTreeClassifier(random_state=0)
clf.fit(X_train, y_train)
accuracy_score(y_test, clf.predict(X_test))#0.869

clf = RandomForestClassifier()
clf.fit(X_train, y_train)
accuracy_score(y_test,clf.predict(X_test))#0.9565

from sklearn.cross_validation import cross_val_score

np.mean(cross_val_score(clf,X_test, y_test))
#Gaussian:0.869
#SVC:0.8462
#Decision Tree:0.902
#Random Forest:0.912

###5.10

df = pd.read_csv('house-votes-84.data.csv')

df.head()



for i in df.columns:
   print df[i].value_counts()
   
for i in df.columns:
    df[i] = df[i].replace('y','1')
    df[i] = df[i].replace('n','0')
   
df.info()
dl=df
dl.drop('Name', axis =1)


for i in dl:
    print df[i].value_counts()
  
df.iloc[:,1] = df.iloc[:,1].replace('?', '0')
df.iloc[:,2] = df.iloc[:,2].replace('?', '1')
df.iloc[:,3] = df.iloc[:,3].replace('?', '1')
df.iloc[:,4] = df.iloc[:,4].replace('?', '0')  
df.iloc[:,5] = df.iloc[:,5].replace('?', '1')
df.iloc[:,6] = df.iloc[:,6].replace('?', '1')
df.iloc[:,7] = df.iloc[:,7].replace('?', '1')
df.iloc[:,8] = df.iloc[:,8].replace('?', '1')    
df.iloc[:,9] = df.iloc[:,9].replace('?', '1')  
df.iloc[:,10] = df.iloc[:,10].replace('?', '1')
df.iloc[:,11] = df.iloc[:,11].replace('?', '0')
df.iloc[:,12] = df.iloc[:,12].replace('?', '0')
df.iloc[:,13] = df.iloc[:,13].replace('?', '1') 
df.iloc[:,14] = df.iloc[:,14].replace('?', '1')
df.iloc[:,15] = df.iloc[:,15].replace('?', '0')
df.iloc[:,16] = df.iloc[:,16].replace('?', '1')


X = df.values[:,2:]
y = df.values[:,1]

X_train, X_test, y_train, y_test = train_test_split(X, y,
    test_size=0.30, random_state=4444)
    

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score 
b=[]
for i in range(1,51):
    neigh = KNeighborsClassifier(n_neighbors=i)
    neigh.fit(X_train, y_train) 
    y_pred = neigh.predict(X_test)
    b.append(accuracy_score(y_pred, y_test))  
#k =5 
    
np.mean(cross_val_score(neigh,X_test, y_test))#0.66455

df = pd.read_csv('/Users/Rohan/Desktop/Code/movfile.csv')
df.info()
df["Movies"].fillna(method='ffill', inplace = True)
df["Number of Wins"].fillna(method='ffill', inplace = True)
df["Total Number of Nomination"].fillna(method='ffill', inplace = True)
df["IMDb Rating"].fillna(method='ffill', inplace = True)
df["IMDb Votes"].fillna(method='ffill', inplace = True)
df["Runtime (minutes)"].fillna(method='ffill', inplace = True)
df["Movie Releas Year"].fillna(method='ffill', inplace = True)
df["Director"].fillna(method='ffill', inplace = True)
df["Country"].fillna(method='ffill', inplace = True)
df["IMDb Rating"].fillna(method='ffill', inplace = True)

df2 = pd.get_dummies(df['Genre'])

frames = [df, df2]

df3 = pd.concat([df, df2], axis=1, join_axes=[df.index])
len(df3)
df3.head(20)
df['Genre'].value_counts()[:].plot(kind='barh')
df3 = df3.drop('Gender of CandidateAwards', axis = 1)
df3 = df3.drop('Director', axis = 1)
df3 = df3.drop('Winner?Awards', axis = 1)
df3 = df3.drop('FieldAwards', axis = 1)
df3 = df3.drop('Country', axis = 1)
df3 = df3.drop('Genre', axis = 1)
df3 = df3.drop('CandidateAwards', axis = 1)
df3 = df3.drop('Movies', axis = 1)
X = df3.drop(['Drama'], axis=1)
y = df3['Drama']

X_train, X_test, y_train, y_test = train_test_split(X, y,
    test_size=0.30, random_state=4444)
    

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score 
b=[]
for i in range(1,51):
    neigh = KNeighborsClassifier(n_neighbors=i)
    neigh.fit(X_train, y_train) 
    y_pred = neigh.predict(X_test)
    b.append(accuracy_score(y_pred, y_test)) 

#accuracy is 0.875
colnames=['Age', 'Year', 'Number', 'Survive'] 
df = pd.read_csv('/Users/Rohan/Desktop/Code/haberman.data.csv', names =colnames, header = None)
df.head()

np.mean(df.Age)#52.457
np.std(df.Age)#10.78

df1 = df.loc[df['Number'] >= 5]
np.mean(df1.Age)#51.09
np.std(df1.Age)#9.639

df1 = df.loc[df['Number'] <= 5]
np.mean(df1.Age)#52.868
np.std(df1.Age)#11.02

plt.hist(df['Age'])
plt.hist(df['Number'])

np.min(df['Year'])#58
np.max(df['Year'])#69

for i in range(len(df1)):
    if df1.Survive[i] >1:
        df1.Survive[i] = 1
    else:
        df1.Survive[i] = 0

y = df1['Survive']
X = df1.drop('Survive', axis = 1)

X_train, X_test, y_train, y_test = train_test_split(X, y,
    test_size=0.30, random_state=4444)
model_lr = LogisticRegression()
model_lr.fit(X_train, y_train)
model_lr.coef_
logacc = accuracy_score(y_test, model_lr.predict(X_test))
logacc #0.3913

#Age and Number are positive coeffs whuile Year is negativeto survival

print(__doc__)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.datasets import load_digits
from sklearn.model_selection import learning_curve
from sklearn.model_selection import ShuffleSplit


from matplotlib import pyplot as plt
from sklearn import metrics
import numpy as np

def data_size_response(model,trX,teX,trY,teY,score_func,prob=True,n_subsets=20):

    train_errs,test_errs = [],[]
    subset_sizes = np.exp(np.linspace(3,np.log(trX.shape[0]),n_subsets)).astype(int)

    for m in subset_sizes:
        model.fit(trX[:m],trY[:m])
        if prob:
            train_err = score_func(trY[:m],model.predict_proba(trX[:m]))
            test_err = score_func(teY,model.predict_proba(teX))
        else:
            train_err = score_func(trY[:m],model.predict(trX[:m]))
            test_err = score_func(teY,model.predict(teX))
        print "training error: %.3f test error: %.3f subset size: %.3f" % (train_err,test_err,m)
        train_errs.append(train_err)
        test_errs.append(test_err)

    return subset_sizes,train_errs,test_errs

def plot_response(subset_sizes,train_errs,test_errs):

    plt.plot(subset_sizes,train_errs,lw=2)
    plt.plot(subset_sizes,test_errs,lw=2)
    plt.legend(['Training Error','Test Error'])
    plt.xscale('log')
    plt.xlabel('Dataset size')
    plt.ylabel('Error')
    plt.title('Model response to dataset size')
    plt.show()


