import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import plotly.graph_objs as go
import plotly.figure_factory as FF
from plotly.offline import download_plotlyjs, init_notebook_mode, plot,iplot


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
    
def plotRatingToBudget(name):
    try:
        df = pd.read_csv('parsed_data/' + name + '.csv')
        df['year'] = df['year'].apply(lambda y:str(y))
        df['text'] = df[['title', 'year']].apply(lambda x: ' '.join(x), axis=1)
        df['text'] = df['text'].apply(lambda x: x[0:-2])
        data = [go.Scatter( x=df['rating'], y=df['budget'],
                  text = df['text'],
                  textposition = 'top center',
                  mode = 'markers')]


        iplot(data, filename='parsed_data/Robert Down Jr.csv')
    except Exception as ex:
        print ex
        print 'Maeby the name is written wrong or there is no file from ', name

def plotRatingToBudgetPredict(name):
    try:
        df = pd.read_csv('predicted_data/' + name + '.csv')
        df['year'] = df['year'].apply(lambda y:str(y))
        df['text'] = df[['title', 'year']].apply(lambda x: ' '.join(x), axis=1)
        df['text'] = df['text'].apply(lambda x: x[0:-2])
        data = [go.Scatter( x=df['rating'], y=df['budget'],
                  text = df['text'],
                  textposition = 'top center',
                  mode = 'markers')]


        iplot(data, filename='parsed_data/Robert Down Jr.csv')
    except Exception as ex:
        print ex
        print 'Maeby the name is written wrong or there is no file from ', name

def plotRatingToYear(name):
    try:
        df = pd.read_csv('parsed_data/' + name + '.csv')
        data = [go.Scatter( x=df['year'], y=df['rating'],
                  text = df['title'],
                  textposition = 'top center',
                  mode = 'markers')]


        iplot(data, filename='parsed_data/Robert Down Jr.csv')
    except Exception as ex:
        print ex
        print 'Maeby the name is written wrong or there is no file from ', name

def correlationBetweenYearAndRating(name):
    try:
        df = pd.read_csv('parsed_data/' + name + '.csv')
        df = df[['year','rating']]
        print df.corr(method='pearson', min_periods=1)
    except Exception as ex:
        print ex
#printFactsFromFile('parsed_data/parsedRoger Corman_main_business_vote details_keywords_taglines_trivia_release dates.csv')
#df = df[~np.isnan(df['budget'])]
#df = df[~np.isnan(df['rating'])]
#df = df[['title','rating','budget']]