import pandas as pd

possibleGenres = ['Action', 'Biography', 'Drama', 'War', 'Sport', 'Crime', 'Game-Show',
 'Reality-TV', 'Thriller', 'Documentary', 'Music', 'Romance', 'Adventure', 'Short', 
 'Comedy','Horror', 'Animation', 'Family', 'Fantasy', 'Sci-Fi', 'Mystery', 'History',
 'Western','Musical','Film-Noir','Short','Talk-Show']

def fillPredictedValues(fileName):
    data = pd.read_csv(fileName, error_bad_lines=False)
    data.fillna('',inplace= True)
    addBudget(data)
    addRating(data)
    data.to_csv('predicted' + fileName)

def addRating(data):
    for row in range(0,len(data.index)-1):
        value = data.iloc[row]['rating']
        if value == '':
            predictedRating = getPredictedBudgetForMovie(data.loc[row])
            data.set_value(row,'rating',predictedRating)
    return data

        
def addBudget(data):
    for row in range(0,len(data.index)-1):
        value = data.iloc[row]['budget']
        if value == '':
            predictedBudget = getPredictedBudgetForMovie(data.loc[row])
            data.set_value(row,'budget',predictedBudget)
    return data




#Andreas, put here the machine learning or linear regression implementation.
def getPredictedBudgetForMovie(movieRowObject):
    #movieRowObject['']
    return 'miljoonamiljoonaa'

def getPredicteRatingForMovie(movieRowObject):
    #movieRowObject['title']
    return 'miljoonamiljoonaa'