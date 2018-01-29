# K Means Culstering is an unsupervised learning algorithm that attempts to
# group similar clusters together. It is used for clustering similar docs,
# clustering customers based on features, segmenting market, and identifying
# similar physical groups.

# K Means Algorithm chooses a number K of clusters, then randomly assign each
# data point to a cluster, then repeat computing the cluster center by taking
# the mean vector of points in the cluster and assigning each data point to
# the cluster for which the center is the closest.

# Elbow method could be used for choosing K value. First, computing the sum
# of squared error SSE for some alternative values of K, in which the SSE is
# sum of squared distance between each member of the cluster and its center.
# Second, plot K against SSE, confirm the SSE decrease as K gets larger.
# Choose the K which makes SSE decrease abruptly, which makes the plot looks
# like an elbow in shape.

# generate some artificial data
from sklearn.datasets import make_blobs
# create some data with 200 samples, and 2 features, 4 centers, 
# 1.8 standard deviation for each cluster
data = make_blobs(n_samples=200,n_features=2,centers=4,cluster_std=1.8,
                  random_state=101)

import matplotlib.pyplot as plt
# plot the sample data with one feature against the other
# color the points with their cluster number and map them to rainbow color set
plt.scatter(data[0][:,0],data[0][:,1],c=data[1],cmap='rainbow')

# use KMeans model to fit sample data,see different n_clusters value in plot
model = []
from sklearn.cluster import KMeans
for k in range(2,7):
    model.append(KMeans(n_clusters=k))
    model[k-2].fit(data[0])
    print(k)

# confirm several characteristics of the fitted model
model[0].cluster_centers_
model[0].labels_

# plot them out to see the result with different K
fig,axes = plt.subplots(6,1,sharey=True,figsize=(6,24))
axes[0].set_title('Original')
axes[0].scatter(data[0][:,0],data[0][:,1],c=data[1],cmap='rainbow')
for k in range(2,7):
    axes[k-1].set_title('K Means (k=' + str(k) + ')')
    axes[k-1].scatter(data[0][:,0],data[0][:,1],
        c=model[k-2].labels_,cmap='rainbow')
plt.tight_layout()