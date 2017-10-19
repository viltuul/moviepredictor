import imdb_get_data as igd
import csv
from timeit import default_timer as timer
    
#Creates csv file of the movies of the given person. 
def csvWriter(personName):
    with open(personName + ".csv", "w") as outfile:
        writer = csv.writer(outfile)
        personId = igd.searchPersonIdByName(personName)
        person = igd.getPerson(personId)
        movieIdsInRole = {}
        errors = []
        writer.writerows([titleRowForCSV()])
        for role in igd.roles:
            movieIdsInRole = igd.getMovieIdsByRole(person, role)

            movies = igd.getMoviesByMovieIds(movieIdsInRole)
#           Write one movie at a time, then it's easier to catch and find errors  
            for movie in movies:
                try:
                    data = movieToData(movie,role)
                    writer.writerows(data)
                    print 'Movie ', movie, ' is now added to the file!'
#               If exception occurs write it down.
                except Exception as ex:
                    exToString = str(movie) + ' Error was caused by: ' + str(ex)
                    errors.append(str(exToString))
                    
    print '\n Created a csv file! \n'
    #If there were any errors let the user know.
    print len(errors), 'Errors'
    if len(errors)>0:
        print 'Erronous movies', errors
# Creates the title row for the values that are to be written in the file. When changing adding more columns to 
# the file remember to add the titles here also. Has to be in same order as movieToData method has its parameters.
def titleRowForCSV():
    return ['role','kind','title','year','runtime','genres','plot outline','rating','total votes','votes/rating'
            ,'demographic','certificates','metascore','mpaa','color info','trivia','rentals'] # rentals not working yet
    
# Here one can select the data which gets written on the csv file.
# @return the row which will be written to the csv file. Row indicates all the data from single movie.
def movieToData(movie,role):
    datarow = []
    datarow.append(role) # what was the role of the person, i.e. actor,actress,director e.t.c.
    datarow.append(getDataValue(movie, 'kind'))
    datarow.append(getDataValue(movie, 'title'))
    datarow.append(getDataValue(movie, 'year'))
    datarow.append(getDataValue(movie, 'runtime'))
    datarow.append(getDataValue(movie, 'genres'))
    datarow.append(getDataValue(movie, 'plot outline'))
    datarow.append(getDataValue(movie, 'rating'))
    datarow.append(getDataValue(movie, 'votes'))
    datarow.append(getDataValue(movie, 'number of votes'))
    datarow.append(getDataValue(movie, 'demographic'))
    datarow.append(getDataValue(movie, 'certificates'))
    datarow.append(getDataValue(movie, 'metascore'))
    datarow.append(getDataValue(movie, 'mpaa'))
    datarow.append(getDataValue(movie, 'color info'))
    datarow.append(getDataValue(movie, 'trivia'))
    datarow.append(getDataValue(movie, 'data\'][\'business\'][u\'rentals'))
    
    return [datarow]
# Gets single cell value from the get_movie method.
# @param movie, the movie objec from which the data is parsed.
# @param jsonKey, the key which will get the value from the movie object.
# @return string value which in the csv file is one cell of data.
def getDataValue(movie,jsonKey):
    cellValue = ''
    try:
        cellValue = movie[jsonKey]
    except Exception as ex:
        exToString = str(movie) + ' Error was caused by: ' + str(ex)
        print str(exToString)
    return cellValue

def createCSV(personName):
    start = timer()
    print 'Creating the csv file. Please wait. This might take a minute.'
    igd.print_on = False
    csvWriter(personName)
    end = timer()
    print 'Time taken: ', (end - start), ' seconds'  
    print 'Program is ready.'


# Anne sellors has only one movie so it's fast to get and easy to test
# Side note Anne Sellors causes exception if print_on is True. Quess some data is missing from her infoset.
# createCSV('Anne Sellors')

# Also Daisy Ridley hasn't too many movies so easy to test. Causes some errors because movie year is unknown
# for some movies.
# createCSV('Daisy Ridley')
# createCSV('Hyke Ray')
# createCSV('David Hasselhoff')
