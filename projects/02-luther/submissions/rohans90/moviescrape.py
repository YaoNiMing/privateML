# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 16:01:52 2016

@author: Rohan
"""


import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split
from sklearn.decomposition import PCA
from sklearn.feature_selection import f_regression
import statsmodels.api as sm
import statsmodels.formula.api as smf
import patsy
import seaborn as sns
from seaborn import plt
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import RidgeCV

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


df1 = df.loc[df['Movie Releas Year'] > 2002]
len(df1)



df2 = pd.get_dummies(df1['Genre'])

frames = [df1, df2]

df3 = pd.concat([df1, df2], axis=1, join_axes=[df1.index])
len(df3)
df3.head(20)

df4 = pd.get_dummies(df1['FieldAwards'])
df4.info()

df4=df4.rename(columns = {'Documentary':'Docu'})


  
df5 = pd.concat([df3, df4], axis=1, join_axes=[df3.index])
len(df5)
df5.head(20)

df6 = pd.get_dummies(df1['Gender of CandidateAwards'])
  
df7 = pd.concat([df5, df6], axis=1, join_axes=[df5.index])
len(df7)
df7.head(20)

frames = [df2, df4, df6]
sum1 = pd.concat([df2, df4, df6], axis=1, join_axes=[df2.index])
sum1['final'] = sum1.sum(axis=1)



frames = [df1,sum1]
dff = pd.concat([df1, sum1], axis = 1, join_axes = [df1.index])
dff.head()

dff = dff[(dff.final != 0)]
len(dff)


l = dff['Movies']
dff2 = pd.concat([l, sum1], axis = 1, join_axes = [l.index])

dff2.head()

fd = dff2.groupby(['Movies']).sum()
fd.head()




df1.drop('FieldAwards', axis=1, inplace = True)
df1.drop('Genre', axis=1, inplace = True)
df1.drop('CandidateAwards', axis=1, inplace = True)
df1.drop('Gender of CandidateAwards', axis=1, inplace = True)
df1.drop('Winner?Awards', axis=1, inplace = True)

len(df1)

df1.groupby('Movies')

df9 = df1.drop_duplicates('Movies')

df9 = df9.set_index(['Movies'])
df9.info()
df9.head()
len(df9)

fd.head(20)
len(fd)




result = pd.merge(fd, df9,left_index = True,  right_index=True,how ='outer')
result.head()
len(result)


result.drop('final', axis=1, inplace = True)




af = pd.read_csv('/Users/Rohan/Desktop/Code/mov_filep.csv')
af.head()
af.columns

af.drop('US Release Date', axis=1, inplace = True)
af.drop('Oscar Screener Release', axis=1, inplace = True)
af.drop('Cam Leak', axis=1, inplace = True)
af.drop('Telesync Leak', axis=1, inplace = True)

af.drop('HQ Rip Leak (Telecine/R5/PPV/Webrip/WebDL/HDRip)', axis=1, inplace = True)
af.drop('Screener Leak', axis=1, inplace = True)
af.drop('Retail Leak (DVD/Blu-Ray)', axis=1, inplace = True)
af.drop('US Release to Screener Leak', axis=1, inplace = True)

af.drop('Screener Release to Screener Leak', axis=1, inplace = True)
af.drop('Ceremony Date', axis=1, inplace = True)
af.drop('US Release to DVD/Blu-Ray Leak', axis=1, inplace = True)


af=af.rename(columns = {'itle':'Movies'})

af.set_index(['Movies'])

af2 = pd.get_dummies(af['Screener Leaked by Oscar Night?'], prefix = "screener")
af3 = pd.get_dummies(af['Screener/Retail DVD Leaked by Oscar Night?'], prefix = "DVD")
af4 = pd.get_dummies(af['High-Quality Leak by Oscar Night?'], prefix = "HQ")

af1 = pd.concat([af, af2, af3, af4], axis=1, join_axes=[af2.index])
len(af1)
af1.head(20)


af1.drop('Screener Leaked by Oscar Night?', axis=1, inplace = True)
af1.drop('Screener/Retail DVD Leaked by Oscar Night?', axis=1, inplace = True)
af1.drop('High-Quality Leak by Oscar Night?', axis=1, inplace = True)

aa = af1.set_index(['Movies'])
aa.head()
result.head()

result2 = result.reset_index()
result2.head()

l = result2["Movies"]


import re
r1 = re.compile("(.*?)\s*\(")
r2 = re.compile(".*?\((.*?)\)")
a =[]
for i in l:
    m1 = r1.match(i)
    a.append(m1.group(1))
print a

result2["Mov"] = a



result2.drop('mov', axis=1, inplace = True)
result2.drop('Movies', axis=1, inplace = True)

result2=result2.rename(columns = {'Mov':'Movies'})

result2 = result2.set_index(['Movies'])





d = pd.merge(aa, result2,left_index = True,right_index = True, how = "left")
len(d)
d.head(50)

d["IMDb Votes"].isnull().sum()
#447-151 = 296

d.info()
#####################  Modeling ##############################
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import patsy
import seaborn as sns
from seaborn import plt
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import RidgeCV

d.head()
d.drop('Oscar Year', axis=1, inplace = True)
d.drop('Director', axis=1, inplace = True)
d.drop('Country', axis=1, inplace = True)


e = d.apply(lambda x: x.fillna(x.median()),axis=0)

e.info()
e.corr()
e.columns

e["News"].sum()
e["Short"].sum()

e.sum(axis=0)

e.drop('News', axis=1, inplace = True)
e.drop('Short', axis=1, inplace = True)
e.drop('Horror', axis=1, inplace = True)
e.drop('Special Award', axis=1, inplace = True)
e.drop('Short Film', axis=1, inplace = True)
#Correlation

from string import letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="white")
corr = e.corr()
# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(30, 40))
# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)
# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.2,
            square=True, xticklabels=2, yticklabels=2,
            linewidths=.3, cbar_kws={"shrink": .5}, ax=ax)
            
            
sns.pairplot(e, size = 1.2, aspect=1.5)

e.drop('DVD_No', axis=1, inplace = True)
e.drop('HQ_No', axis=1, inplace = True)
e.drop('screener_No', axis=1, inplace = True)
# Create an empty model
lr = LinearRegression()
# Choose the predictor variables, here all but the first which is the response variable
# This model is analogous to the Y ~ X1 + X2 + X3 + X4 + X5 + X6 model
X = e.iloc[:, 1:]
# Choose the response variable(s)
y = e.iloc[:, 0]
# Fit the model to the full dataset
lr.fit(X, y)
# Print out the R^2 for the model against the full dataset
lr.score(X,y)
lr.intercept_
lr.coef_
lr._decision_function

e.columns = e.columns.map(str.strip)

from pandas import compat

compat.PY3 = True

e.columns = [x.strip().replace(' ' , '_') for x in e.columns]

e.columns

e.rename(columns={'Sci-Fi': 'SciFi'}, inplace=True)


# Create your feature matrix (X) and target vector (y)

y, X = patsy.dmatrices('US_Release_to_First_Leak~ screener_Yes+DVD_Yes+ HQ_Yes+ Action+Adventure+Animation+Biography+Comedy+Crime+Documentary+Drama+Family+Fantasy+History+Music+Musical+Mystery+Romance+SciFi+Sport+Thriller+War+Western+Acting+Animation+Best_Picture+Cinematography+Directing+Documentary+Film_Editing+Foreign_Language_Film+Make_up_and_Hairstyling+ Music+Sound+Writing+Female+Male+Number_of_Wins+Total_Number_of_Nomination+IMDb_Rating+IMDb_Votes+ Movie_Releas_Year', data=e, return_type="dataframe")
# Create your model
model = sm.OLS(y, X)
# Fit your model to your training set
fit = model.fit()
# Print summary statistics of the model's performance
fit.summary()





#Working on regularized/standardized data

std_scale = preprocessing.StandardScaler().fit(e[['screener_Yes','DVD_Yes','HQ_Yes', 'Action','Adventure','Animation', 'Biography','Comedy','Crime','Documentary','Drama','Family','Fantasy','History','Music','Musical','Mystery','Romance','SciFi','Sport','Thriller','War','Western','Acting','Animation','Best_Picture','Cinematography','Directing','Documentary','Film_Editing','Foreign_Language_Film','Make_up_and_Hairstyling','Music','Sound','Writing','Female','Male','Number_of_Wins','Total_Number_of_Nomination','IMDb_Rating','IMDb_Votes', 'Movie_Releas_Year']])
e_std = std_scale.transform(e[['screener_Yes','DVD_Yes','HQ_Yes', 'Action','Adventure','Animation', 'Biography','Comedy','Crime','Documentary','Drama','Family','Fantasy','History','Music','Musical','Mystery','Romance','SciFi','Sport','Thriller','War','Western','Acting','Animation','Best_Picture','Cinematography','Directing','Documentary','Film_Editing','Foreign_Language_Film','Make_up_and_Hairstyling','Music','Sound','Writing','Female','Male','Number_of_Wins','Total_Number_of_Nomination','IMDb_Rating','IMDb_Votes', 'Movie_Releas_Year']])

minmax_scale = preprocessing.MinMaxScaler().fit(e[['screener_Yes','DVD_Yes','HQ_Yes', 'Action','Adventure','Animation', 'Biography','Comedy','Crime','Documentary','Drama','Family','Fantasy','History','Music','Musical','Mystery','Romance','SciFi','Sport','Thriller','War','Western','Acting','Animation','Best_Picture','Cinematography','Directing','Documentary','Film_Editing','Foreign_Language_Film','Make_up_and_Hairstyling','Music','Sound','Writing','Female','Male','Number_of_Wins','Total_Number_of_Nomination','IMDb_Rating','IMDb_Votes', 'Movie_Releas_Year']])
e_minmax = minmax_scale.transform(e[['screener_Yes','DVD_Yes','HQ_Yes', 'Action','Adventure','Animation', 'Biography','Comedy','Crime','Documentary','Drama','Family','Fantasy','History','Music','Musical','Mystery','Romance','SciFi','Sport','Thriller','War','Western','Acting','Animation','Best_Picture','Cinematography','Directing','Documentary','Film_Editing','Foreign_Language_Film','Make_up_and_Hairstyling','Music','Sound','Writing','Female','Male','Number_of_Wins','Total_Number_of_Nomination','IMDb_Rating','IMDb_Votes', 'Movie_Releas_Year']])

X_mov = e.values[:,1:]
y_mov = e.values[:,0]

X_train, X_test, y_train, y_test = train_test_split(X_mov, y_mov,
    test_size=0.30, random_state=42)
    
std_scale = preprocessing.StandardScaler().fit(X_train)
X_train_std = std_scale.transform(X_train)
X_test_std = std_scale.transform(X_test)

X_train_std = pd.DataFrame(X_train_std)
X_test_std = pd.DataFrame(X_test_std)

 

y_train = pd.DataFrame(y_train)
y_test = pd.DataFrame(y_test)



g = pd.DataFrame(data=X_train_std[0:,0:],    # values
          index=range(312),    # 1st column as index
          columns=e.columns[1:,])

g["US_Release_to_First_Leak"] = y_train

g.head()

t = pd.DataFrame(data=X_test_std[0:,0:],    # values
          index=range(135),    # 1st column as index
          columns=e.columns[1:,])
t["US_Release_to_First_Leak"] = y_test 

t.head()        
#############
from sklearn.datasets import load_diabetes
from sklearn.linear_model import Lasso, Ridge, ElasticNet, LinearRegression

from sklearn.cross_validation import cross_val_score, train_test_split, KFold
from sklearn.grid_search import GridSearchCV

kfold = KFold(len(X_train), n_folds=5, shuffle=True, random_state=0)

print("Lasso Model:")
params = {
    "alpha": np.logspace(-4, -.1, 20)
}

grid_est = GridSearchCV(Lasso(), param_grid=params, cv=kfold)
grid_est.fit(X_train_std, y_train)
df = pd.DataFrame(grid_est.grid_scores_)
df["alpha"] = df.parameters.apply(lambda val: val["alpha"])
plt.plot(np.log(df.alpha), df.mean_validation_score);
grid_est.grid_scores_


print("Ridge Model:")
params = {
    "alpha": np.logspace(-4, -.1, 20)
}

grid_est = GridSearchCV(Ridge(), param_grid=params, cv=kfold)
grid_est.fit(X_train, y_train)
df = pd.DataFrame(grid_est.grid_scores_)
df["alpha"] = df.parameters.apply(lambda val: val["alpha"])
plt.plot(np.log(df.alpha), df.mean_validation_score);
grid_est.grid_scores_



from sklearn.metrics import r2_score, mean_squared_error

y_pred = lin_reg_est.predict(X_holdout)
print("Linear Regression:", r2_score(y_holdout, y_pred))

y_pred = lasso_grid_est.predict(X_holdout)
print("Lasso Regression:", r2_score(y_holdout, y_pred))

y_pred = ridge_grid_est.predict(X_holdout)
print("Ridge Regression:", r2_score(y_holdout, y_pred))

y_pred = elastic_net_grid_est.predict(X_holdout)
print("ElasticNet Regression:", r2_score(y_holdout, y_pred))


plt.scatter('US_Release_to_First_Leak', 'Movie_Releas_Year', data = g)

##Try 1
y, X = patsy.dmatrices('US_Release_to_First_Leak~ screener_Yes+DVD_Yes+ HQ_Yes+ Action+Adventure+Animation+Biography+Comedy+Crime+Documentary+Drama+Family+Fantasy+History+Music+Musical+Mystery+Romance+SciFi+Sport+Thriller+War+Western+Acting+Animation+Best_Picture+Cinematography+Directing+Docu+Film_Editing+Foreign_Language_Film+Make_up_and_Hairstyling+ Music+Sound+Writing+Female+Male+Number_of_Wins+Total_Number_of_Nomination+IMDb_Rating+IMDb_Votes+ Movie_Releas_Year', data=g, return_type="dataframe")
# Create your model
model = smf.OLS(y, X)
# Fit your model to your training set
fit = model.fit()
# Print summary statistics of the model's performance
fit.summary()

y_test, X_test = patsy.dmatrices('US_Release_to_First_Leak~ screener_Yes+DVD_Yes+ HQ_Yes+ Action+Adventure+Animation+Biography+Comedy+Crime+Documentary+Drama+Family+Fantasy+History+Music+Musical+Mystery+Romance+SciFi+Sport+Thriller+War+Western+Acting+Animation+Best_Picture+Cinematography+Directing+Docu+Film_Editing+Foreign_Language_Film+Make_up_and_Hairstyling+ Music+Sound+Writing+Female+Male+Number_of_Wins+Total_Number_of_Nomination+IMDb_Rating+IMDb_Votes+ Movie_Releas_Year', data=t, return_type="dataframe")

##TRY 7
y, X = patsy.dmatrices('US_Release_to_First_Leak~ DVD_Yes+ HQ_Yes+ Adventure+Documentary+Drama+Mystery+Romance+SciFi+War+Acting+Directing+Sound+Writing+Number_of_Wins+Total_Number_of_Nomination+ Movie_Releas_Year', data=g, return_type="dataframe")
# Create your model
model7 = sm.OLS(y, X)
# Fit your model to your training set
fit7 = model7.fit()
# Print summary statistics of the model's performance
fit7.summary()

y_test, X_test = patsy.dmatrices('US_Release_to_First_Leak~ DVD_Yes+ HQ_Yes+ Adventure+Documentary+Drama+Mystery+Romance+SciFi+War+Acting+Directing+Sound+Writing+Number_of_Wins+Total_Number_of_Nomination+ Movie_Releas_Year', data=t, return_type="dataframe")


#Polynomial
y, X = patsy.dmatrices('US_Release_to_First_Leak~ DVD_Yes +HQ_Yes+Documentary+Drama+Mystery+Romance+SciFi+War+Acting+Directing+Sound+Writing+I(Writing**2)+Number_of_Wins+I(Number_of_Wins**2)+Total_Number_of_Nomination+ I(Total_Number_of_Nomination**2) +Movie_Releas_Year', data=g, return_type="dataframe")
# Create your model
modelf = smf.OLS(y, X)
# Fit your model to your training set
fitf = modelf.fit()
# Print summary statistics of the model's performance
fitf.summary()

y_test, X_test = patsy.dmatrices('US_Release_to_First_Leak~ DVD_Yes +HQ_Yes+Documentary+Drama+Mystery+Romance+SciFi+War+Acting+Directing+Sound+Writing+I(Writing**2)+Number_of_Wins+I(Number_of_Wins**2)+Total_Number_of_Nomination+ I(Total_Number_of_Nomination**2) +Movie_Releas_Year', data=t, return_type="dataframe")

lr = LinearRegression()
lr.fit(X, y)
# Print out the R^2 for the model against the full dataset
lr.score(X_test,y_test)
#0.1455

from sklearn import metrics

y_pred = fitf.predict(X_test)
score = metrics.r2_score(y_test, y_pred)
print (metrics.mean_squared_error(y_test, y_pred))**(0.5)
#61.76
print score
#0.145




    
    



# STUDENT SECTION
# Let's visualize some of the different variables against 'cnt'
# Temp
l = e
l.reset_index(inplace = True)
l.head()
l.groupby

plt.scatter(l['US_Release_to_First_Leak'], l['Number_of_Wins'])

fig, ax = plt.subplots(1,1, figsize=(15,10))
ax.set_title('US Release by IMDb Votes')
# Create a seaborn boxplot of count by temperature ordered by temperature
sns.barplot(x=l['US_Release_to_First_Leak'].sort_values(), y=l['IMDb_Votes'])
ax.set_xlabel('Days after Release')
ax.set_ylabel('IMDb Votes')
plt.xticks(rotation = 90)


X_test_std.columns
mi = mutual_info_regression(X, y)
mi /= np.max(mi)
mi

from sklearn.feature_selection import f_regression, mutual_info_regression
from sklearn.feature_selection import mutual_info_regression


##Random Forest

from sklearn.ensemble import RandomForestRegressor
import numpy as np
rf = RandomForestRegressor()
rf.fit(X, y)
rf.feature_importances_
rf.score(X_test,y_test)
#0.053
sorted(zip(rf.feature_importances_, g.columns),reverse=True)




from sklearn import metrics
y_pred = fit.predict(X_test)
score = metrics.r2_score(y_test, y_pred)
metrics.accuracy_score(y_train, y_pred)

import metrics from scikit learn first

##Ridge Score
from sklearn.linear_model import RidgeCV
rcv = RidgeCV(cv=10)
rcv.fit(X, y)
rcv.score(X_test, y_test)
#0.2106
rcv.coef_

y_pred = rcv.predict(X_test)
score = metrics.r2_score(y_test, y_pred)
print (metrics.mean_squared_error(y_test, y_pred))**(0.5)
#59.35
print score
0.2106


from sklearn.linear_model import Lasso
from sklearn.preprocessing import StandardScaler
  
lasso = Lasso(alpha=.1)
lasso.fit(X, y)

lasso.coef_
lasso.score(X_test,y_test)
#0.179



lasso = Lasso(alpha=.9)
lasso.fit(X, y)

lasso.coef_
lasso.score(X_test,y_test)
#0.2265

rfmod = RandomForestRegressor(n_estimators = 1000,max_features = 18, min_samples_leaf =2, n_jobs =8)
rfmod.fit(X,y)
predval = rfmod.predict(X_test)
rfmod.score(X_test, y_test)
#0.1969







#SEARCHING DIFFERENT PARAMETERS
# define the parameter values that should be searched
k_range = list(range(1, 45))
weight_options = ['uniform', 'distance']

# create a parameter grid: map the parameter names to the values that should be searched
param_grid = dict(n_neighbors=k_range, weights=weight_options)
print(param_grid)

# instantiate and fit the grid
grid = GridSearchCV(knn, param_grid, cv=10, scoring='accuracy')
grid.fit(X, y)

# view the complete results
grid.grid_scores_

# examine the best model
print(grid.best_score_)
print(grid.best_params_)

##best params to make predictions
# train your model using all data and the best known parameters
knn = KNeighborsRegressor(n_neighbors=20, weights='uniform')
knn.fit(X_train_std, y_train)
knn.score(X_test_std,y_test)


















