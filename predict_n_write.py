from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn import preprocessing

possibleGenres = ['Action', 'Biography', 'Drama', 'War', 'Sport', 'Crime', 'Game-Show',
 'Reality-TV', 'Thriller', 'Documentary', 'Music', 'Romance', 'Adventure', 'Short', 
 'Comedy','Horror', 'Animation', 'Family', 'Fantasy', 'Sci-Fi', 'Mystery', 'History',
 'Western','Musical','Film-Noir','Short','Talk-Show']

def fillPredictedValues(fileName):
    data = pd.read_csv(fileName, error_bad_lines=False)
    
    for val in ["votes", "year", "runtimes"]:
        data[val].fillna(data[val].mean(), inplace=True)
    
    categorical_values = ["role", "kind"]

    # Turn categorical values into numbers instead of strings
    for val in categorical_values:
        data[val] = data[val].astype('category')
        
    cat_columns = data.select_dtypes(['category']).columns
    data[cat_columns] = data[cat_columns].apply(lambda x: x.cat.codes) 
    data['rating'].fillna(0, inplace=True)
    data['budget'].fillna(0, inplace=True)
    addBudget(data)
    addRating(data)
    data.to_csv('predicted' + fileName)

def addRating(data):
    for row in range(0,len(data.index)-1):
        value = data.iloc[row]['rating']
        if value == 0:
            predictedRating = getPredicteRatingForMovie(data)
            data.set_value(row,'rating',predictedRating)
    return data

        
def addBudget(data):
    for row in range(0,len(data.index)-1):
        value = data.iloc[row]['budget']
        if value == 0:
            predictedBudget = getPredictedBudgetForMovie(data)
            data.set_value(row,'budget',predictedBudget)
    return data


#Andreas, put here the machine learning or linear regression implementation.
def getPredictedBudgetForMovie(df):
    df = df[df["budget"] != 0]

    #sets target and data 
    target = df['budget']
    data = df[["year", "votes", "runtimes", "rating", "role", "kind"]]  

    # Split the data and target into training/testing sets
    X_train, X_test, y_train, y_test = train_test_split(data, target, train_size = 0.8, test_size = 0.2)

    regr = linear_model.LinearRegression()

    # Train the model using the training sets
    regr.fit(X_train, y_train)
    
    return regr.predict(X_test)[0:1]

def getPredicteRatingForMovie(df):
    df = df[df["rating"] != 0]
    #sets target and data 
    target = df['rating']
    data = df[["year", "votes", "runtimes", "budget", "role", "kind"]]  

    # Split the data and target into training/testing sets
    X_train, X_test, y_train, y_test = train_test_split(data, target, train_size = 0.8, test_size = 0.2)

    regr = linear_model.LinearRegression()

    # Train the model using the training sets
    regr.fit(X_train, y_train)

    #floats can't be used as target vector with random forest
    lab_enc = preprocessing.LabelEncoder()
    y_train = lab_enc.fit_transform(y_train)
    y_test = lab_enc.fit_transform(y_test)

    return regr.predict(X_test)[0:1]

fillPredictedValues('parsedRoger Corman_main_business_vote details_keywords_taglines_trivia_release dates.csv')