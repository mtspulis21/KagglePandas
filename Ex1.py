import pandas as pd

#pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})

pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']}, index=['Product A', 'Product B'])

#pd.Series([1, 2, 3, 4, 5])
#pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')

# read_csv para abrir o csv na variavel
wine_reviews = pd.read_csv('S:\KAGGLE\Pandas\winemag-data-130k-v2.csv', index_col=0)
# .shape para ver o tamanho do arquivo

wine_reviews.shape

# (129971, 14)
# usar .head para ver um preview do conteuo
wine_reviews.head()

#Exercises
#1. In the cell below, create a DataFrame fruits that looks like this:
# apples 30 bananas 21

fruits = pd.DataFrame({'Apples':[30],'Bananas':[21]})

# 2. Create a dataframe fruit_sales that matches the diagram below:
# 2017 sales -> apples 35, bananas 21
# 2018 sales -> apples 41, bananas 34

fruit_sales = pd.DataFrame({'Apples':[35,41],'Bananas':[21,34]},index=['2017 Sales','2018 Sales'])
fruit_sales

# 3. Create a variable ingredients with a Series that looks like:
# Flour     4 cups
# Milk       1 cup
# Eggs     2 large
# Spam       1 can
# Name: Dinner, dtype: object
quantities =['4 cups', '1 cup', '2 large', '1 can']
items = ['Flour', 'Milk', 'Eggs','Spam']
ingredients = pd.Series(quantities, index=items, name= 'Dinner')
ingredients

# 4. Read the following csv dataset of wine reviews into a DataFrame called reviews
reviews = pd.read_csv('S:\KAGGLE\Pandas\winemag-data_first150k.csv',index_col=0)
reviews

# animals.to_csv("cows_and_goats.csv") -> Salvar csv
#In the cell below, write code to save this DataFrame to disk as a csv file with the name cows_and_goats.csv.