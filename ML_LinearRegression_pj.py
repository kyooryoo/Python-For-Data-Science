from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Get the data
customers = pd.read_csv(
        './Documents/Python-For-Data-Science/sample_EcommerceCustomers')

customers.head()
customers.describe()
customers.info()

# Exploratory data analysis
sns.jointplot(x='Time on Website',
              y='Yearly Amount Spent',
              data=customers)

sns.jointplot(x='Time on App',
              y='Yearly Amount Spent',
              data=customers)

sns.jointplot(x='Time on App',
              y='Length of Membership',
              data=customers,
              kind='hex')

sns.pairplot(customers)

sns.lmplot(x='Length of Membership',
           y='Yearly Amount Spent',
           data=customers)

# Training and testing data
X = customers[np.delete(np.array(customers.columns),[0,1,2,7])]
y = customers['Yearly Amount Spent']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                    random_state=101)

lm = LinearRegression()
lm.fit(X_train,y_train)
lm.coef_

predictions = lm.predict(X_test)
plt.scatter(y=predictions,x=y_test)
plt.xlabel('Y test')
plt.ylabel('Predictions')

from sklearn import metrics
print('MAE: ', metrics.mean_absolute_error(y_test, predictions))
print('MSE: ', metrics.mean_squared_error(y_test, predictions))
print('RMSE: ', np.sqrt(metrics.mean_squared_error(y_test, predictions)))

sns.distplot((y_test-predictions),bins=50)

index = np.delete(np.array(customers.columns),[0,1,2,7])
pd.DataFrame(data=lm.coef_,index=index,columns=['Coeffecient'])