import numpy as np
import pandas as pd

# missing values
# pandas can fill missing values with null or NaN or drop them 
d = {'A':[1,2,np.nan],'B':[1,np.nan,np.nan],'C':[1,2,3]}
df = pd.DataFrame(d)
print("the df with missing value:\n{}".format(df))
print("by default, dropna drop rows with missing value:\n{}"
      .format(df.dropna()))
print("for dropping column, us arg axis=1:\n{}"
      .format(df.dropna(axis=1)))
print("drop rows with less than two valid values:\n{}"
      .format(df.dropna(thresh=2)))
print("fill missing value with number 5:\n{}"
      .format(df.fillna(value=5)))
print("fill missing values with its column mean:\n{}"
      .format(df.fillna(value=df.mean())))

# groupby can group rows based on a column and apply aggregate functions
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
        'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
        'Sales':[200,120,340,124,243,350]}
df = pd.DataFrame(data)
print("the original dataframe:\n{}".format(df))
byComp = df.groupby('Company')
# mean() aggregate function auto pass non-number columns
# similar functions are sum() std()
print("apply mean to group by company:\n{}"
      .format(byComp.mean()))
print("get the sum of FB with one line of code:\n{}"
      .format(df.groupby('Company').sum().loc['FB']))
# count() fun counts the instances within the group
# similar functions are max()
print("the instance within every company:\n{}"
      .format(df.groupby('Company').count()))
# one useful fun is describe, which privdes a summary
print("a summary of each company:\n{}"
      .format(df.groupby('Company').describe()))
print("the summary of company FB:\n{}"
      .format(df.groupby('Company').describe().loc['FB']))
# describe() returned df has MultiIndex in columns 
print("the max and min of all companies:\n{}"
      .format(df.groupby('Company').describe()['Sales'][['max','min']]))
print("a transposed version of the same summary:\n{}"
      .format(df.groupby('Company').describe().transpose()))
print("a portion of the transposed summary:\n{}"
      .format(df.groupby('Company').describe()
      .transpose().loc['Sales'].loc[['max','min']]))

# merging, joining and concatenating
df1 = pd.DataFrame({'A':['A0','A1','A2','A3'],
                   'B':['B0','B1','B2','B3'],
                   'C':['C0','C1','C2','C3'],
                   'D':['D0','D1','D2','D3']},
                   index=[0,1,2,3])
df2 = pd.DataFrame({'A':['A4','A5','A6','A7'],
                   'B':['B4','B5','B6','B7'],
                   'C':['C4','C5','C6','C7'],
                   'D':['D4','D5','D6','D7']},
                   index=[4,5,6,7])
df3 = pd.DataFrame({'A':['A8','A9','A10','A11'],
                   'B':['B8','B9','B10','B11'],
                   'C':['C8','C9','C10','C11'],
                   'D':['D8','D9','D10','D11']},
                   index=[8,9,10,11])
print("the three dataframes:\n{}\n{}\n{}"
      .format(df1,df2,df3))
# as dimensions match along the axis dfs can be joined together
print("the concatenated dataframe is:\n{}"
      .format(pd.concat([df1,df2,df3]))) 
print("concat on the wrong axis will get:\n{}"
      .format(pd.concat([df1,df2,df3],axis=1)))

keys1 = 'K0 K1 K2 K3'.split()
df4 = df1.transpose()
df5 = df2.transpose()
df4['key'] = keys1
df5['key'] = keys1
print("another two dataframes:\n{}\n{}".format(df4,df5))
result1 = pd.merge(df4,df5,how='inner',on='key')
print("merge the two dfs based on keys:\n{}".format(result1))

keys2 = 'K2 K3 K4 K5'.split()
df6 = df3.transpose()
df6['key'] = keys2
print("another one dataframes:\n{}".format(df6))
print("inner merge:\n{}"
      .format(pd.merge(result1,df6,how='inner',on='key')))
print("outer merge:\n{}"
      .format(pd.merge(result1,df6,how='outer',on='key')))
print("left merge:\n{}"
      .format(pd.merge(result1,df6,how='left',on='key')))
print("right merge:\n{}"
      .format(pd.merge(result1,df6,how='right',on='key')))

# join works in similar way with merge but on index not column
df4.set_index('key',inplace=True)
df5.set_index('key',inplace=True)
df6.set_index('key',inplace=True)
print("the modified three dataframes:\n{}\n{}\n{}".format(df4,df5,df6))
result2 = df4.join(df5)
print("join the first two:\n{}"
      .format(result2))
print("further inner jont the last one:\n{}"
      .format(result2.join(df6,how='inner')))
print("further outer jont the last one:\n{}"
      .format(result2.join(df6,how='outer')))
print("further left jont the last one:\n{}"
      .format(result2.join(df6,how='left')))
print("further right jont the last one:\n{}"
      .format(result2.join(df6,how='right')))

print("the dataframe will be used for the following ops:\n{}"
      .format(df))
print("there are {} unique values in column 'Company':\n{}"
      .format(df['Company'].nunique(),df['Company'].unique()))
print("the times every unique value appears:\n{}"
      .format(df['Company'].value_counts()))

# for applying a function to a column
def times2(x):
    return x*2
print("the sales values after times 2 are:\n{}"
      .format(df['Sales'].apply(times2)))
print("the length of every person name is:\n{}"
      .format(df['Person'].apply(len)))

# use lambda expression
print("the sales values after times 2 with lambda are:\n{}"
      .format(df['Sales'].apply(lambda x: x*2)))

# drop columns or index
print("the dataframe after dropping column 'Company' is:\n{}"
      .format(df.drop('Company',axis=1)))

# check content of the column or index
print("the column and index of sample dataframe are:\n{}\n{}"
      .format(df.columns,df.index))

# sort by column or index
print("sort the sample dataframe by sales values:\n{}"
      .format(df.sort_values('Sales')))

# check the whole dataframe for null values
print("check the null values in sample dataframe:\n{}"
      .format(df.isnull()))

# pivot table
data = {'Country':['US','US','US','JP','JP','JP'],
        'Gender':['M','M','F','M','M','F'],
        'Staff':['Staff','Manager','Staff','Staff','Manager','Manager'],
        'Number':[4,1,5,1,3,2]}
df = pd.DataFrame(data)
print("the sample dataframe:\n{}".format(df))
print("the pivot table:\n{}"
      .format(df.pivot_table(values='Number',
                             index=['Country','Gender'],
                             columns='Staff')))

#######################################################################
# some extra note

# for selecting column in dataframe use df['column name']
# row in dataframe use df.loc['row name']

# selecting sub elements in MultiIndexed columns use df[l1x][[l2x1,l2x2]]
# in MultiIndexed rows use df.loc[l1x].loc[[l2x1,l2x2]]

# merge is one function of panda package, takes both dfs as parameters
# join is one method of df object, takes df to be joined as parameter
# more complexed merge could happen on multiple columns of keys use
# pd.merge(df1,df2,on=['key1','key2']) to try the result