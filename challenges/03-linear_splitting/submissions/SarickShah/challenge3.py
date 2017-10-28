import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import seaborn as sns
from sklearn.metrics import explained_variance_score, r2_score
os.chdir("C:\\Users\\Sarick\\Documents\\Python Scripts\\")
df=pd.read_csv('movies.csv')
#%%
#3.1
y = df['DomesticTotalGross']
X = np.ones([len(y),1])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = LinearRegression(normalize = True)
model.fit(X_train, y_train)
y_predict = model.predict(X_test)

plt.scatter(y_predict, y_test)
r2_score(y_test, y_predict)
'''
intercepts have almost no predictive power, an r2 score of -0.008 indicates no correlation between 
the uniform values and the domestic gross total.
'''


list1 = [(x - y1)**2 for x, y1 in zip(y_test, y_predict)]
list1 = np.array(list1).ravel()
plt.hist(list1, bins = 30)

'''
Skewed right
'''
#%%
#3.2
df = df.dropna(subset=['Budget'])
X = df['Budget']
y = df['DomesticTotalGross']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model.fit(X_train, y_train)
y_predict = model.predict(X_test)
plt.scatter(y_predict, y_test)
r2_score(y_test, y_predict)

#FINISH
#%%
#3.3
dummies = pd.get_dummies(df['Rating'], drop_first=True)
y = df['DomesticTotalGross']
X_train, X_test, y_train, y_test = train_test_split(dummies, y, test_size=0.3, random_state=42)
model.fit(X_train, y_train)
y_predict = model.predict(X_test)
plt.scatter(y_predict, y_test)
r2_score(y_test, y_predict)
#%%
#3.4
df = df.dropna()
y = df['DomesticTotalGross']
X = df[['Budget', 'Runtime']]
dummies = pd.get_dummies(df['Rating'], drop_first=True)
X = pd.concat([X, dummies], axis =1, join_axes=[X.index])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model.fit(X_train, y_train)
y_predict = model.predict(X_test)
plt.scatter(y_predict, y_test)
r2_score(y_test, y_predict)

#%%
#Did it already


