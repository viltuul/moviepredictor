from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import cross_val_score

df = pd.read_csv('parsedRoger Corman_main_business_vote details_keywords_taglines_trivia_release dates.csv', index_col = False) 

#fills missing values with means
for val in ["rating", "votes", "year", "runtimes", "budget"]:
    df[val].fillna(df[val].mean(), inplace=True)

clf = RandomForestClassifier(n_estimators = 100, max_depth = 4)

#floats can't be used as target vector with random forest
lab_enc = preprocessing.LabelEncoder()
df["rating"] = lab_enc.fit_transform(df["rating"])

#sets target and data as numpy array
target = df["rating"]
data = df[["votes", "year", "runtimes", "budget"]]

# Split the data and target into training/testing sets
X_train, X_test, y_train, y_test = train_test_split(data, target, train_size = 0.8, test_size = 0.2)
clf.fit(X_train, y_train)


print clf.feature_importances_
y_pred = clf.predict(X_test)
print y_pred[0:5]/10.0
