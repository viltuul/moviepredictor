#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 18:59:33 2017

@author: ittobor
"""

import imdb_get_data as igd


personName = "Anne Sellors"
person = igd.getPerson(igd.searchPersonIdByName(personName))
for role in igd.roles:
    movieIdsInRole = igd.getMovieIdsByRole(person, role)
    
    for infset in igd.infsets_movie:
        movies = igd.getMovieInfsetsByMovieIds(movieIdsInRole, infset)
        
        for movie in movies:
            with open("movies/" + movie.movieID + "_" + personName + "_" + role + "_" + infset + ".txt", "w") as outfile:
                outfile.write(str(vars(movie)))
