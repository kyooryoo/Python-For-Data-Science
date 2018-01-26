import pandas as pd
df = pd.read_csv('./Documents/Python-For-Data-Science/sample_loan_data.csv')
df.head()
df.info()
df.describe()

# explore the data
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
df[df['credit.policy']==1]['fico'].hist(bins=35,color='blue',
  label='Credit Policy = 1',alpha=0.6)
df[df['credit.policy']==0]['fico'].hist(bins=35,color='red',
  label='Credit Policy = 0',alpha=0.6)
plt.xlabel('FICO')
plt.legend()

plt.figure(figsize=(10,6))
df[df['not.fully.paid']==1]['fico'].hist(bins=35,color='blue',
  label='Not Fully Paid = 1',alpha=0.6)
df[df['not.fully.paid']==0]['fico'].hist(bins=35,color='red',
  label='Not Fully Paid = 0',alpha=0.6)
plt.xlabel('FICO')
plt.legend()

import seaborn as sns
plt.figure(figsize=(10,6))
sns.countplot(x='purpose',data=df,hue='not.fully.paid',palette='Set1')

sns.jointplot(x='fico',y='int.rate',data=df,color='purple')

plt.figure(figsize=(10,6))
sns.lmplot(y='int.rate',x='fico',data=df,hue='credit.policy',
           col='not.fully.paid',palette='Set1')

# build the model
cat_feats = ['purpose']
final_data = pd.get_dummies(df,columns=cat_feats,drop_first=True)

from sklearn.cross_validation import train_test_split
X = final_data.drop('not.fully.paid',axis=1)
y = final_data['not.fully.paid']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                    random_state=101)

from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier()
dtc.fit(X_train,y_train)
pred_dtc = dtc.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix
print(classification_report(y_test,pred_dtc))
print(confusion_matrix(y_test,pred_dtc))

from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=300)
rfc.fit(X_train,y_train)
pred_rfc = rfc.predict(X_test)
print(classification_report(y_test,pred_rfc))
print(confusion_matrix(y_test,pred_rfc))