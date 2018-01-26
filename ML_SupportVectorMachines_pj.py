# have a look of the flowers
from IPython.display import Image
Setosa = 'http://upload.wikimedia.org/wikipedia/commons/5/56/Kosaciec_szczecinkowaty_Iris_setosa.jpg'
Versicolor = 'http://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg'
Virginica = 'http://upload.wikimedia.org/wikipedia/commons/9/9f/Iris_virginica.jpg'
Image(Setosa,width=300,height=300)
Image(Versicolor,width=300,height=300)
Image(Virginica,width=300,height=300)

import seaborn as sns
iris = sns.load_dataset('iris')
iris.head()
iris.info()
iris.describe()

sns.pairplot(iris,hue='species',palette='Dark2')

setosa = iris[iris['species']=='setosa']
sns.kdeplot(setosa['sepal_width'],setosa['sepal_length'],
            cmap='plasma',shade=True,shade_lowest=False)

from sklearn.cross_validation import train_test_split
X = iris.drop('species',axis=1)
y = iris['species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

from sklearn.svm import SVC
model = SVC()
model.fit(X_train, y_train)
pred = model.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix
print(classification_report(y_test,pred))
print(confusion_matrix(y_test,pred))

from sklearn.grid_search import GridSearchCV
param_grid = {'C':[0.1,1,10,100,1000],'gamma':[1,0.1,0.01,0.001,0.0001]}
grid = GridSearchCV(SVC(),param_grid,verbose=3)
grid.fit(X_train,y_train)
grid.best_params_
grid.best_estimator_
grid.best_score_

pred_grid = grid.predict(X_test)
print(classification_report(y_test,pred_grid))
print(confusion_matrix(y_test,pred_grid))
