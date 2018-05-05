

# import files 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# import the dataset
dataset = pd.read_csv('Data.csv')

# create a matrix of features 
# 
X = dataset.iloc[:, :-1].values
# matrix of independent variables 
y = dataset.iloc[:, 3].values

# taking care of missing data 
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy= 'mean', axis = 0)
imputer = imputer.fit(X[:,1:3])
# replace the missing data
X[:, 1:3] = imputer.transform(X[:, 1:3])