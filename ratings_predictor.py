#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn import preprocessing

df = pd.read_csv('parsedRoger Corman_main_business_vote details_keywords_taglines_trivia_release dates.csv', index_col = False) 

#fills missing values with means
for val in ["rating", "votes", "year", "runtimes", "budget"]:
    df[val].fillna(df[val].mean(), inplace=True)

#sets target and data as numpy array
target = df['rating'].values
data = df[["year"]].values   #for multiple regression  data = df[["role", "kind", "genres", "year", "total votes"]].values

# Split the data and target into training/testing sets
X_train, X_test, y_train, y_test = train_test_split(data, target, train_size = 0.8, test_size = 0.2)

regr = linear_model.LinearRegression()
clf = RandomForestClassifier(n_estimators = 100, max_depth = 4)

# Train the model using the training sets
regr.fit(X_train, y_train)

#floats can't be used as target vector with random forest
lab_enc = preprocessing.LabelEncoder()
y_train = lab_enc.fit_transform(y_train)
y_test = lab_enc.fit_transform(y_test)

# Train the model using the training sets
clf.fit(X_train, y_train)

# Make predictions using the testing set
y_pred = regr.predict(X_test)
print "Linear regression predictions"
print regr.predict(X_test)[0:5]

print "Random forest predictions"
print clf.predict(X_test)[0:5]/10.0