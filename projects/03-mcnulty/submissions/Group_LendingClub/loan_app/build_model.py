import re
from sklearn.externals import joblib 
import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.preprocessing import LabelEncoder


if __name__ == "__main__":
        
    df_applicant = pd.read_csv('loan_app_data.csv')
    df_applicant = df_applicant.replace(-1.0, np.nan)
    df_applicant = df_applicant.dropna()
    X = df_applicant.drop(['Accepted'], axis=1)
    y = df_applicant['Accepted']
    
    X_nozip = X.drop(['zip_code'], axis=1)
    X_title = X_nozip['title']
    X_state = X_nozip['addr_state']
    X_emp = X_nozip['emp_length']
    X_numerical = X_nozip[['loan_amnt', 'dti']]
    enc = LabelEncoder()
    X_title = enc.fit_transform(X_title)
    X_state = enc.fit_transform(X_state)
    X_emp = enc.fit_transform(X_emp)
    X_title = pd.DataFrame(X_title)
    X_state = pd.DataFrame(X_state)
    X_emp = pd.DataFrame(X_emp)

    frames = [X_numerical, X_title, X_state, X_emp]
    X_final = pd.concat(frames, axis=1, join_axes=[X_title.index])
    columns = ['loan_amnt', 'dti', 'title', 'addr_state', 'emp_length']
    X_final.columns = columns

    gbm = xgb.XGBClassifier(max_depth = 2, n_estimators=200, learning_rate=0.1).fit(X_nozip, y)


    joblib.dump(gbm, 'models/loan_decision.pkl')
