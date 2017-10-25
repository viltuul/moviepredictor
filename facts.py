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
    plotRatingToBudget(data)


def getMostExpensiveMovie(data):
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

def getCheapestMovie(data):
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

def getHighestRankedMovie(data):
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

def getLowestRankedMovie(data):
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

def printFactsFromFile(fileName):
    data = pd.read_csv(fileName, error_bad_lines=False)
    funFacts(data)
    
def plotRatingToBudget(data):
    data = data.drop(data[np.isnan(data['rating'])].index)
    data = data.drop(data[np.isnan(data['rating'])].index)
    plt.plot(data['rating'],data['budget'],'ro' )
    plt.show()

printFactsFromFile('parsed_data/parsedRoger Corman_main_business_vote details_keywords_taglines_trivia_release dates.csv')