import json
import imdb_get_data as igd
# gets the data from all movies of the person and writes it on a JSON file.
def movieDataToJSON(personName):
    with open(personName + ".json", "w") as outfile:
        personId = igd.searchPersonIdByName(personName)
        person = igd.getPerson(personId)
        movieIdsInRole = {}
        for role in roles:
            movieIdsInRole[role] = igd.getMovieIdsByRole(person, role)
            movies = igd.getMoviesByMovieIds(movieIdsInRole.get(role))
            for movie in movies:
                data = vars(movie)
                json.dump(data, outfile, sort_keys=True, indent=4, separators=(',', ': '))
    print 'Created a json file!'

    
# private method to change the movie data to json style
#def movieToData(movie, role):
#    thisRole = role;
#    title = movie['title']
#    year = movie['year']
#    rating = movie['rating']
#    votes = movie['votes']
#    #runtime = movie['runtimes']
#    genres = movie['genres']
#    #mpaa = movie['mpaa']
#    data = {'title':title,
#            'year':year,
#            'rating':rating,
#            'votes': votes,
#            'genres': [genres]}
#    return data
#
# test
# movieDataToJSON('Kit Harrington')
#
#
#