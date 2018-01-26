# decision tree have nodes that split for the value of a certain attribute and
# edges that as the outcome of a split to the next node. Root node performs 
# the first split, leaves are the terminals that predict the final outcome.

# Entropy and Information Gain are the mathematical methods of choosing the
# best features for splitting the target classes. In short we want to choose
# the features that can be sued to perfectly split the instances in data 
# in the same way as we interested or in concern with these instances 

# There is high variance in dicision tree. Different split in training data
# may lead to totally different trees. 
# For avoiding all trees use the same strong feature in a data set and become 
# highly correlated we can use Random Trees

import pandas as pd
df = pd.read_csv('./Documents/Python-For-Data-Science/sample_kyphosis.csv')
df.head()
df.info()

import seaborn as sns
sns.pairplot(df,hue='Kyphosis')

from sklearn.model_selection import train_test_split
X = df.drop('Kyphosis',axis=1)
y = df['Kyphosis']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# use decision tree model
from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier()
dtc.fit(X_train,y_train)
pred_dtc = dtc.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix
print(classification_report(y_test,pred_dtc))
print(confusion_matrix(y_test,pred_dtc))

# use random forest model
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=200)
rfc.fit(X_train,y_train)
pred_rfc = rfc.predict(X_test)
print(classification_report(y_test,pred_rfc))
print(confusion_matrix(y_test,pred_rfc))

# plotting the tree in image
# install pydot and graphviz with
# sudo apt install python-pydot python-pydot-ng graphviz
from IPython.display import Image
from sklearn.externals.six import StringIO
from sklearn.tree import export_graphviz
import pydot

features = list(df.columns[1:])
dot_data = StringIO()
export_graphviz(dtc,out_file=dot_data,feature_names=features,filled=True,
                rounded=True)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
Image(graph[0].create_png())
