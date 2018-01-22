# Google search ISLR to get reading material and references

# Maching learning is a data analysis method for automating analytical model
# building, uses algorithms iteratively learn from data to find hidden insights
# without explicitly programmed where to look

# there are three main types of machine learning algorithms
# Supervised learning uses known labeled data to try predicting a label based
# off of known features. Unsupervised learning use unlabeled data an try to
# group together similar data points based off of the features. Reinforcement
# learning performs an action from experience.

# use scikit-learn package for learning ML with Python
# run following line of code to see if scikit-learn package is installed
from sklearn.linear_model import LinearRegression

# all data should be split into training and testing sets
# for example
import numpy as np
from sklearn.model_selection import train_test_split
x, y = np.arange(10).reshape((5,2)), range(5)
x
y
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
x_train
x_test
y_train
y_test

# after split the data we train or fit model on the training data
# while unsupervised model accepts only one argument
# model.fit(x_train, y_train)
# model.fit(x_train)


# supervised model use predict method like follows
# predictions = model.predict(x_test)
# model.predict_proba()

# classification or regression problems also have scored method
# or predict method for predicting labels in clustering algorithms
# model.score()
# model.pridict()
# return the new presentation of the input data based on the unsupervised model
# model.transform()

# some model can fit and transform the data at the same time
# model.fit_transform()

# for getting some advice about choosing algorithms google search
# scikit-learn algorithm cheat-sheet
