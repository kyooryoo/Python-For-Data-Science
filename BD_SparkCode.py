# lambda expression is used very often in big data process, here is warm up

# define a traditional function
def square(num):
    result = num**2
    return result

# verify it
square(4)

# simplify the function
def square(num):return num**2

# verify it
square(5)

# turn into lambda
square = lambda num: num**2

# verify it
square(6)

# some other lambdas
# notice: lambda is not used for defining a function but used directly in code
# here we use it to define a function just for verifying it is working

# check the number is even or not
even = lambda num: num%2 == 0
even(4)
even(5)

# return the first character of a string
first = lambda s: s[0]
first('abcde')

# reverse a string
rev = lambda s: s[::-1]
rev('abcde')

# add two values
add = lambda x,y: x+y
add(3,5)

# warm up of creating rdd and apply some actions
from pyspark import SparkContext
import ipython
sc = SparkContext()
ipython().run_cell_magic('writefile', 'example.txt', 
       'first line\nsecond line\nthird line\nfourth line ') 
textFile = sc.textFile('example.txt') # create the rdd object
textFile.count() # try an action
textFile.first() # another action
secfind = textFile.filter(lambda line: 'second' in line)
secfind
secfind.collect()
secfind.count()

# review some concepts:
# RDD: Resilient Distributed Dataset
# Transformation: Spark operation that produces an RDD
# Action: Spark operation that produces a local object
# Spark Job: Sequence of transformations on data with a final action

# two common ways to create an RDD
# sc.parallelize(array) creates RDD from elements of array or list
# sc.textFile(path/to/file) creates RDD from a file

# RDD Transformations is a set of instructions to perform on the RDD before
# we call an action and actually execute them on the RDD, examples:
# filter(lambda x: x % 2 == 0) discard non even elements
# map(lambda x: x * 2) multiply each elements by 2
# map(lambda x: x.split()) split each string into words
# flatMap(lambda x: x.split()) split each string into words and flatten seq
# sample(withReplacement=True,0.25) create sample of 25% elements with rep
# union(rdd) append rdd to existing RDD
# distinct() Remove duplicates in RDD
# sortBy(lambda x: x, ascending=False) sort elements in descending order

# RDD Actions execute the recipe in transformations, some common ones:
# collect() convert RDD to in memory list
# take(3) return first 3 elements of RDD
# top(3) return top 3 elements of RDD
# takeSample(withReplacement=True,3) create sample of 3 elements with rep
# sum() mean() std() find element sum mean or deviation of numeric elements

# run this code in jupyter notebook to create a sample text file
"""
%%writefile example.txt
first
second line
the third line
then a fourth line
"""
# return: Overwriting example.txt

from pyspark import SparkContext
sc = SparkContext()
# create an rdd
text_rdd = sc.textFile('example.txt')

# check the different before and after split
words = text_rdd.map(lambda line: line.split())
words.collect()
# [['first'],
#  ['second', 'line'],
#  ['the', 'third', 'line'],
#  ['then', 'a', 'fourth', 'line']]
text_rdd.collect()
# ['first', 'second line', 'the third line', 'then a fourth line']

# check the different action of flatmap
text_rdd.flatMap(lambda line: line.split()).collect()
# ['first',
#  'second',
#  'line',
#  'the',
#  'third',
#  'line',
#  'then',
#  'a',
#  'fourth',
#  'line']

# create another sample text file
"""
%%writefile services.txt
#EventId    Timestamp    Customer   State    ServiceID    Amount
201       10/13/2017      100       NY       131          100.00
204       10/18/2017      700       TX       129          450.00
202       10/15/2017      203       CA       121          200.00
206       10/19/2017      202       CA       131          500.00
203       10/17/2017      101       NY       173          750.00
205       10/19/2017      202       TX       121          200.00
"""
# Writing services.txt

services = sc.textFile('services.txt')
# check the first two lines
services.take(2)
# ['#EventId    Timestamp    Customer   State    ServiceID    Amount',
#  '201       10/13/2017      100       NY       131          100.00']

services.map(lambda line: line.split()).take(3)
# [['#EventId', 'Timestamp', 'Customer', 'State', 'ServiceID', 'Amount'],
#  ['201', '10/13/2017', '100', 'NY', '131', '100.00'],
#  ['204', '10/18/2017', '700', 'TX', '129', '450.00']]

# eliminate the # mark at the beginning of the first line
services.map(lambda line: line[1:] if line[0]=='#' else line).collect()
# ['EventId    Timestamp    Customer   State    ServiceID    Amount',
#  '201       10/13/2017      100       NY       131          100.00',
#  '204       10/18/2017      700       TX       129          450.00',
#  '202       10/15/2017      203       CA       121          200.00',
#  '206       10/19/2017      202       CA       131          500.00',
#  '203       10/17/2017      101       NY       173          750.00',
#  '205       10/19/2017      202       TX       121          200.00']

clean = services.map(lambda line: line[1:] if line[0]=='#' else line)
clean = clean.map(lambda line: line.split())
clean.collect()
# [['EventId', 'Timestamp', 'Customer', 'State', 'ServiceID', 'Amount'],
#  ['201', '10/13/2017', '100', 'NY', '131', '100.00'],
#  ['204', '10/18/2017', '700', 'TX', '129', '450.00'],
#  ['202', '10/15/2017', '203', 'CA', '121', '200.00'],
#  ['206', '10/19/2017', '202', 'CA', '131', '500.00'],
#  ['203', '10/17/2017', '101', 'NY', '173', '750.00'],
#  ['205', '10/19/2017', '202', 'TX', '121', '200.00']]

# take the interested featurs for calculating the grouped sum
clean.map(lambda line: (line[3],line[-1])).collect()
# [('State', 'Amount'),
#  ('NY', '100.00'),
#  ('TX', '450.00'),
#  ('CA', '200.00'),
#  ('CA', '500.00'),
#  ('NY', '750.00'),
#  ('TX', '200.00')]

# try to get the grouped sum, notice that Amount value was processed as text
pairs = clean.map(lambda line: (line[3],line[-1]))
rekey = pairs.reduceByKey(lambda amt1, amt2: amt1 + amt2)
rekey.collect()
# [('State', 'Amount'),
#  ('NY', '100.00750.00'),
#  ('TX', '450.00200.00'),
#  ('CA', '200.00500.00')]

# tranfer text to float by utilizing float() method 
rekey = pairs.reduceByKey(lambda amt1, amt2: float(amt1) + float(amt2))
rekey.collect()
[('State', 'Amount'), ('NY', 850.0), ('TX', 650.0), ('CA', 700.0)]

# the summary of all 4 steps
# grab (state, amount)
step1 = clean.map(lambda line: (line[3],line[-1]))
# reduce by key
step2 = step1.reduceByKey(lambda amt1,amt2: float(amt1)+float(amt2))
# get rid of titles
step3 = step2.filter(lambda x: not x[0]=='State')
# sort result by amount
step4 = step3.sortBy(lambda stAmount: stAmount[1],ascending=False)
# action
step4.collect()
# [('NY', 850.0), ('CA', 700.0), ('TX', 650.0)]


# sometimes we need more readable functions
X = ['ID','State','Amount']
# not easy to read
def func1(lst):
    return lst[-1]
# much more readable
def func2(id_st_amt):
    # unpack values
    (pid,st,amt) = id_st_amt
    return amt
func1(X)
# 'Amount'
func2(X)
# 'Amount'