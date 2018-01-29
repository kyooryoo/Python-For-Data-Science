# import sample data
import pandas as pd

data_addr = './Documents/Workspace/Python-For-Data-Science/sample_College_Data'
data = pd.read_csv(data_addr,index_col=0)
data.head()
data.info()
data.describe()

# explore the data
import seaborn as sns
import matplotlib.pyplot as plt

sns.lmplot(x='Room.Board',y='Grad.Rate',data=data,hue='Private',fit_reg=False,
           palette='coolwarm',size=6,aspect=1)

sns.lmplot(x='Outstate',y='F.Undergrad',data=data,hue='Private',fit_reg=False,
           palette='coolwarm',size=6,aspect=1)

g = sns.FacetGrid(data,hue='Private',palette='coolwarm',size=4,aspect=2)
g = g.map(plt.hist,'Outstate',bins=20,alpha=0.7)

g = sns.FacetGrid(data,hue='Private',palette='coolwarm',size=4,aspect=2)
g = g.map(plt.hist,'Grad.Rate',bins=20,alpha=0.7)

# find the college which has grad rate with invalid value and fix it
data[data['Grad.Rate']>100]
data['Grad.Rate']['Cazenovia College'] = 100

# confirm the grad rate of all colleges are valid
g = sns.FacetGrid(data,hue='Private',palette='coolwarm',size=4,aspect=2)
g = g.map(plt.hist,'Grad.Rate',bins=20,alpha=0.7)

# build the model
from sklearn.cluster import KMeans

model = KMeans(n_clusters=2)
model.fit(data.drop('Private',axis=1))

model.cluster_centers_

# evaluate the model with known cluster info
def map_cluster(private):
    if private == 'Yes':
        return 1
    else:
        return 0
data['Cluster'] = data['Private'].apply(map_cluster)
data.head()

from sklearn.metrics import confusion_matrix, classification_report
print(confusion_matrix(data['Cluster'],model.labels_))
print(classification_report(data['Cluster'],model.labels_))