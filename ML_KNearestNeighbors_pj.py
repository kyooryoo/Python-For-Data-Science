# import data
import pandas as pd
df = pd.read_csv(
        './Documents/Python-For-Data-Science/sample_KNN_Project_Data')
df.head()

# pre processing data to standardize values
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(df.drop('TARGET CLASS',axis=1))
scaled_features = scaler.transform(df.drop('TARGET CLASS',axis=1))
df_features = pd.DataFrame(scaled_features,columns=df.columns[:-1])

# train the knn model and predict for the first time
from sklearn.cross_validation import train_test_split
X = df_features
y = df['TARGET CLASS']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                    random_state=101)
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train,y_train)
predictions = knn.predict(X_test)

# check the result of the first prediction
from sklearn.metrics import confusion_matrix, classification_report
print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))

# iterate K values to find possibility for better precision
import numpy as np
error_rate = []
for i in range(1,40):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train,y_train)
    predictions_i = knn.predict(X_test)
    error_rate.append(np.mean(y_test != predictions_i))

import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
plt.plot(range(1,40),error_rate)
plt.title('Error Rate vs K value')
plt.xlabel('K Value')
plt.ylabel('Error Rate')

# use the discovered K value to improve the model accuracy
knn = KNeighborsClassifier(n_neighbors=31)
knn.fit(X_train,y_train)
predictions = knn.predict(X_test)
print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))

# model precision improved from 0.72 to 0.84 with K from 1 to 31