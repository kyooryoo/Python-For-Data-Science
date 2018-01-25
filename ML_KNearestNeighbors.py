# K Nearest Neighbors KNN is classification algorithm with following steps:
# 1. it stores all training data
# 2. it calculates the distance from new data to all training data points
# 3. it sorts training data points by their distance from new data
# 4. it predicts from the labels of majority K closest training data points
# choosing different values of K may impact the classification result

# Pros of KNN include: it is a simple algorithm with a few parameters of K
# and distance metric, the training process of just saving the training data
# is trivial, it works with any number of classes and easy to add more data
# Cons of KNN include: there is a high prediction cost for calculating
# distances between data points which makes it worse for large data sets,
# and not good with high dimensional data that have many features, and 
# categorical features also do not work with KNN.

# a common application of KNN is classifying some classified data without 
# knowing the context of the data, which has what the columns represent is
# not known. This is also a common data scientist interview task.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(
        './Documents/Python-For-Data-Science/sample_Classified_Data',
        index_col=0)
df.head()
df.info()
df.describe()

# standardize data to facilitate the distance calculation
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(df.drop('TARGET CLASS',axis=1))
scaled_features = scaler.transform(df.drop('TARGET CLASS',axis=1))
df_features = pd.DataFrame(scaled_features,columns=df.columns[:-1])

# train the model and check the result of first round of prediction
from sklearn.cross_validation import train_test_split
X = df_features
y = df['TARGET CLASS']
X_train, X_test,y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                    random_state=101)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train,y_train)
predictions = knn.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix
print(classification_report(y_test,predictions))
print(confusion_matrix(y_test,predictions))

# iterate K value from 1 to 40 to see how the model accuracy change
error_rate = []
for i in range(1,40):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train,y_train)
    prediction_i = knn.predict(X_test)
    error_rate.append(np.mean(prediction_i != y_test))

plt.figure(figsize=(10,6))
plt.plot(range(1,40),error_rate,color='blue',linestyle='dashed',marker='o',
         markerfacecolor='red',markersize=10)
plt.title('Error Rate vs K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')

# use one of the optimized K value to get a better model
# change K value from 1 to 34 improves precision from 0.92 to 0.96
knn = KNeighborsClassifier(n_neighbors=34)
knn.fit(X_train,y_train)
predictions = knn.predict(X_test)
print(classification_report(y_test,predictions))
print(confusion_matrix(y_test,predictions))