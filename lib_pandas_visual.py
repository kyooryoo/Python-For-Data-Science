import numpy as np
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

















df1 = pd.read_csv('df1',index_col=0)
print("the sample dataframe of df1:\n{}".format(df1.head()))