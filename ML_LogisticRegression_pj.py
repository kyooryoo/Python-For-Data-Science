import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(
        './Documents/Python-For-Data-Science/sample_advertising.csv')

data.head()
data.info()
data.describe()

plt.hist(data['Age'],bins=30)
data['Age'].plot.hist(bins=30)
sns.jointplot(x='Age',y='Area Income',data=data)
sns.jointplot(y='Daily Time Spent on Site',x='Age',data=data,kind='kde')
sns.jointplot(x='Daily Time Spent on Site',y='Daily Internet Usage',data=data)
sns.pairplot(data,hue='Clicked on Ad')

# confirm the data does not contain null value - visually
sns.heatmap(data.isnull())
# confir them data does not contain null value - by data
for col in data.columns:
    print(data[col].isnull().unique())

X = data.drop(['Clicked on Ad','Ad Topic Line','City','Country','Timestamp'],
              axis=1)
y = data['Clicked on Ad']

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

plt.plot(x=y_test,y=predictions)
sns.distplot((y_test-predictions))