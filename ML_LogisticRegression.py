# use bias variance trade off to evaluate model performance
# bias means how much the result is different from right result
# variance means how much the results are distributed or clustered

# a too simple model have high error in both training and testing data
# a too complex model have low error in training data but high in test data

# in practice we trade off low variance for low bias which means we add more
# noice to the training data to get a less overfitting model, so that the model
# has it predicted result with more variance but less bias from right results

# logistic regression is a method for classification results between Y/N
# Sigmoid function 1/(1+e^(-z)) is used for logistic regression model
# the linear model of y=b0+b1*x could be used for replacing z in Sigmoid fun

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

train = pd.read_csv(
        './Documents/Python-For-Data-Science/sample_titanic_train.csv')

train.head()
train.info()

# reveal the null values in the data frame
sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')

# style the plot with some grid
sns.set_style('whitegrid')

# find the survived vs unsurvived ratio and their gender detail
sns.countplot(x='Survived',hue='Sex',data=train)

# find the class detail and difference between of survived and unsurvived
sns.countplot(x='Survived',hue='Pclass',data=train)

# find the age distribution of the passengers
sns.distplot(train['Age'].dropna(),kde=False,bins=30)

# use pandas default plotting to show the age distribution
train['Age'].plot.hist(bins=30)

# find the sibling information of passengers
sns.countplot(x='SibSp',data=train)

# find the fare distribution of the passengers
train['Fare'].plot.hist(bins=40,figsize=(12,4))

# no sure it is necessary to have following two lines of code
# uncomment these lines if any problem happens during plotting
# import cufflinks as cf
# cf.go_offline()

# use interactive plot to show the fare distribution
from plotly.offline import plot
import plotly.graph_objs as go

plot([go.Histogram(x=train['Fare'],nbinsx=30)])

# explore the age data for filling the absent age data
sns.boxplot(x='Pclass',y='Age',data=train)
# so we can find the average age are about 37,29 and 33

# define a function to impute the age for missing age data
def impute_age(cols):
    Age = cols[0]
    Pclass = cols[1]
    
    if pd.isnull(Age):
        if Pclass==1:
            return 37
        elif Pclass==2:
            return 29
        else:
            return 24
    else:
        return Age

# apply the function to fill up missing age data
train['Age'] = train[['Age','Pclass']].apply(impute_age,axis=1)
# check the age data are filled
sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')

# for the column of Cabin with too many missing data, drop it
train.drop('Cabin',axis=1,inplace=True)
# check the Cabin column is dropped
sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')

# from heatmap seems like no null data, but check will still find null data
for col in train.columns:
    print('the column of {} has missing data:\n{}\n'
          .format(col,train.isnull()[col].value_counts()))

# drop the two incomplete records of data
train.dropna(inplace=True)

# convert categorical variables into dummies or indicated variables
sex = pd.get_dummies(train['Sex'],drop_first=True)
embark = pd.get_dummies(train['Embarked'],drop_first=True)
train = pd.concat([train,sex,embark],axis=1)
train.drop(['Sex','Embarked','Name','Ticket'],axis=1,inplace=True)
train.drop(['PassengerId'],axis=1,inplace=True)

# train and test the model to predict survived column
X = train.drop('Survived',axis=1)
y = train['Survived']

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3,
                                                    random_state=101)

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(X_train, y_train)

predictions = lr.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix
print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))