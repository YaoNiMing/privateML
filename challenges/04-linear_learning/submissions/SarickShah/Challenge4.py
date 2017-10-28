# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 15:20:17 2016

@author: Sarick
"""
#Challenge 4
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import seaborn as sns
from sklearn.metrics import explained_variance_score, r2_score, mean_squared_error
os.chdir("C:\\Users\\Sarick\\Documents\\Python Scripts\\")
from scipy.optimize import curve_fit
import random
#%%

#Build dataset
X = range(2, 200)
y = []
for i in X:
    y.append(5 + 8*np.log(i) + random.random())

#Fit quadratic
z = np.polyfit(X, y, 2)
f = np.poly1d(z)
x_new = np.linspace(X[0], X[-1], 198)
y_new = f(x_new)
plt.plot(X,y,'o', x_new, y_new)
coefficient_of_dermination = r2_score(y, y_new)

#Fit Logarithmic
def func(x, p1,p2):
  return p1*np.log(x)+p2
popt, pcov = curve_fit(func, X, y, p0=(5,3))

# curve params
p1 = popt[0]
p2 = popt[1]

# plot curve
curvex=np.linspace(1,198, 198)
curvey=func(curvex,p1,p2)
plt.plot(curvex,curvey,'r', linewidth=5)
# plot data
plt.scatter(X, y)
plt.show()
coefficient_of_dermination = r2_score(y, curvey)
#%%
x = np.random.uniform(1, 100, 1000)
x = pd.DataFrame(x)
y = 4 + 8*x + 9*(x**2) + 20*random.normalvariate(0,1)
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_train)
mean_squared_error(y_train, y_pred)
#%%

x = np.linspace(1,5,1000)
y = np.random.uniform(0.5, 1, 1)*np.square(x) + np.random.uniform(0.5, 1, 1)*x + np.random.uniform(0.5, 1, 1) + np.random.normal(0, 1, 1000)
train_e, test_e, r2 = [], [], []

for i in range (0, 8):
    X = pd.DataFrame(np.power(x, i))
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
    model.fit(X_train, y_train)    
    y_pred = model.predict(X_train)
    train_e.append(mean_squared_error(y_train, y_pred))    
    y_pred = model.predict(X_test)
    test_e.append(mean_squared_error(y_test, y_pred))    
    r2.append(r2_score(y_test, y_pred))
    
polynomial = list(range(0,8))
plt.plot(polynomial, train_e)
plt.plot(polynomial, test_e)
plt.plot(polynomial, r2)
#%%
x = np.linspace(1,5,1000)
y = np.random.uniform(0.5, 1, 1)*np.square(x) + np.random.uniform(0.5, 1, 1)*x + np.random.uniform(0.5, 1, 1) + np.random.normal(0, 1, 1000)
x = x.reshape(-1, 1); y = y.reshape(-1, 1)

for i in range(5,750,5):
    y_train2 = y_train[0:i]
    X_train2 = X_train[0:i]
    model.fit(X_train2, y_train2)
    y_pred_train = model.predict(X_train2)
    train_e.append(mean_squared_error(y_train2, y_pred_train))    
    y_pred_test = model.predict(X_test)
    test_e.append(mean_squared_error(y_test, y_pred_test))
    
length = list(range(0, len(train_e)))
plt.plot(length, train_e)
plt.plot(length, test_e)
