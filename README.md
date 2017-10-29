# moviepredictor

Movie predictor. For given person, (actor, director or producer name) the program downloads dataset from IMDB and shows his or her movie history. From the output one can see persons most favorable movie genre, succesfulness of the person e.t.c. Then with this dataset the program predicts the next movie where this person is taking part. Prediction includes movie title, plot keywords, when the movie is coming out and the succesfulness of the movie.

*How does it work:
1. csv_writer.py downloads the dataset for the given perosn from imdb and writes a csv file from it
2. csv_data_parser.py creates new csv file from the raw_data: Newly created file is easier to read and utilize for visualization and data analysis.
3. facts.py (or facts.ipynb) visualizes the data and also uses some machine learning to predict some of the missing values from the raw data.

Note:
The IMDbPy library which downloads the data from imdb works quite slow, that's why there are some readymade files you can check out.

This was Introduction to data science -course project. Project is still a bit unfinished since either the project had too little time or we chose too big subject.
