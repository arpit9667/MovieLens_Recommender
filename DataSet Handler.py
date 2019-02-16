import numpy as np
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'notebook')
column_names = ['user_id', 'item_id', 'rating', 'timestamp']
df = pd.read_csv('u.data', sep='\t', names=column_names)

print(df.head())
movie_titles = pd.read_csv('Movie_Id_Titles')
movie_titles.head()

# merge dataset

df = pd.merge(df, movie_titles, on='item_id')
print(df.head())

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')

# create a ratings dataframe with average rating and number of ratings:¶
df.groupby('title')['rating'].mean().sort_values(ascending=False).head(10)
df.groupby('title')['rating'].count().sort_values(ascending=False).head(10)
ratings =pd.DataFrame(df.groupby('title')['rating'].mean())
print(ratings.head())

# Set the number of ratings column:
ratings['rating_numbers'] = pd.DataFrame(df.groupby('title')['rating'].count())
print(ratings.head())

# Number of ratings histogram
ratings['rating_numbers'].hist(bins=70)

# Average rating per movie histogram
ratings['rating'].hist(bins=70)


# Relationship between the average rating and the actual number of ratings
# The larger the number of ratings, the more likely the rating of a movie is
sns.jointplot(x='rating', y='rating_numbers', data=ratings, alpha=0.5)


# ## Recommending Similar Movies

# Let's create a matrix that has the user ids on one access and the movie title on another axis. Each cell will then consist of the rating the user gave to that movie. The NaN values are due to most people not having seen most of the movies.

moviemat = df.pivot_table(index='user_id', columns='title', values='rating')
print(moviemat.head())


# ##### Most rated movies
ratings.sort_values('rating_numbers', ascending=False).head(10)


# #### Let's choose two movies for our system: Starwars, a sci-fi movie. And Liar Liar, a comedy.

# What are the user ratings for those two movies?
starwars_user_ratings = moviemat['Star Wars (1977)']
liar_liar_user_ratings =moviemat['Liar Liar (1997)']
print(starwars_user_ratings.head())




