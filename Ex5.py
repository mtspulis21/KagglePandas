import pandas as pd
pd.set_option('display.max_rows', 5)
import numpy as np

# read_csv para abrir o csv na variavel
# wine_
reviews = pd.read_csv('S:\KAGGLE\Pandas\winemag-data-130k-v2.csv', index_col=0)

# reviews = pd.read_csv('S:\KAGGLE\Pandas\winemag-data_first150k.csv',index_col=0)


##########################################################################################

reviews[pd.isnull(reviews.country)]

reviews.region_2.fillna("Unknown")

reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino")

# What is the data type of the points column in the dataset?

dtype = reviews.points.dtype

# Create a Series from entries in the points column,
# but convert the entries to strings. Hint: strings are str in native Python.

point_strings = reviews.points.astype(str)

# Sometimes the price column is null. How many reviews in the dataset are missing a price?
n_missing_prices = pd.isnull(reviews.price).sum()

# What are the most common wine-producing regions? 
# Create a Series counting the number of times each value occurs in the region_1 field. 
# This field is often missing data, so replace missing values with Unknown. 
# Sort in descending order. Your output should look something like this:

reviews.region_1.fillna('Unknown')
reviews.region_1.value_counts()
reviews.sort_values(ascending=False)

reviews.region_1.fillna('Unknown').value_counts().sort_values(ascending=False)
