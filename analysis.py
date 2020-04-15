

# Load the Pandas Libraries with the alias of pd
import pandas as pd
from pandas import DataFrame

# Load the NumPy Libraries with the alias of np
import numpy as np
from numpy import array

# Load sklearn 
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
#from sklearn.externals import joblib
from sklearn.datasets import load_iris 
iris_dataset = load_iris()
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# statistical data visualization 
import seaborn as sns
import matplotlib.pyplot as plt


#When using the below code to view the data will work but wont have headings See the with open section for the update. 
#Update on this is that I had to add a line naming the columns. See line 11 
'''
# Load the CSV file
f = pd.read_csv("c:/Users/chimezie/Desktop/Iris_Dataset.csv")
f.columns = ['sepal_length', 'sepal_width' , 'petal_length', 'petal_width', 'species']  Refereance : (DataFrame, Protopopov and Joshi, 2019)
# Print the contents of the CSV file
print(f)
'''


# Open the CSV file and call is ds. We also will add headings to each column and print the results. 
with open ("c:/Users/chimezie/Desktop/Iris_Dataset.csv") as ds: 
    cols = ["Sepal Length", "Sepal Width" , "Petal Length", "Petal Width", "Species"]
    data = pd.read_csv(ds, names=cols)
print(data)
print("\n")


# Print the number of rows in the dataset.
print(data["Species"].count)
print("\n")


# Display the amount of rows and columns in the set
print(data.shape)
print("\n")


# What are the column names in the set
print(data.columns)
print("\n")


print(type(data))
print("\n")


# Print the first 10 rows
print(data.head(10))
print("\n")


'''
# Just like the finding rows from the beginning, we can also find rows from the end
print(data.tail(10))
'''


# Print the unique values of the data set and display the number of rows that belong to each
data['Species'].unique()
print(data.groupby('Species').size())
print("\n")


# Summary of each attribute
print(data.describe())
print("\n")


# Below commented out code does the same as the above describe command but is not visually a good option for all of them together.
'''
print(data.min())
print(data.max())
print(data.median())
print(data.mean())
print(data.std())
'''


# Output n number of random rows from the set
print(data.sample(5))
print("\n")


# Find if the set has any null values. 
print(data.isnull())
print("\n")


# Find if the set has any null values that are grouped.
print(data.isnull().sum())
print("\n")