# in a pair of values, predict one value from another value
# hopefully there is a linear relationship between the two values

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./Documents/Python-For-Data-Science/sample_USA_Housing.csv')

# explore the data by running the following codes line by line
df.head()
df.info()
df.describe()
df.columns
sns.pairplot(df)

# check the distribution of the target column
sns.distplot(df['Price'])

# check the full coorelation of all columns
sns.heatmap(df.corr(),cmap='RdYlBu')

# transfer columns to features list without target and irrelevant features
X1 = np.array(df.columns)
col_length = len(X1)
X1 = np.delete(X1,[col_length-2,col_length-1])

X1 = df[X1]
y1 = df['Price']
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.4, 
                                                    random_state=101)

# create a linear regression model and use the data to train it
lm1 = LinearRegression()
lm1.fit(X1_train,y1_train)

# check some characteristics of the trained model
lm1.intercept_
lm1.coef_

# create a dataframe to save the coefficient
cdf1 = pd.DataFrame(data=lm1.coef_,index=X1.columns,columns=['Coef'])

# for analyzing some real data
from sklearn.datasets import load_boston
boston = load_boston()

# explore the boston data
boston.keys()
boston['data']
boston['target']
boston['feature_names']
boston['DESCR']

# create the features data and split
X2 = boston['data']
y2 = boston['target']
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.4, 
                                                    random_state=101)

# train the model and show the coefficient
lm2 = LinearRegression()
lm2.fit(X2_train,y2_train)
index = boston['feature_names']
cdf2 = pd.DataFrame(data=lm2.coef_,index=index,columns=['Coef'])

# consume the trained model to predict features
predictions1 = lm1.predict(X1_test)

# plot the result
plt.scatter(y1_test,predictions1)
sns.distplot((y1_test - predictions1))

# calculate the MAE, MSE and RMSE for evaluating the model
from sklearn import metrics
print('MAE: ', metrics.mean_absolute_error(y1_test, predictions1))
print('MSE: ', metrics.mean_squared_error(y1_test, predictions1))
print('RMSE: ', np.sqrt(metrics.mean_squared_error(y1_test, predictions1)))

# do the same thing on boston data set and model
predictions2 = lm2.predict(X2_test)
plt.scatter(y2_test,predictions2)
sns.distplot((y2_test - predictions2))

from sklearn import metrics
print('MAE: ', metrics.mean_absolute_error(y2_test, predictions2))
print('MSE: ', metrics.mean_squared_error(y2_test, predictions2))
print('RMSE: ', np.sqrt(metrics.mean_squared_error(y2_test, predictions2)))