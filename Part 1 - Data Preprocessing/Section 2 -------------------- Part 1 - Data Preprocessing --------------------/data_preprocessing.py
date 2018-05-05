

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


# encoding catrgorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelEncoder_X = LabelEncoder()
X[:, 0] = labelEncoder_X.fit_transform(X[:, 0])
# witch colunm need to be catrgory
oneHotEncoder = OneHotEncoder(categorical_features = [0])
X = oneHotEncoder.fit_transform(X).toarray()