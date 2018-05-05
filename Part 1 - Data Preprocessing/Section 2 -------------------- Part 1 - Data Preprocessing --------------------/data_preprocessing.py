

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