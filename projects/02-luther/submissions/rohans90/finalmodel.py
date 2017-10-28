# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 11:01:52 2016

@author: Rohan
"""

#MODELLING Results
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

#original score 0.20
#try7 is 0.19
#newmod is 0.318

from sklearn import metrics

y_pred = fitn.predict(X_test)
score = metrics.r2_score(y_test, y_pred)
print (metrics.mean_squared_error(y_test, y_pred))**(0.5)
#61.76, newmod is 53.43
print score
#0.145, 0.318



##Ridge Score
from sklearn.linear_model import RidgeCV
rcv = RidgeCV(cv=10)
rcv.fit(X, y)
rcv.score(X_test, y_test)
#0.2106, new mod is 0.302
rcv.coef_
#Original score 0.238
#try7 is 0.219

y_pred = rcv.predict(X_test)
score = metrics.r2_score(y_test, y_pred)
print (metrics.mean_squared_error(y_test, y_pred))**(0.5)
#59.35, original - 0.238, try7 is 59.03, newmod is 54.04
print score
#0.2106, try 7 is 0.219, newmod is 0.302




lasso = Lasso(alpha=.79)
lasso.fit(X, y)

lasso.coef_
lasso.score(X_test,y_test)
#0.179

#original at 0.1 is 0.21
#original at 0.3 is 0.232
#original at 0.9 is 0.251

#try7 at 0.9 is 0.231
#newmod is 0.28
lasso = Lasso(alpha=0.1)
lasso.fit(X, y)

lasso.coef_
lasso.score(X_test,y_test)
#0.230
#try7 is 0.199
#newmod is 0.317


rfmod = RandomForestRegressor(n_estimators = 1000,max_features = 18, min_samples_leaf =2, n_jobs =8)
rfmod.fit(X,q)
predval = rfmod.predict(X_test)
rfmod.score(X_test, q_test)
#0.1969
#original is 0.201
#new mod is 0.48

from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

q = np.ravel(y)
q_test = np.ravel(y_test)
gbmod = GradientBoostingRegressor(n_estimators = 1000, learning_rate = .1, max_depth =10)
gbmod.fit(X, y)
prval = gbmod.predict(X_test)
gbmod.score(X_test, y_test)
gbmod.feature_importances_
plt.scatter(y_test, prval)
sorted(zip(gbmod.feature_importances_, t.columns),reverse=True)
metrics.average_precision_score(y_test, prval)
s = metrics.accuracy_score(q_test,prval)
q_test.shape
prval.shape
#original is 0.17 
#new mod is 0.679

score = metrics.r2_score(y_test, prval)
print (metrics.mean_squared_error(y_test, prval))**(0.5)
print score

#RMSE is 36.62
#Score is 0.679
import sklearn.ensemble.partial_dependence
sklearn.ensemble.partial_dependence.plot_partial_dependence
X_tr = X_train[['HQ_Yes', 'Female', 'Total_Number_of_Nomination', 'Sound', 'Cinematography', 'Best_Picture', 'Action', 'Acting', 'IMDb_Rating']]
features = ['HQ_Yes', 'Female', 'Total_Number_of_Nomination', 'Sound', 'Cinematography', 'Best_Picture', 'Action', 'Acting', 'IMDb_Rating']
fig, axs = sklearn.ensemble.partial_dependence.plot_partial_dependence(gbmod,X_tr, features)








from sklearn.linear_model import Lasso, Ridge, ElasticNet, LinearRegression
from sklearn.cross_validation import cross_val_score, train_test_split, KFold
from sklearn.grid_search import GridSearchCV

X_train, X_holdout, y_train, y_holdout = train_test_split(e, e.US_Release_to_First_Leak, test_size=0.1, random_state=42)
kfold = KFold(len(X_train), n_folds=5, shuffle=True, random_state=0)


scores = cross_val_score(gbmod, X_train, y_train, cv=kfold)
print np.mean(scores)
#[ 0.86628246  0.99884027  0.96147989  0.99420242  0.88061225]

gbmod.fit(X_train, y_train)

y_train_pred = gbmod.predict(X_train)


plt.scatter(y_train, y_train_pred, alpha=0.2)
plt.plot([0, 400], [0, 400])



X_test.head()
y_test.head()
# Fitted vs. Actual
y_test_pred = gbmod.predict(X_test)
temp =np.linspace(-600,600,1200)
plt.scatter(y_test, prval)
plt.plot([0, 400], [0, 400])
plt.title("Test v/s Predicted Days to Leak")
plt.plot(temp,temp, 'k--')

plt.xlabel('Test')
plt.ylabel('Predicted')

residualst = y_train - y_train_pred
residualst
temp =np.linspace(-600,600,1200)
plt.scatter(y_train, residualst)
plt.plot([0,400], [0, 0])
plt.ylim([-0.005,0.005])
plt.title("Actual vs. Residuals")
plt.plot(temp,temp, 'k--')
plt.xlabel('Actual')
plt.ylabel('Residuals')




residualst = q_test - y_test_pred
residualst
temp =np.linspace(-600,600,1200)
plt.scatter(y_test, residualst)
plt.plot([0,400], [0, 0])
plt.ylim([-0.0005,0.0005])
plt.title("Predicted vs. Residuals")
plt.plot(temp,temp, 'k--')
plt.xlabel('Predicted')
plt.ylabel('Residuals')


print("Lasso Model:")
params = {
    "alpha": np.logspace(-4, -.1, 20)
}

grid_est = GridSearchCV(Lasso(), param_grid=params, cv=kfold)
grid_est.fit(X_train, y_train)
df = pd.DataFrame(grid_est.grid_scores_)
df["alpha"] = df.parameters.apply(lambda val: val["alpha"])
plt.plot(np.log(df.alpha), df.mean_validation_score);
grid_est.grid_scores_

 
    
est_poly = make_pipeline(PolynomialFeatures(3), Lasso(alpha = 1))
est_poly.fit(X, y)
y_predict = est_poly.predict(X_test)
score = metrics.r2_score(y_test, y_pred)
print (metrics.mean_squared_error(y_test, y_pred))**(0.5)
#59.35, original is 58.28, try7 is 59.03, new mod is 54.04
print score
#0.21, original is 0.239, try7 is 0.219, new mod is 0.302
temp =np.linspace(-600,600,1200)
plt.scatter(y_test, y_predict)
plt.plot(temp,temp, 'k--')
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures

plt.scatter(e['US_Release_to_First_Leak'],e['IMDb_Rating'])
temp =np.linspace(-600,600,1200)
plt.plot([0,400], [0, 0])
plt.ylim([3,10])
plt.title("Days to First Leak v/s Number of Nominations")
plt.plot(temp,temp, 'k--')
plt.xlabel('Days')
plt.ylabel('Total Nominations')

#New trial 
##Try 1
y, X = patsy.dmatrices('US_Release_to_First_Leak~ screener_Yes+DVD_Yes+ HQ_Yes+ Action+Adventure+Animation+Biography+Comedy+Crime+Documentary+Drama+Family+Fantasy+History+Music+Musical+Mystery+Romance+SciFi+Sport+Thriller+War+Western+Acting+Animation+Best_Picture+Cinematography+Directing+Docu+Film_Editing+Foreign_Language_Film+Make_up_and_Hairstyling+ Music+Sound+Writing+I(Writing**2)+Female+Male+Number_of_Wins+I(Number_of_Wins**2)++np.log(Total_Number_of_Nomination)+Total_Number_of_Nomination+I(Total_Number_of_Nomination**2)+IMDb_Rating+IMDb_Votes+ Movie_Releas_Year', data=g, return_type="dataframe")
# Create your model
modeln = smf.OLS(y, X)
# Fit your model to your training set
fitn = modeln.fit()
# Print summary statistics of the model's performance
fitn.summary()

y_test, X_test = patsy.dmatrices('US_Release_to_First_Leak~ screener_Yes+DVD_Yes+ HQ_Yes+ Action+Adventure+Animation+Biography+Comedy+Crime+Documentary+Drama+Family+Fantasy+History+Music+Musical+Mystery+Romance+SciFi+Sport+Thriller+War+Western+Acting+Animation+Best_Picture+Cinematography+Directing+Docu+Film_Editing+Foreign_Language_Film+Make_up_and_Hairstyling+ Music+Sound+Writing+I(Writing**2)+Female+Male+Number_of_Wins+I(Number_of_Wins**2)+Total_Number_of_Nomination+I(Total_Number_of_Nomination**2)+IMDb_Rating+IMDb_Votes+ Movie_Releas_Year', data=g, return_type="dataframe")



