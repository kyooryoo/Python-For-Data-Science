# Pandas is an open source library built on top of Numpy
# it provides fast data analysis, cleaning, and preparation
# it has built in visualization feature, good performance
# and support a wide variety of data sources

# topics about pandas include: series, dataframes, missing data, groupby
# merging, joining, concatenating, and other operations, data IO

# series is a data type built on Numpy array
# series could be indexed by label
import numpy as np
import pandas as pd

labels = ['a','b','c'] # a list
my_data = [10,20,30] # a list
arr = np.array(my_data) # a numpy array
d = {'a':10,'b':20,'c':30} # a dictionary

s1 = pd.Series(data=my_data)
s2 = pd.Series(data=my_data,index=labels)
# parameters is right order do not have to be specified
# and a numpy array or list could be the same for data source
s3 = pd.Series(arr,labels)
print("the original list is: {}".format(my_data))
print("the transformed Series is:\n{}".format(s1))
print("Series with labels:\n{}".format(s2))
print("Series created from array:\n{}".format(s3))
# or a dictionray as input will have key as labels automatically
s4 = pd.Series(d)
print("Series created from dictionray:\n{}".format(s4))
# Series can also take functions as input data type
s5 = pd.Series(data=[sum,print,len])
print("Series can take functions as input data: \n{}".format(s5))

# elements in Series could be retrieved with their labels
s6 = pd.Series([1,2,3,4],['US','JP','CN','SG'])
print("a nother Series: \n{}".format(s6))
print("the element with label 'JP': {}".format(s6['JP']))
s7 = pd.Series([1,2,3,4],['US','FR','CN','SG'])
print("a similar Series:\n{}".format(s7))
# Series could operate on each other, non common elements lost value
print("combination of the two Series:\n{}".format(s6+s7))
# after combination elements order changed to alphabetic
# and all values in elements are tansferred from int to float