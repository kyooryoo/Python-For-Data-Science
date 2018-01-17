# plotly is an interactive visualization library
# cufflinks connects plotly with pandas

# plotly and cufflinks are not installed in Anaconda, 
# pip install plotly and cufflinks to install them

# following lines of code should be executed in Jupyter Notebook

import pandas as pd
import numpy as np
import cufflinks as cf
# comment in the following line to show figures in Jupyter Notebook
# %matplotlib inline

from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

init_notebook_mode(connected=True)
cf.go_offline()

# prepare some sample dataframes
df1 = pd.DataFrame(np.random.randn(100,4),columns='A B C D'.split())
df2 = pd.DataFrame({'Category':['A','B','C'],'Values':[32,43,50]})
df3 = pd.DataFrame({'x':[1,2,3,4,5],'y':[10,20,30,20,10],'z':[5,4,3,2,1]})

# iplot is used for Jupyter Notebook with special args definition
# as the equivalent of iplot, plot has different args
df1.iplot(kind='scatter',x='A',y='B',mode='markers',size=10)
df1.plot(kind='scatter',x='A',y='B')

df2.iplot(kind='bar',x='Category',y='Values')

# count function here could be other aggregation functions such as sum
df1.count().iplot(kind='bar')

df1.iplot(kind='box')

df3.iplot(kind='surface',colorscale='rdylbu')

df1[['A','B']].iplot(kind='spread')

df1['A'].iplot(kind='hist',bins=25)

df1.iplot(kind='bubble',x='A',y='B',size='C')

# similar to seaborn pairplot
df1.scatter_matrix()

# resource
# https://plot.ly/
# https://github.com/santosjorge/cufflinks