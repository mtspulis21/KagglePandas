import pandas as pd
pd.set_option('display.max_rows', 5)
import numpy as np

# read_csv para abrir o csv na variavel
# wine_
reviews = pd.read_csv('S:\KAGGLE\Pandas\winemag-data-130k-v2.csv', index_col=0)

# reviews = pd.read_csv('S:\KAGGLE\Pandas\winemag-data_first150k.csv',index_col=0)


##########################################################################################

# agrupar por pontos e contar quantos em cada ponto
reviews.groupby('points').points.count()

# agrupar por 'winery' e mostrar o primeiro de cada iloc[0]
reviews.groupby('winery').apply(lambda df: df.title.iloc[0])

# For even more fine-grained control, you can also group by more than one column.
# For an example, here's how we would pick out the best wine by country and province:

reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])
reviews.groupby(['country']).price.agg([len, min, max])

# Multi-indexes
countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
countries_reviewed

mi = countries_reviewed.index
type(mi)

# reseta o index e tira a dupla criando uma linha pra cada
countries_reviewed.reset_index()

# sorting by len
countries_reviewed = countries_reviewed.reset_index()
countries_reviewed.sort_values(by='len')

# (by='len', ascending=False) # ordem do maior pro menor

# double sort
countries_reviewed.sort_values(by=['country', 'len'])

# reate a Series whose index is the taster_twitter_handle category from the dataset, 
# and whose values count how many reviews each person wrote

reviews_written = reviews.groupby('taster_twitter_handle').size()

# or

# reviews.groupby('taster_twitter_handle').taster_twitter_handle.count()

# What is the best wine I can buy for a given amount of money? 
# Create a Series whose index is wine prices and whose values is the maximum number of 
# points a wine costing that much was given in a review. Sort the values by price, 
# ascending (so that 4.0 dollars is at the top and 3300.0 dollars is at the bottom).
reviews.head()

best_rating_per_price = reviews.groupby('price')['points'].max().sort_index()
best_rating_per_price

# What are the minimum and maximum prices for each variety of wine?
# Create a DataFrame whose index is the variety category from the dataset and
# whose values are the min and max values thereof

prices_extremes = reviews.groupby('variety').price.agg([min,max])

# What are the most expensive wine varieties? 
# Create a variable sorted_varieties containing a copy 
# of the dataframe from the previous question where vrieties are sorted in descending
# order based on minimum price, then on maximum price (to break ties)

sorted_varieties = prices_extremes.sort_values(by=['min', 'max'],ascending=False)
sorted_varieties

# Create a Series whose index is reviewers and whose values is the average review
# score given out by that reviewer. Hint: you will need the taster_name and points columns.

reviewer_mean_ratings = reviews.groupby('taster_name').points.mean()

# What combination of countries and varieties are most common? 
# Create a Series whose index is a MultiIndexof {country, variety} pairs. 
# For example, a pinot noir produced in the US should map to {"US", "Pinot Noir"}. 
# Sort the values in the Series in descending order based on wine count.

country_variety_counts = reviews.groupby(['country','variety']).size().sort_values(ascending=False)
country_variety_counts
