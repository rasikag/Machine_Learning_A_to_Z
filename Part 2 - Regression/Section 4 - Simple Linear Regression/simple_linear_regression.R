# Simple Linear Regression 

# Import the dataset 
dataset = read.csv('Salary_Data.csv')

# Create subset of data set 
#dataset = dataset[, 2:3]

# Splitting the dataset into the Training set and Test set

#install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature Scaling 
# training_set[, 2:3] = scale(training_set[, 2:3])
# test_set[, 2:3] = scale(training_set[, 2:3])

# Fitting simple linear regression to the traing set
regressor = lm(formula = Salary ~ YearsExperience,
               data = training_set)

# summary(regressor)
y_pred = predict(regressor, newdata = test_set)


