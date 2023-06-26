import pandas as pd
pd.set_option('display.max_rows', 5)
import numpy as np

# read_csv para abrir o csv na variavel
# wine_
reviews = pd.read_csv('S:\KAGGLE\Pandas\winemag-data-130k-v2.csv', index_col=0)

# reviews = pd.read_csv('S:\KAGGLE\Pandas\winemag-data_first150k.csv',index_col=0)

# region_1 and region_2 are pretty uninformative names for locale columns in the dataset.
# Create a copy of reviews with these columns renamed to region and locale, respectively.

renamed_reviews = reviews.rename(columns={'region_1' : 'region', 'region_2' : 'locale'})

# Set the index name in the dataset to wines.

reindexed = reviews.rename_axis('wines', axis='columns')

# The Things on Reddit dataset includes product links from a selection of top-ranked forums 
# ("subreddits") on reddit.com. Run the cell below to load a dataframe of
# products mentioned on the /r/gaming subreddit and another dataframe for products 
# mentioned on the r//movies subreddit.

gaming_products = pd.read_csv("../input/things-on-reddit/top-things/top-things/reddits/g/gaming.csv")
gaming_products['subreddit'] = "r/gaming"
movie_products = pd.read_csv("../input/things-on-reddit/top-things/top-things/reddits/m/movies.csv")
movie_products['subreddit'] = "r/movies"

combined_products = pd.concat([gaming_products,movie_products])

# The Powerlifting Database dataset on Kaggle includes one CSV table 
# for powerlifting meets and a separate one for powerlifting competitors.
# Run the cell below to load these datasets into dataframes:

powerlifting_meets = pd.read_csv("../input/powerlifting-database/meets.csv")
powerlifting_competitors = pd.read_csv("../input/powerlifting-database/openpowerlifting.csv")

powerlifting_combined = powerlifting_meets.set_index(['MeetID']).join(powerlifting_competitors.set_index('MeetID'))

