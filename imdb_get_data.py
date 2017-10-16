# -*- coding: utf-8 -*-
"""
Spyder Editor

Person IMDB data collector.

"""
import datetime
from imdb import IMDb

roles = [
        'stunts', 
        'sound department', 
        'producer', 
        'self', 
        'writer',
        'actor',
        'director',
        'in development', 
        'miscellaneous crew'
        ]

print_on = True
ia = IMDb()

def searchPersonIdByName(personName):
    if print_on:
        print 'a search_person \'%s\' %s' % (personName, datetime.datetime.now())

    persons = ia.search_person(personName)
    firstPerson = persons[0]

    if print_on:
        print firstPerson.summary()
    
    if print_on:
        print 'b search_person \'%s\' %s' % (personName, datetime.datetime.now())
    
    return firstPerson.personID

def getPerson(personId):
    if print_on:
        print 'a get_person: \'%s\' %s' % (personId, datetime.datetime.now())

    person = ia.get_person(personId)
    
    if print_on:
        print person.summary()
    
    if print_on:
        print 'b get_person: \'%s\' %s' % (personId, datetime.datetime.now())
    
    return person

def getMovieIdsByRole(person, role):
    if print_on:
        print 'a person: \'%s\' \'%s\' %s' % (role, person['birth name'], datetime.datetime.now())

    movieIds = []

    if role in person.keys():
        moviesInRole = person[role]
        for movie in moviesInRole:
            movieIds.append(movie.movieID)
    
    if print_on:
        print 'b person: \'%s\' \'%s\' %s' % (role, person['birth name'], datetime.datetime.now())
    
    return movieIds

def getMoviesByMovieIds(movieIds):
    if print_on:
        print 'a movies: \'%s\' %s' % (len(movieIds), datetime.datetime.now())

    movies = []

    for movieId in movieIds:
        if print_on:
            print 'a get_movie : \'%s\' %s' % (movieId, datetime.datetime.now())
        movies.append(ia.get_movie(movieId))
        if print_on:
            print 'b get_movie : \'%s\' %s' % (movieId, datetime.datetime.now())

    if print_on:
        print 'b movies: \'%s\' %s' % (len(movieIds), datetime.datetime.now())
    
    return movies

# to test search by person name --> get personId
personId = searchPersonIdByName("Roger Corman")

# to test person data --> get Person object
person = getPerson(personId)

# to test movieid listings per 'role' --> get dict (role, list-of-movie-ids)
movieIdsInRole = {}
for role in roles:
    movieIdsInRole[role] = getMovieIdsByRole(person, role)
    if print_on:
        print '#movies ', len(movieIdsInRole[role]), role
if print_on:
    print len(movieIdsInRole)

# to test movies for role --> list of Movie objects
writer_movies = getMoviesByMovieIds(movieIdsInRole.get('writer'))
if print_on:
    for movie in writer_movies:
        print movie.summary()
    print vars(movie)
# to show that update adds more information to movie, 
# big question is what sets are there that can be updated, 
# which are we interested in??
    ia.update(movie, 'business')
    print vars(movie)

# just to mention, person can have pseudonames, should we search them as well?    
if print_on:
    print person['akas']

#if print_on:
#    print 'a get_person: %s' % datetime.datetime.now()

#print vars(director)
#print "##################################################"
#print director['director']
#print "##################################################"
#print director['producer']
#if print_on:
#    print 'b get_person: %s' % datetime.datetime.now()
#
#counter = 0
#total = 0
#average = 0
#
#if print_on:
#    print 'a for-i-in-director: %s' % datetime.datetime.now()

#for i in director['director']:
#
#    if print_on:
#        print i.movieID + ' a get_movie: %s' % datetime.datetime.now()
#    
#    movie = ia.get_movie(i.movieID)
#
#    if print_on:    
#        print i.movieID + ' d get_movie: %s' % datetime.datetime.now()
#
#    total += movie['rating']
#
#    if print_on:
#        print i.movieID + ' c get_movie: %s' % datetime.datetime.now()
#
#    counter += 1
#
#
#print 'b for-i-in-director: %s' % datetime.datetime.now()
#    
#if counter > 0:
#    average = total / counter
#    
#print average
#print counter