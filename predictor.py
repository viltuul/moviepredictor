#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn import preprocessing
import sys

#path to csv file used in predictions
file_path = sys.argv[1]

df = pd.read_csv(file_path, index_col = False) 

#genre
if len(sys.argv) > 2:
    genre = sys.argv[2]
    df = df[df[genre] == 1]
else:
    genre =""    

#fills missing values with means
for val in ["rating", "votes", "year", "runtimes", "budget"]:
    df[val].fillna(df[val].mean(), inplace=True)
    
categorical_values = ["role", "kind"]

# Turn categorical values into numbers instead of strings
for val in categorical_values:
    df[val] = df[val].astype('category')

cat_columns = df.select_dtypes(['category']).columns
df[cat_columns] = df[cat_columns].apply(lambda x: x.cat.codes)

#sets target and data 
target1 = df['rating']
data1 = df[["year", "votes", "runtimes", "budget", "role", "kind"]]  
target2 = df["budget"].astype(int)
data2 = df[["rating", "year", "runtimes", "votes", "role", "kind"]]  

# Split the data and target into training/testing sets
X_train1, X_test1, y_train1, y_test1 = train_test_split(data1, target1, train_size = 0.8, test_size = 0.2)
X_train2, X_test2, y_train2, y_test2 = train_test_split(data2, target2, train_size = 0.8, test_size = 0.2)

regr1 = linear_model.LinearRegression()
clf1 = RandomForestClassifier(n_estimators = 100, max_depth = 4)
regr2 = linear_model.LinearRegression()
clf2 = RandomForestClassifier(n_estimators = 100, max_depth = 4)

# Train the model using the training sets
regr1.fit(X_train1, y_train1)
regr2.fit(X_train2, y_train2)

#floats can't be used as target vector with random forest
lab_enc = preprocessing.LabelEncoder()
y_train1 = lab_enc.fit_transform(y_train1)
y_test1 = lab_enc.fit_transform(y_test1)

# Train the model using the training sets
clf1.fit(X_train1, y_train1)
clf2.fit(X_train2, y_train2)

# Make predictions using the testing set
print "Linear regression predictions for person's next 5",genre,"movies ratings"
print regr1.predict(X_test1)[0:5]

print "Random forest predictions for next person's 5",genre,"movies ratings"
print clf1.predict(X_test1)[0:5]/10.0

print "Random forest importance"
print clf1.feature_importances_
print
# Make predictions using the testing set
print "Linear regression predictions for person's next 5",genre,"movies budgets"
print regr2.predict(X_test2)[0:5]

print "Random forest predictions for person's next 5",genre,"movies budgets"
print clf2.predict(X_test2)[0:5]

print "Random forest feature importance"
print clf2.feature_importances_
