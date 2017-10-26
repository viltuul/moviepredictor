#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import pandas as pd


df = pd.read_csv('parsed_data/parsedRoger Corman_main_business_vote details_keywords_taglines_trivia_release dates.csv', index_col = False) 

#fills missing values with means
for val in ["rating", "votes", "year"]:
    df[val].fillna(df[val].mean(), inplace=True)
    

categorical_values = ["role", "kind", "genres"]

# Turn categorical values into numbers instead of strings
for val in categorical_values:
    df[val] = df[val].astype('category')

cat_columns = df.select_dtypes(['category']).columns
df[cat_columns] = df[cat_columns].apply(lambda x: x.cat.codes)

#sets target and data as numpy array
target = df['rating'].values
data = df[["year"]].values   #for multiple regression  data = df[["role", "kind", "genres", "year", "total votes"]].values

# Split the data and target into training/testing sets
X_train, X_test, y_train, y_test = train_test_split(data, target, train_size = 0.8, test_size = 0.2)

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(X_train, y_train)

# Make predictions using the testing set
y_pred = regr.predict(X_test)
print y_pred[0:5]

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(y_test, y_pred))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(y_test, y_pred))

# Plot outputs
plt.scatter(X_test, y_test,  color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()