# Support Vector Machines SVMs are supervised learning models with associated
# learning algorithms that analyze data and recognize patterns, used for
# classification and regression analysis by drawing lines between different
# classes. The lines are identified by instances staying at the border between
# classes, which are the support vectors of the model.

# prepare the data
from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
cancer.keys()
cancer['DESCR']
cancer['target']
cancer['target_names']
cancer['feature_names']

import pandas as pd
df_feat = pd.DataFrame(cancer['data'],columns=cancer['feature_names'])
df_feat.head()
df_feat.info()

from sklearn.cross_validation import train_test_split
X = df_feat
y = cancer['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                    random_state=101)

# build the SVC model with default settings
from sklearn.svm import SVC
model = SVC()
model.fit(X_train, y_train)
pred = model.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix
print(classification_report(y_test,pred))
print(confusion_matrix(y_test,pred))

# use grid search to find the best combination of parameters
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
