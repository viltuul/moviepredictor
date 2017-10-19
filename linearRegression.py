#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import pandas as pd


df = pd.read_csv('David Hasselhoff.csv', index_col = False) 

#fills missing values with means
for val in ["rating", "total votes", "year"]:
    df[val].fillna(df[val].mean(), inplace=True)
    

categorical_values = ["role", "kind", "genres"]

# Turn categorical values into numbers instead of strings
for val in categorical_values:
    df[val] = df[val].astype('category')

cat_columns = df.select_dtypes(['category']).columns
df[cat_columns] = df[cat_columns].apply(lambda x: x.cat.codes)

#sets target and data as numpy array
target = df['rating'].values
data = df[["year"]].values

#attempt 1 to fix size issue
target = np.array(target)
data = np.array(data)

# Split the data into training/testing sets
X_train = data[:-20]
X_test = data[-20:]


# Split the targets into training/testing sets
y_train = target[:-20]
y_test = target[-20:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(X_train, y_train)

# Make predictions using the testing set
y_pred = regr.predict(X_test)
print y_pred [0:5]

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(y_test, y_pred))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(y_test, y_pred))

print len(X_test)
print len(y_test)
# Plot outputs
plt.scatter(X_test, y_test,  color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()