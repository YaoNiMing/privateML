#### Pair Problem

Explore a [practice dataset](Practice_data.csv) by implementing a linear regression in five steps:

1) Plot each independent variable against the dependent variable and take note of any obvious relationships.

2) Break the data into a training set and a test set.

3) Build a few regression models using the training set. Each model is choosing what variables to include and doing this:
model = sm.OLS(y_train, X_train)
results = model.fit()

4) According to these models what can you say about the sign and certainty of the relationships between the variables in the data?  Do the independent variables have a linear relationship with the dependent variable?

5) Apply the results of each of these regression models to predict the values the dependent variable should take on in the test sample.  Compare the models using the adjusted R2 - which model performs the best in the test sample?
