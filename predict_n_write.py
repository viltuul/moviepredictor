from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

possibleGenres = ['Action', 'Biography', 'Drama', 'War', 'Sport', 'Crime', 'Game-Show',
 'Reality-TV', 'Thriller', 'Documentary', 'Music', 'Romance', 'Adventure', 'Short', 
 'Comedy','Horror', 'Animation', 'Family', 'Fantasy', 'Sci-Fi', 'Mystery', 'History',
 'Western','Musical','Film-Noir','Short','Talk-Show']

def fillPredictedValues(fileName):
    data = pd.read_csv('parsed_data/' + fileName, error_bad_lines=False)
    
    for val in ["votes", "year", "runtimes"]:
        data[val].fillna(round(data[val].mean()), inplace=True)
    
    categorical_values = ["role", "kind"]
    temprole = data["role"]
    tempkind = data["kind"]

    # Turn categorical values into numbers instead of strings
    for val in categorical_values:
        data[val] = data[val].astype('category')
        
    cat_columns = data.select_dtypes(['category']).columns
    data[cat_columns] = data[cat_columns].apply(lambda x: x.cat.codes) 
    
    data['budget'].fillna(0, inplace=True)
    data['rating'].fillna(0, inplace=True)

    try:
        addRating(data)
        addBudget(data)
        data["role"] = temprole
        data["kind"] = tempkind
        data.to_csv('predicted_data/predicted' + fileName)
        print fileName,'Ready!'
    except Exception as ex:
        print ex
        print 'The file ', fileName, ' might be insufficent. Check if there is any values in \'budget\' column from \'raw_data\' folder'


def addRating(data):
    for row in range(len(data)-1, -1, -1):
        value = data.iloc[row]['rating']
        if value == 0:
            predictedRating = getPredicteRatingForMovie(data)
            data.set_value(row,'rating',predictedRating)
    return data

        
def addBudget(data):
    for row in range(len(data)-1, -1, -1):
        value = data.iloc[row]['budget']
        if value == 0:
            predictedBudget = getPredictedBudgetForMovie(data)
            data.set_value(row,'budget',predictedBudget)
    return data


#Andreas, put here the machine learning or linear regression implementation.
def getPredictedBudgetForMovie(df):
    df = df[df["budget"] > 0]

    #sets target and data 
    target = df['budget']
    data = df[["rating", "year", "votes", "runtimes", "role", "kind"]]  

    # Split the data and target into training/testing sets
    X_train, X_test, y_train, y_test = train_test_split(data, target, train_size = 0.8, test_size = 0.2)

    regr = linear_model.LinearRegression()

    # Train the model using the training sets
    regr.fit(X_train, y_train)
    
    return round(max(regr.predict(X_test)), -4)

def getPredicteRatingForMovie(df):
    df = df[df["rating"] > 0]
    df = df[df["budget"] > 0]
    #sets target and data 
    target = df['rating']
    data = df[["year", "votes", "runtimes", "budget", "role", "kind"]]  

    # Split the data and target into training/testing sets
    X_train, X_test, y_train, y_test = train_test_split(data, target, train_size = 0.8, test_size = 0.2)

    regr = linear_model.LinearRegression()

    # Train the model using the training sets
    regr.fit(X_train, y_train)

    return round(max(regr.predict(X_test)),1)

#fillPredictedValues('Roger Corman.csv')


fillPredictedValues('Brad Pitt.csv')
fillPredictedValues('Al Pacino.csv')
fillPredictedValues('Ron Jeremy.csv')
fillPredictedValues('Roger Corman.csv')
