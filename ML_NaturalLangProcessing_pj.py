# this project classify Yelp reviews into 1 to 5 stars of categories based off
# the text content in reviews. Review contains review content in text, a rate
# value between 1 and 5 for stars, and cool, useful, and funny value for the
# feedback to this review itself from other reviewers.

import pandas as pd
file = './Documents/Workspace/Python-For-Data-Science/sample_yelp.csv'
yelp = pd.read_csv(file)
yelp.head()
yelp.describe()
yelp.info()

# create a new column which has the number of words in the text column
yelp['text_length'] = yelp['text'].apply(len)

import seaborn as sns
import matplotlib.pyplot as plt

# create a grid of 5 histograms of the text length based on the star ratings
g = sns.FacetGrid(yelp,col='stars')
g = g.map(plt.hist,'text_length')

# create a boxplot of text length for each star category
sns.boxplot(x='stars',y='text_length',data=yelp,palette='rainbow')

# create a countplot of the number of occurrences for each star category
sns.countplot(data=yelp,x='stars',palette='rainbow')

# get the mean values of the numerical columns
yelp.groupby('stars').mean()

# use corr() method on the groupby dataframe
yelp.drop('stars',axis=1).corr()

# create a heatmap based on the correlation dataframe
sns.heatmap(yelp.drop('stars',axis=1).corr(),cmap='coolwarm',annot=True)

# create a dataframe which contains only the 1 and 5 star reviews
yelp_class = yelp[(yelp['stars']==1) | (yelp['stars']==5)]
# prepare feature and target data with text and stars columns
X = yelp_class['text']
y = yelp_class['stars']

# create CountVectorizer object and fit data into its fit transform method
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
X = cv.fit_transform(X)

# prepare the train and test data
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,
                                                 random_state=101)

# train the multinomial NB model
from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()
nb.fit(X_train,y_train)

# predict and evaluate model
predictions = nb.predict(X_test)
from sklearn.metrics import confusion_matrix,classification_report
print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))

# use text processing with tf-idf
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
pipe = Pipeline([('bow',CountVectorizer()),
                 ('tfidf',TfidfTransformer()),
                 ('model',MultinomialNB())])
X = yelp_class['text']
y = yelp_class['stars']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,
                                                 random_state=101)
pipe.fit(X_train,y_train)
predictions = pipe.predict(X_test)
print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))
# form the result you can find that tf-idf some