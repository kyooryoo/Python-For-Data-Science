import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)
# pd.DataFrame take paras of input data, then row and column name
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print("a dataframe:\n{}".format(df))
# a column could be easily retrieved from a dataframe
print("the 'W' column of the df:\n{}".format(df['W']))
print("a column of dataframe is a series with data type of:\n{}"
      .format(type(df['W'])))
print("a dataframe has the data type of:\n{}".format(type(df)))
print("retrieve several columns by passing a list of column names:\n{}"
      .format(df[['W','Z']]))
df['new'] = df['W'] + df['Z']
print("added a new column with combined value of column 'W' and 'Z' is:\n{}"
      .format(df))
# for deleting a column from dataframe use df.drop() with axis set to 1
# this returns a new modified dataframe by default but not happens in place
print("after dropping the new column 'new':\n{}"
      .format(df.drop('new',axis=1)))
print("but it happens not inplace, so df is still:\n{}".format(df))
# for making it happens inplace on the df, use inplace=True argument
df.drop('new',axis=1,inplace=True)
print("now this drop happens inplace, df becomes:\n{}".format(df))
# shape attribute returns the description of the dataframe's shape
# it is a tuple with first value for row and second value for column
print("the df has {} rows and {} columns".format(df.shape[0],df.shape[1]))
# use loc[] to get sections from a dataframe, first para specify rows
# second specify columns, both could be list for multy selection
print("the A row of the df datafram is:\n{}".format(df.loc['A']))
print("the A and D row of df dataframe are:\n{}".format(df.loc[['A','D']]))
print("use index of rows to select the same:\n{}".format(df.iloc[[0,3]]))
print("the element on row C and column Y: {}".format(df.loc['C','Y']))
print("a section of the df with rows of CD and columns of XYZ:\n{}"
      .format(df.loc[['C','D'],['X','Y','Z']]))

# for conditional selection of a dataframe, use boolean dataframe
booldf = df > 0
print("a boolean dataframe of df > 0 is:\n{}".format(booldf))
print("use the boolean dataframe to filter df can get:\n{}"
      .format(df[booldf]))
# for partially filter by some condition on a few columns
print("clean out record with minus value on column W:\n{}"
      .format(df[df['W']>0]))
print("more complexed selection could be df[df['W']>0][['X','Z']]:\n{}"
      .format(df[df['W']>0][['X','Z']]))
print("or combined conditions such as df[(df['W']>0)&(df['Y']>0)]:\n{}"
      .format(df[(df['W']>0)&(df['Y']>0)][['X','Z']]))

# index could be reset by using reset_index method
print("the dataframe after reseting index is:\n{}".format(df.reset_index()))
# following steps reset index with a list
newindex = 'US CN JP SG FR'.split() # prepare a list
df['Country'] = newindex # add list to df as a new column
print("now the dataframe with new column is:\n{}".format(df))
print("set Country column as index:\n{}".format(df.set_index('Country')))
# the set_index method will replace existing index and cause info lost

# index could have levels
outside = ['G1','G1','G1','G2','G2','G2']
inside= [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
print("levels of index:\n{}".format(hier_index))
df = pd.DataFrame(randn(6,2),hier_index,['A','B'])
print("the df with levels of index:\n{}".format(df))
print("getting the B column of 1 and 2 row in G2:\n{}"
      .format(df.loc['G2'].loc[[1,2]]['B']))
# the index name attribute could be directly retrieved or assigned
df.index.names = ['Groups','Numbers']
print("now the df with named levels of index:\n{}"
      .format(df))

# cross section allows retrieving data from deeper index cross upper index
print("get all number with Numbers index value of 1:\n{}"
      .format(df.xs(1,level='Numbers')))