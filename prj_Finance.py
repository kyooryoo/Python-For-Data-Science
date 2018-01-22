from pandas_datareader import data
import seaborn as sns
import matplotlib.pyplot as plt
import plotly
import cufflinks as cf
import pandas as pd
import numpy as np
import datetime
# comment out the line of code below for showing plot in Jupyter Notebook
# %matplotlib inline

# create start and end time from Jan 1st 2006 to Jan 1st 2016
start = datetime.datetime(2006,1,1)
end = datetime.datetime(2016,1,1)

# run following code line by line to make sure they are done
BAC = data.DataReader("BAC", 'yahoo', start, end)
C = data.DataReader("C", 'yahoo', start, end)
GS = data.DataReader("GS", 'yahoo', start, end)
JPM = data.DataReader("JPM", 'yahoo', start, end)
MS = data.DataReader("MS", 'yahoo', start, end)
WFC = data.DataReader("WFC", 'yahoo', start, end)

tickers = ["BAC","C","GS","JPM","MS","WFC"]
tickers.sort()

# pay attention to the use of keys argument
bank_stocks = pd.concat([BAC,C,GS,JPM,MS,WFC],axis=1,keys=tickers)
bank_stocks.columns.names = ['Bank Ticker','Stock Info']

# get the max close price for each bank stock during this period
bank_stocks.xs(key='Close',axis=1,level='Stock Info').max()

# use pct_change() method to calculate the return value per day
# pct_change() calculates the change of input sequence in percentage
returns = pd.DataFrame()
for tick in tickers:
    returns[tick+' Return'] = bank_stocks[tick]['Close'].pct_change()

# use seaborn to pairplot the returns dataframe
# exclude the first line of input data which contains NaN
sns.pairplot(returns[1:])

# use idxmin() to get the day with the least return for each bank
returns.idxmin()
# for getting the day with the most return
returns.idxmax()

# find the standard deviation of returns, bigger value means less
# stable price in the stock price
returns.std()
# use loc[] to specify a peroid of time for calculating std
returns.loc['2015-01-01':'2015-12-31'].std()

# create a displot using seaborn of the 2015 returns for MS
sns.distplot(returns.loc['2015-01-01':'2015-12-31']['MS Return'],
             bins=50,color='green')

# create a displot using seaborn of the 2008 returns for C
sns.distplot(returns.loc['2008-01-01':'2008-12-31']['C Return'],
             bins=50,color='red')

# line plot the close price for each bank for the entire time
for tick in tickers:
    bank_stocks[tick]['Close'].plot(label=tick,figsize=(12,4))
plt.legend()
# with cross section method
bank_stocks.xs(key='Close',axis=1,level='Stock Info').plot(figsize=(12,4))

# plot the rolling 30 day average of the close price for BAC in 2008
plt.figure(figsize=(12,4))
plot_data = BAC['Close'].loc['2008-01-01':'2009-01-01']
plot_data.rolling(window=30).mean().plot(label='30 day Mov Avg')
plot_data.plot(label='BAC Close')
plt.legend()

# plot the heatmap of the correlation between the stock close price
plot_data = bank_stocks.xs(key='Close',axis=1,level='Stock Info').corr()
sns.heatmap(plot_data,annot=True)

# plot the clustermap of the same data above
plot_data = bank_stocks.xs(key='Close',axis=1,level='Stock Info').corr()
sns.clustermap(plot_data,annot=True)

# following iplot only work in Jupyter Notebook

# a candle plot for Bank of America in year 2008
plot_data = BAC[['Open','High','Low','Close']].loc['2008-01-01':'2009-01-01']
plot_data.iplot(kind='candle')

# plot a Simple Moving Average plot of Morgan Stanley for 2015
plot_data = MS[['Close']].loc['2015-01-01':'2015-01-01']
plot_data.ta_plot(study='sma',periods=[13,21,55])

# plot a Bollinger Band Plot for Bank of America for 2015
plot_data = BAC[['Close']].loc['2015-01-01':'2015-01-01']
plot_data.ta_plot(study='boll')