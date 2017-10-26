import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def funFacts(data):
    data = data.drop(data[data['kind'] == 'tv series'].index)
    data = data.drop(data[data['kind'] == 'tv mini series'].index)
    data = data.drop(data[data['kind'] == 'video game'].index)

    facts = data['role'].value_counts()
    print '\nRoles in movies:'
    print facts,'\n'
    print getMostExpensiveMovie(data),'\n'
    print getCheapestMovie(data),'\n'
    print getHighestRankedMovie(data),'\n'
    print getLowestRankedMovie(data),'\n'

def getMostExpensiveMovie(data):
    try:
        index = data['budget'].idxmax()
        movie = data.loc[index]     
        if np.isnan(movie['budget']):
            budget = 'Not known'
        else:
            budget = movie['budget'].astype(int).astype(str) + '$'
        info = 'Most expensive movie:\n'
        info += movie['title'] + '\n Role:' + movie['role'] + ' Year:' + movie['year'].astype(int).astype(str)
        info += '\n Budget: ' + budget
        info += '\n Genres: ' + movie['genres'].replace('\'','').replace(']','').replace('[','')
        info += '\n IMDb rating: ' + movie['rating'].astype(str)
        return  info
    except Exception as ex:
        return 'Error: Most expensive movie not found!'

def getCheapestMovie(data):
    try:
        index = data['budget'].idxmin()
        movie = data.loc[index]
        if np.isnan(movie['budget']):
            budget = 'Not known'
        else:
            budget = movie['budget'].astype(int).astype(str) + '$'
        info = 'Cheapest movie:\n'
        info += movie['title'] + '\n Role:' + movie['role'] + ' Year:' + movie['year'].astype(int).astype(str)
        info += '\n Budget: ' + budget
        info += '\n Genres: ' + movie['genres'].replace('\'','').replace(']','').replace('[','')
        info += '\n IMDb rating: ' + movie['rating'].astype(str)
        return  info
    except Exception as ex:
        return 'Error: Cheapest movie not found!'

def getHighestRankedMovie(data):
    try:
        index = data['rating'].idxmax()
        movie = data.loc[index]     
        if np.isnan(movie['budget']):
            budget = 'Not known'
        else:
            budget = movie['budget'].astype(int).astype(str) + '$'
        info = 'Best rated movie:\n'
        info += movie['title'] + '\n Role:' + movie['role'] + ' Year:' + movie['year'].astype(int).astype(str)
        info += '\n Budget: ' + budget
        info += '\n Genres: ' + movie['genres'].replace('\'','').replace(']','').replace('[','')
        info += '\n IMDb rating: ' + movie['rating'].astype(str)
        return  info
    except Exception as ex:
        return 'Error: Highest rated movie not found!'

def getLowestRankedMovie(data):
    try:
        index = data['rating'].idxmin()
        movie = data.loc[index] 
        info = 'Worst rated movie:\n'
        if np.isnan(movie['budget']):
            budget = 'Not known'
        else:
            budget = movie['budget'].astype(int).astype(str) + '$'
        info += movie['title'] + '\n Role:' + movie['role'] + ' Year:' + movie['year'].astype(int).astype(str)
        info += '\n Budget: ' + budget
        info += '\n Genres: ' + movie['genres'].replace('\'','').replace(']','').replace('[','')
        info += '\n IMDb rating: ' + movie['rating'].astype(str)
        return  info
    except Exception as ex:
        return 'Error: Highest rated movie not found!'

def printFactsFromFile(fileName):
    data = pd.read_csv('parsed_data/' + fileName + '.csv', error_bad_lines=False)
    funFacts(data)
    
def plotRatingToBudget(fileName):
    try:
        data = pd.read_csv('parsed_data/' + fileName + '.csv', error_bad_lines=False)
        data = data.drop(data[np.isnan(data['rating'])].index)
        data = data.drop(data[np.isnan(data['rating'])].index)
        plt.plot(data['rating'],data['budget'],'ro' )
        plt.show()
    except Exception as ex:
        return 'Error: Couldn\'t plot rating and budget.'


#printFactsFromFile('parsed_data/parsedRoger Corman_main_business_vote details_keywords_taglines_trivia_release dates.csv')