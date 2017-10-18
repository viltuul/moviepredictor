import imdb_get_data as igd
import csv
    
#Creates csv file of the movies of the given person. 
def createCSV(personName):
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
# the file remember to add the titles here also.
def titleRowForCSV():
    return ['role','title','year','runtime','rating','genres']
    
# Here one can select the data which gets written on the csv file.
# Somehow need to automize errorhandling in this method. Many movies hasn't all the data we might need,
# so my idea would be that if there is no data or its 'weird data' we write some fake data here. Or alternatively we
# write some value to the column which can be handled in the next phase of our project. You can test how the errors
# occur by running createCSV('Daisy Ridley') for example.
def movieToData(movie,role):
    datarow = []
    datarow.append(role)
    datarow.append(movie['title'])
    datarow.append(movie['year'])
    datarow.append(movie['runtime'])
    datarow.append(movie['rating'])
    datarow.append(movie['genres'])
    return [datarow]
    
igd.print_on = False
# Anne sellors has only one movie so it's fast to get and easy to test
# Side note Anne Sellors causes exception if print_on is True. Quess some data is missing from her infoset.
# createCSV('Anne Sellors')
# Also Daisy Ridley hasn't too many movies so easy to test. Causes some errors because movie year is unknown
# for some movies.
createCSV('daisy ridley')
print 'done'