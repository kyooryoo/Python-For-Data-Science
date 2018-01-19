# the data source is https://www.kaggle.com/mchirico/montcoalert

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('911.csv')
df.info()
df.head()

# top 5 zip code for calls
df['zip'].value_counts().head(5)
# top 5 township for calls
df['twp'].value_counts().head(5)
# number of unique value in title codes
df['title'].nunique()

# split the reason code from title to create a new column named "Reason"
df['Reason'] = df['title'].apply(lambda x: x.split(":")[0])
# find the most common reason
df['Reason'].value_counts().head(3)
# use Seaborn to create a count plot of reason
sns.countplot(df['Reason'],palette='viridis')
sns.countplot(x='Reason',data=df)

# check the data type of the objects in timeStamp column
type(df['timeStamp'][0])
# convert the string type date stamp into date time type
df['timeStamp'] = pd.to_datetime(df['timeStamp'])
# add new features of Hour, Month and Day of Week
df['Hour'] = df['timeStamp'].apply(lambda x: x.hour)
df['Month'] = df['timeStamp'].apply(lambda x: x.month)
df['Day of Week'] = df['timeStamp'].apply(lambda x: x.dayofweek)
# convert Day of Week to more readable form by mapping
dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
df['Day of Week'] = df['Day of Week'].map(lambda x: dmap[x])
# df['Day of Week'] = df['Day of Week'].map(dmap) # this is sufficient

# create a count plot of day of week with hue based on reason
sns.countplot(x='Day of Week',data=df,hue='Reason',palette='viridis')
plt.legend(bbox_to_anchor=(1.05, 1),borderaxespad=0,facecolor='white',
           edgecolor='white')
# create a count plot of month with hue based on reason
sns.countplot(x='Month',data=df,hue='Reason',palette='viridis')
plt.legend(bbox_to_anchor=(1.25, 1),borderaxespad=0,facecolor='white',
           edgecolor='white')
# use line plot to cover the missing data for some months
byMonth = df.groupby('Month').count()
byMonth['e'].plot()

# use implot() to create a linear fit on the number of calls per month
# use reset_index() to reset index back to a column for reuse
sns.lmplot(x='Month',y='e',data=byMonth.reset_index())
# create a date column by applying the date() method
df['Date'] = df['timeStamp'].apply(lambda x: x.date())
# aggregate the call counts by date and plot
df.groupby('Date').count()['e'].plot(color='blue')
plt.tight_layout()

# aggregate the call counts by reason and date
df[df['Reason']=='Traffic'].groupby('Date').count()['e'].plot(color='blue')
plt.title('Traffic')
plt.tight_layout()
df[df['Reason']=='Fire'].groupby('Date').count()['e'].plot(color='blue')
plt.title('Fire')
plt.tight_layout()
df[df['Reason']=='EMS'].groupby('Date').count()['e'].plot(color='blue')
plt.title('EMS')
plt.tight_layout()

# restructure the dataframe to have colomns as hours and indexs as day of week
# create a heatmap of the restructured dataframe
plot_data = df.groupby(['Day of Week','Hour']).count()['e']\
    .sort_index().unstack(level=-1)
plt.figure(figsize=(8,6))
sns.heatmap(plot_data,cmap='viridis')
plt.tight_layout()
# create a cluster map with the same data
plt.figure(figsize=(8,6))
sns.clustermap(plot_data,cmap='viridis')
plt.tight_layout()
# repoeat same operation for month and day of week
plot_data = df.groupby(['Day of Week','Month']).count()['e']\
    .sort_index().unstack(level=-1)
plt.figure(figsize=(8,6))
sns.heatmap(plot_data,cmap='viridis')
plt.tight_layout()
# create a cluster map with the same data
plt.figure(figsize=(8,6))
sns.clustermap(plot_data,cmap='viridis')
plt.tight_layout()