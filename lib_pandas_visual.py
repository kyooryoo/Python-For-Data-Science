import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df1 = pd.read_csv('df1',index_col=0)
print("the sample dataframe of df1:\n{}".format(df1.head()))
df2 = pd.read_csv('df2')
print("the sample dataframe of df2:\n{}".format(df2.head()))

# next three lines of code have the same results
df1['A'].hist(bins=20)
df1['A'].plot(kind="hist",bins=20)
df1['A'].plot.hist(bins=20)

#
df2.plot.area(alpha=0.6)

df2.plot.bar()
df2.plot.bar(stacked=True,alpha=0.6)

df1.plot.line(x=df1.index,y='B',figsize=(12,3),lw=1)

# plot a four dimentional figure, based on the coordinations of A and B
# add color of scale to reveal C further adding the size scale to reveal D
df1.plot.scatter(x='A',y='B',c='C',s=df1['D']*50)

df2.plot.box()

df = pd.DataFrame(np.random.randn(1000,2),columns=['a','b'])
df.plot.hexbin(x='a',y='b',gridsize=25,cmap="coolwarm")

df2['a'].plot.kde()
df2['a'].plot.density()
df2.plot.density()

# practice
df3 = pd.read_csv('df3')
print("summary of dataframe df3:\n{}".format(df3.info()))
print("the sample dataframe of df3:\n{}".format(df3.head()))

df3.plot.scatter(x='a',y='b',color='red',figsize=(8,2),s=35)

df3['a'].plot.hist()

# apply style sheet to plot
plt.style.use('ggplot')
df3['a'].plot.hist(bins=20,alpha=0.5)

df3[['a','b']].plot.box(color='red')

df3['d'].plot.kde(color='red',line_style=':')

df3['d'].plot.kde(color='red',ls=':',lw=5)

# put the legend out of the figure
df3.ix[0:30].plot.area(alpha=0.5)
plt.legend(loc='center left',bbox_to_anchor=(1.0,0.5))
