import imdb_get_data as igd
import csv
from timeit import default_timer as timer

main_titles = [
        'kind',
        'title',
        'year',
        'aspect_ratio',
        'genres',
        'runtimes',
        'rating',
        'votes',
        'color_info',
        'plot_outline',
        'language_codes',
        'country_codes']
main_fields = [
        'kind',
        'title',
        'year',
        'aspect ratio',
        'genres',
        'runtimes',
        'rating',
        'votes',
        'color info',
        'plot outline',
        'language codes',
        'country codes']

business_titles = [
        'budget']
business_fields = [
        'budget']

votedtls_titles = [
        'arithmetic_mean',
        'demographic',
        'number_of_votes',
        'median']
votedtls_fields = [
        'arithmetic mean',
        'demographic',
        'number of votes',
        'median']

keywords_titles = [
        'keywords']
keywords_fields = [
        'keywords']

taglines_titles = [
        'taglines']
taglines_fields = [
        'taglines']

trivia_titles = [
        'trivia']
trivia_fields = [
        'trivia']

reldates_titles = [
        'release_dates']
reldates_fields = [
        'release dates']

titles = {}
titles['main'] = main_titles
titles['business'] = business_titles
titles['vote details'] = votedtls_titles
titles['keywords'] = keywords_titles
titles['taglines'] = taglines_titles
titles['trivia'] = trivia_titles
titles['release dates'] = reldates_titles

fields = {}
fields['main'] = main_fields
fields['business'] = business_fields
fields['vote details'] = votedtls_fields
fields['keywords'] = keywords_fields
fields['taglines'] = taglines_fields
fields['trivia'] = trivia_fields
fields['release dates'] = reldates_fields
    
#Creates csv file of the movies of the given person. 
def csvWriter(personName):
    with open('raw_data/' + personName + ".csv", "w") as outfile:
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

#Creates csv file of the movies with selected infsets of the given person. 
def csvInfsetWriter(personName, infsets):
    infNames = '_'.join(infsets)
    with open('raw_data/' + personName + ".csv", "w") as outfile:
        writer = csv.writer(outfile)
        personId = igd.searchPersonIdByName(personName)
        person = igd.getPerson(personId)
        movieIdsInRole = {}
        errors = []
        writer.writerows([infTitleRowForCSV(infsets)])
        for role in igd.roles:
            movieIdsInRole = igd.getMovieIdsByRole(person, role)

            movies = igd.getMovieInfsetsByMovieIds(movieIdsInRole, infsets)
#           Write one movie at a time, then it's easier to catch and find errors  
            for movie in movies:
                try:
                    data = movieInfsetToData(movie,role,infsets)
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
    

# Creates the title row based on selected infsets
def infTitleRowForCSV(infsets):
    ret_titles = ['movieID', 'role']
    for a in infsets:
        if titles.has_key(a):
            ret_titles = ret_titles + titles.get(a)
    return ret_titles

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

# Here one can select the data which gets written on the csv file.
# @return the row which will be written to the csv file. Row indicates all the data from single movie.
def movieInfsetToData(movie,role,infsets):
    datarow = [movie.movieID, role]
    for a in infsets:
        fieldnames = fields[a]
        for b in fieldnames:
            if a == 'main':
                datarow.append(getDataValue(movie, b))
            elif a == 'business':
                td = getDataValue(movie, a)
                datarow.append(getDataValue(td, b))
            elif a == 'vote details':
                datarow.append(getDataValue(movie, b))
            elif a == 'keywords':
                datarow.append(getDataValue(movie, b))
            elif a == 'taglines':
                datarow.append(getDataValue(movie, b))
            elif a == 'trivia':
                datarow.append(getDataValue(movie, b))
            elif a == 'release dates':
                datarow.append(getDataValue(movie, b))
            else:
                datarow.append(' ')
    return [datarow]

# Gets single cell value from the get_movie method.
# @param movie, the movie objec from which the data is parsed.
# @param jsonKey, the key which will get the value from the movie object.
# @return string value which in the csv file is one cell of data.
def getDataValue(movie,jsonKey):
    cellValue = ''
    try:
        cellValue = movie[jsonKey]
        cellValue = cellValue.replace(";", "\;")
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

def createInfCSV(personName):
    start = timer()
    print 'Creating the csv file. Please wait. This might take a minute.'
    igd.print_on = True
    csvInfsetWriter(personName, ['main','business','vote details','keywords','taglines','trivia','release dates'])
    end = timer()
    print 'Time taken: ', (end - start), ' seconds'  
    print 'Program is ready.'

# Anne sellors has only one movie so it's fast to get and easy to test
# Side note Anne Sellors causes exception if print_on is True. Quess some data is missing from her infoset.
#createCSV('Anne Sellors')
#createInfCSV('Anne Sellors')
#createInfCSV('Hyke Ray')
#createInfCSV('Charles Bronson')
#createInfCSV('Robert Down Jr')
#createInfCSV('Daisy Ridley')
 
 
# Also Daisy Ridley hasn't too many movies so easy to test. Causes some errors because movie year is unknown
# for some movies.
# createCSV('Daisy Ridley')
# createCSV('Hyke Ray')
# createCSV('David Hasselhoff')
#createInfCSV('Mel Blanc')
#createInfCSV('Quentin Tarantino')
#createInfCSV('Martin Scorsese')
#createInfCSV('Christopher Nolan')
#createInfCSV('Steven Spielberg')