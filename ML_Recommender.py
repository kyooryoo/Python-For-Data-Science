# Recommender Systems requires linear algebra at advanced level

# Most common recommender systems are Content-Based and Collaborative Filtering
# Collaborative Filtering produces recommendations based on the knowledge of
# user's attitude to items which uses the wisdom of the crowd to reccomend item
# Content-based recommender system focus on the attributes of the items and
# give recommendations based on the similarity between them.
# Collaborative Filtering is more commonly used than content-based systems as 
# it gives better results and easy to understand from implementation perspective

# Collaborative Filtering (CF) use the algorithm with ability to learn feature
# on its own. CF has two sub categories of Memory-Based CF and Model-Based CF.
# Memory-Based CF could be implemented by computing cosine similarity.
# Model-Based CF could be implemented by using Singular Value Decomposition

import pandas as pd
# read the user rating data
user = './Documents/Workspace/Python-For-Data-Science/sample_u.data'
columns_names = ['user_id','item_id','rating','timestamp']
df = pd.read_csv(user,sep='\t',names=columns_names)
df.head()

# read the movie title and id data
movie = './Documents/Workspace/Python-For-Data-Science/sample_Movie_Id_Titles'
movie_titles = pd.read_csv(movie)
movie_titles.head()

# merge the movie title with user rating data 
df = pd.merge(df,movie_titles,on='item_id')
df.head()

import seaborn as sns
sns.set_style('white')

# find the movies have the most high rating
# some movie may be rated by a few people
df.groupby('title')['rating'].mean().sort_values(ascending=False).head()

# find the movies have the most number of rating times
df.groupby('title')['rating'].count().sort_values(ascending=False).head()

# create a new dataframe with both mean of ratings and number of ratings
ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
ratings['num of ratings'] = pd.DataFrame(df.groupby('title')['rating'].count())
ratings.head()

# most movies have only one rating record as you can see from following plot
ratings['num of ratings'].hist(bins=70)
# ratings are generally normally distributed around 3
ratings['rating'].hist(bins=70)
# discover the relationship between ratings and num of ratings
sns.jointplot(x='rating',y='num of ratings',data=ratings,alpha=0.5)

# next section finds correlationship of two movies with other movies
moviemat = df.pivot_table(index='user_id',columns='title',values='rating')
moviemat.head()
ratings.sort_values('num of ratings',ascending=False).head()

starwars_user_ratings = moviemat['Star Wars (1977)']
liarliar_user_ratings = moviemat['Liar Liar (1997)']

similar_to_starwars = moviemat.corrwith(starwars_user_ratings)
similar_to_liarliar = moviemat.corrwith(liarliar_user_ratings)

corr_starwars = pd.DataFrame(similar_to_starwars,columns=['Correlation'])
corr_starwars.dropna(inplace=True)
corr_starwars.head()

# some minority movies may have high correlationship with star wars
# just because some one rated that minoriy movie also rated star wars
corr_starwars.sort_values('Correlation',ascending=False).head(10)

# so we want to filter out these minority movies with low numbers of ratings
corr_starwars = corr_starwars.join(ratings['num of ratings'])
corr_starwars.head()
corr_starwars[corr_starwars['num of ratings']>100].sort_values(
        'Correlation',ascending=False).head()

# do the same steps fo movie of liar liar to find its high correlated movies
corr_liarliar = pd.DataFrame(similar_to_liarliar,columns=['Correlation'])
corr_liarliar.dropna(inplace=True)
corr_liarliar = corr_liarliar.join(ratings['num of ratings'])
corr_liarliar[corr_liarliar['num of ratings']>100].sort_values(
        'Correlation',ascending=False).head()

# nex section builds recommender systems
# have a quick look of the unique users and movies
num_users = df.user_id.nunique()
num_movies = df.item_id.nunique()
print('Num. of users: {}'.format(num_users))
print('Num. of movies: {}'.format(num_movies))

# split the data for train and test
from sklearn.model_selection import train_test_split
train_data, test_data = train_test_split(df, test_size=0.3)

# Memory-Based CF have both user-item filtering and item-item filtering
# user-item filtering recommends items that similar users like
# item-item filtering recommends that are liked by users who like this item

# First create user-item matrix then calculate and create similarity matrix
# Similarity values in item-item CF are measured by observing all users who
# have rated both items. Similarity values between users in user-item CF are
# measured by observing all the items that are rated by both users. 

# create user-item matrices for training and testing
import numpy as np
train_data_matrix = np.zeros((num_users,num_movies))
test_data_matrix = np.zeros((num_users,num_movies))
# DataFrame.intertuples() interates over dataframe rows as named tuples
for line in train_data.itertuples():
    train_data_matrix[line[1]-1,line[2]-1] = line[3]
for line in test_data.itertuples():
    test_data_matrix[line[1]-1,line[2]-1] = line[3]

# use pairwise_distances function to calculate cosine similarity, which
# calculate the distance metric. Ratings are seen as vectors in n-dimensioinal
# space and similarity is calcualted based on the angle between the vectors.
from sklearn.metrics.pairwise import pairwise_distances
user_similarity = pairwise_distances(train_data_matrix,metric='cosine')
item_similarity = pairwise_distances(train_data_matrix.T,metric='cosine')

def predict(ratings, similarity, type='user'):
    if type == 'user':
        mean_user_rating = ratings.mean(axis=1)
        ratings_diff = (ratings - mean_user_rating[:,np.newaxis])
        pred = mean_user_rating[:,np.newaxis]+similarity.dot(
                ratings_diff)/np.array([np.abs(similarity).sum(axis=1)]).T
    elif type == 'item':
        pred = ratings.dot(similarity)/np.array(
                [np.abs(similarity).sum(axis=1)])
    return pred

item_prediction = predict(train_data_matrix,item_similarity,type='item')
user_prediction = predict(train_data_matrix,user_similarity,type='user')

# use root mean squared error to evaluate accuracy of predicted ratings
from sklearn.metrics import mean_squared_error
from math import sqrt
def rmse(prediction, ground_truth):
    prediction = prediction[ground_truth.nonzero()].flatten() 
    ground_truth = ground_truth[ground_truth.nonzero()].flatten()
    return sqrt(mean_squared_error(prediction, ground_truth))

print('User-based CF RMSE: ' + str(rmse(user_prediction, test_data_matrix)))
print('Item-based CF RMSE: ' + str(rmse(item_prediction, test_data_matrix)))

# Model-Based CF
sparsity=round(1.0-len(df)/float(num_users*num_movies),3)
print('The sparsity level of MovieLens100K is ' +  str(sparsity*100) + '%')

from scipy.sparse.linalg import svds
#get SVD components from train matrix. Choose k.
u, s, vt = svds(train_data_matrix, k = 20)
s_diag_matrix=np.diag(s)
X_pred = np.dot(np.dot(u, s_diag_matrix), vt)
print('User-based CF MSE: ' + str(rmse(X_pred, test_data_matrix)))

# Memory-Based CF does not scale to real world scenarios and does not address
# the cold start problem. Model-Based CF methods are scalable and can deal with
# higher sparsity level than Memory-Based CF, but also has cold start issue.

# extra reading material: Recommender System by Jannach and Zanker
# http://blog.ethanrosenthal.com/2015/11/02/intro-to-collaborative-filtering/