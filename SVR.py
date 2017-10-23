#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from sklearn.svm import SVR
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
data = df[["role", "kind", "genres", "year", "total votes"]].values

# Split the data and target into training/testing sets
X_train, X_test, y_train, y_test = train_test_split(data, target, train_size = 0.8, test_size = 0.2)


svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
y_rbf = svr_rbf.fit(X_train, y_train)
y_pre = y_rbf.predict(X_test)

print y_pre[0:5]