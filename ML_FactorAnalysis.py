# Principal Component Analysis is an unsupervised statistical technique used
# to examine the interrelation among a set of variables in order to identify
# the underlying structure of them, also known as general factor analysis.

# On contrast to regression determines a line of best fit to a data set,
# factor analysis determines several orthogonal lines of best fit to the data
# set. Orthogonal means at right angles, which are perpendicular to each other
# in n-dimensional space. The n-dimensional space is the variable sample space
# which has its number of dimentions equal to number of varialbes or features.

# in a 2d plot of two variables, a regression line and a orthogonal line form
# the components for PCA. Components are a linear transformation that choose
# a variable system from the data set so that the greatest variance of the data
# set lies on the first axis, the regression line. And the second greatest
# variance lies on the second axis, the orthogonal line. Components are 
# uncorrelated as in the sample space they are orthogonal to each other. 
# This analysis could continue into higher dimensions.

# This process reduces the number of variables used in an analysis. For data
# set with a large number of variables, the amount of explained variation could
# be compressed into just a few components. The most challenging part of PCA is
# interpreting the components.

from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
cancer.keys()
# dict_keys(['data', 'target', 'target_names', 'DESCR', 'feature_names'])
print(cancer['DESCR'])

import pandas as pd
df = pd.DataFrame(cancer['data'],columns=cancer['feature_names'])
df.head()
cancer['target']
cancer['target_names']

# use PCA to compress 30 variables into 2 components and plot them
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(df)
scaled_data = scaler.transform(df)

from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca.fit(scaled_data)
x_pca = pca.transform(scaled_data)

# check that 30 variables are compressed to 2 components
scaled_data.shape
x_pca.shape

import matplotlib.pyplot as plt
plt.figure(figsize=(8,6))
plt.scatter(x_pca[:,0],x_pca[:,1],c=cancer['target'],cmap='plasma')
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')

# components are saved as attributes of a PCA object
import seaborn as sns
# check the components attributes
pca.components_
# make the components more readable
df_comp = pd.DataFrame(pca.components_,columns=cancer['feature_names'])
# check the content of the components
df_comp
plt.figure(figsize=(12,6))
sns.heatmap(df_comp,cmap='plasma')

# Logistical regression or support vector machine methods could be applied to
# the components. And 3d plot or 4d plot of colorful 3d plot could be used for
# plotting PCA objects with more than 2 components.