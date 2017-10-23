import csv_writer as writer
import csv
import pandas as pd
import re
import numpy as np

possibleGenres = ['Action', 'Biography', 'Drama', 'War', 'Sport', 'Crime', 'Game-Show',
 'Reality-TV', 'Thriller', 'Documentary', 'Music', 'Romance', 'Adventure', 'Short', 
 'Comedy','Horror', 'Animation', 'Family', 'Fantasy', 'Sci-Fi', 'Mystery', 'History',
 'Western','Musical','Film-Noir','Short','Talk-Show']

def replaceOldFile(data, fileName):
    data.to_csv('parsed' + fileName)
    
def clean(fileName):
    data = pd.read_csv(fileName, error_bad_lines=False)
# Replace 'nan':s with empty value
    data.fillna('', inplace=True)   
    data['genres'] = parseGenres(data['genres'])
    data['runtimes'] = parseRuntimes(data['runtimes'])
    data['budget'] = parseBudget(data['budget'])
    
    data = createNewColumnsForGenres(data)
    data = putGenreValuesToGenreColumns(data)
    replaceOldFile(data,fileName)
    print fileName, 'Ready!'

def putGenreValuesToGenreColumns(data):
    i = 0
    for movie in data['genres']:
        for genre in possibleGenres:
            if genre in movie:
                data.set_value(i,genre,1)
        i = i + 1 
        
#     print data['Action']
    return data


def createNewColumnsForGenres(data):
    for genre in possibleGenres:
        newCol = np.zeros(len(data))
        data[genre] = newCol
    return data


            
def parseGenres(col):
    newCol = []
    for value in col:
        genres = []
        value = value.split('\'')
        for genre in value:           
                genres.append(genre)                
        genres = genres[1::2]
        newCol.append(genres)
    return newCol
    
def parseRuntimes(col):
    newCol = []
    for value in col:
        if value is not None:
            newCol.append('')
            continue
        value = value.split('\'')
        value[1] = int(filter(str.isdigit, value[1]))
        newCol.append(value[1])
    return newCol
    
    
def parseBudget(col):
    newCol = []
    for value in col:
        if value is not None:
            newCol.append('')
            continue
        value = value.split('\'')
        value[1] = int(filter(str.isdigit, value[1]))
        newCol.append(value[1])
    return newCol



#clean('Charles Bronson_main_business_vote details_keywords_taglines_trivia_release dates.csv')
#clean('Charlie Chaplin_main_business_vote details_keywords_taglines_trivia_release dates.csv')
#clean('Chuck Norris_main_business_vote details_keywords_taglines_trivia_release dates.csv')
#clean('Michael J. Fox_main_business_vote details_keywords_taglines_trivia_release dates.csv')
#clean('Roger Corman_main_business_vote details_keywords_taglines_trivia_release dates.csv')
#clean('Steven Seagal_main_business_vote details_keywords_taglines_trivia_release dates.csv')
#clean('Sylvester Stallone_main_business_vote details_keywords_taglines_trivia_release dates.csv')


