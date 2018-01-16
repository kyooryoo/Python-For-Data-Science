# Seaborn is a statistical plotting library built on Matplotlib
# Seaborn has beautiful styles and works well with pandas dataframes
# use keywords of seaborn, github, and python to search seaborn repo
# go to official doc page and pay attention to API and Gallery tabs

# some plots such as distplot or boxplot are common and more widely used
# other plots should be carefully used or just for exploring the data

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# seaborn has some default datasets such as tips
tips = sns.load_dataset('tips')
print("the head of tips dataframe:\n{}".format(tips.head()))

# a histgram with or without kde (kernel density estimation) plot
sns.distplot(tips['total_bill'],kde=False,bins=20)

# for comparing two values
# kind can take 'hex','reg', 'scatter' by default, or 'kde'
sns.jointplot(x='total_bill',y='tip',data=tips,kind='kde')

# pair plot is a full jointplot of all numerical values in a dataframe
# optionally hue arg provides more categorical details
# optionally palette sets the color style
sns.pairplot(tips,hue='sex',palette='coolwarm')

# rug plot is a horizontal formed histgram plot
sns.rugplot(tips['total_bill'])
sns.kdeplot(tips['total_bill'])

# bar plot can aggregate the categorical data
sns.barplot(x='sex',y='total_bill',data=tips)
sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.std)

# count plot simply count the instances based on categary
sns.countplot(x='sex',data=tips)

# box plot shows the distribution of categorical data
# use hue to reveal more detail based on an extra category
sns.boxplot(x='day',y='total_bill',data=tips)
sns.boxplot(x='day',y='total_bill',data=tips,hue='smoker')

sns.violinplot(x='day',y='total_bill',data=tips)
sns.violinplot(x='day',y='total_bill',data=tips,hue='sex')
sns.violinplot(x='day',y='total_bill',data=tips,hue='sex',split=True)

# strop plot is a scatter plot of categorical and numerical value
# set jitter arg to ture to have dots more scattered to reveal density
sns.stripplot(x='day',y='total_bill',data=tips,jitter=True)
sns.stripplot(x='day',y='total_bill',data=tips,
              jitter=True,hue='sex',split=True)

# swarm plot combines the features of both violin plot and strip plot
# this plot is not widely used, nor good for plotting a big dataframe
sns.swarmplot(x='day',y='total_bill',data=tips)

# sometimes plots could be combined to reveal more information
sns.violinplot(x='day',y='total_bill',data=tips)
sns.swarmplot(x='day',y='total_bill',data=tips,color="yellow")

# factor plot can easily plot other kinds of plots by specify in kind arg
sns.factorplot(x='day',y='total_bill',data=tips,kind='bar')
sns.factorplot(x='day',y='total_bill',data=tips,kind='violin')

# for plotting matrix, we have to prepare a matrix in advance
# coorelate tips to make a matrix which has variables in both rows and columns
tc = tips.corr()
# use heatmap to reveal the heat of a matrix
sns.heatmap(tc)
sns.heatmap(tc,annot=True)
sns.heatmap(tc,annot=True,cmap='coolwarm')

# prepare another matrix with the pivot table of another dataframe flights
flights = sns.load_dataset('flights')
print("another dataset of flights:\n{}".format(flights.head()))
fp = flights.pivot_table(index='month',columns='year',values='passengers')
print("the pivot table of flights:\n{}".format(fp.head()))
sns.heatmap(fp,cmap='rainbow',linecolor='white',lw=1)

# cluster map automatically cluster data by their similarities
sns.clustermap(fp,cmap='coolwarm')
sns.clustermap(fp,cmap='coolwarm',standard_scale=1)

# lmplot adds linear model regression info into the plot
sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',markers=['o','x'])
sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',markers=['o','x'],
           scatter_kws={'s':100})
sns.lmplot(x='total_bill',y='tip',data=tips,col='sex',row='time')
sns.lmplot(x='total_bill',y='tip',data=tips,col='day',hue='sex',
           aspect=1.5,size=4)

iris = sns.load_dataset('iris')
print("a third sample dataframe iris:\n{}".format(iris.head()))
print("there are {} species of iris in this dataframe:\n{}"
      .format(iris['species'].nunique(),iris['species'].unique()))
# pairplot is an automatic version of pairgrid
sns.pairplot(iris)
# pairgrid requires more detailed control
pg = sns.PairGrid(iris)
pg.map(plt.scatter)
# or with more sophisticated control
pg = sns.PairGrid(iris)
pg.map_diag(sns.distplot)
pg.map_upper(plt.scatter)
pg.map_lower(sns.kdeplot)

# facet grid map a plot to a specific feature based on two conditions
# this example map distribution plot to the feature of total bill
# based on different combination of situations of time and smoker
fg = sns.FacetGrid(data=tips,col='time',row='smoker')
fg.map(sns.distplot,'total_bill')
# or map scatter plot to total bill and tip, as scatter requires two args
fg = sns.FacetGrid(data=tips,col='time',row='smoker')
fg.map(plt.scatter,'total_bill','tip')

# figure size could be modified in advance of plotting
plt.figure(figsize=(8,3))
# some predefined template could be used such as poster
# use font_scale arg to further modify font size by times
sns.set_context('notebook',font_scale=1)
# for styling the plot background use set_style() method with paras of
# white, ticks, darkgrid, whitegrid
sns.set_style('white')
sns.countplot(x='sex',data=tips)
# the top and right spines could be removed by default
# left and bottom apines could be removed by specified
sns.despine(left=False,bottom=False)

# matplotlib provides series of colormap for palette settings
# search matplotlib and colormap to find the sample and their keywords
sns.lmplot(x="total_bill",y="tip",data=tips,hue='sex',palette='coolwarm')