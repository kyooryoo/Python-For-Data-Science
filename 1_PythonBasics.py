# following code is tested in Python3

# some note for basic Python
# variable names cannot start with number or special characters
# strings could be double or single quotes
# use print('my {one} output from {two}.'.format(one='first',two='Python'))
# or save 'one' and 'two' print('my {} output from {}.'.format(second,Python))
print('my {one} output from {two}.'.format(one='first',two='Python'))
print('my {} output from {}.'.format('second','Python'))

# list wrap elements with [] and can have mixed type of data and nested
alist = ['hi',1,[2,[3,4]]]
print("the original list: {}".format(alist))
# list have default funcs such as append, pop and so on
alist.append('a')
print("the current list after appending 'a': {}".format(alist))
# retrieve element in list with index, starting from 0
print('the first element of the third element: {}'.format(alist[2][0]))
# list elements could be modified directly
alist[0] = 'hello'
print('the current list after update: {}'.format(alist))

# dictionary use {} to wrap elements which have keys and values
adict = {'key1':'item1','key2':'item2'}
print('a sample dictionary: {}'.format(adict))
# refer to an element in dictionary with key
print('the item2 in sample: {}'.format(adict['key2']))

# tuples use () to wrap elements which cannot be modified
atuple = (1,2,3,2,1)
print('a sample tuple: {}'.format(atuple))
print('the third element: {}'.format(atuple[2]))
# atuple[2] = 'NEVER do this!' will cause error

# sets use {} to wrap elements which are all unique
aset = {1,2,3,2,1}
print('a sample set: {}'.format(aset))

# lambda returns a function which could be consumed easily
aseq = [1,2,3,4,5]
result = list(map(lambda var: var**2, aseq))
print('squared seq of [1,2,3,4,5]: {}'.format(result))

# some convenient system method
astring = 'Hello, welcome to the world of Python!'
print('the original string: {}'.format(astring))
uppered = astring.upper()
print('the string after upper: {}'.format(uppered))
splited = astring.split(',')
print('the string after split: {}'.format(splited))

print('a sample dict: {}'.format(adict))
print('the keys of a dict: {}'.format(adict.keys()))
print('the items of a dict: {}'.format(adict.items()))

print('a sample list: {}'.format(alist))
print('the last element poped: {}'.format(alist.pop()))
print('the list after poped: {}'.format(alist))
# the in method only works on the first level of a list
print('1 is in the list or not: {}'.format(1 in alist))
print('2 is in the list or not: {}'.format(2 in alist))
print("'a' is in the list or not: {}".format('a' in alist))


# list comprehensions
even_numbers = [x for x in range(5) if x % 2 == 0]
print("a list of even numbers: {}".format(even_numbers))
squares = [x * x for x in range(5)]
print("square the numbers from 0 to 4: {}".format(squares))
even_squares = [x * x for x in even_numbers]
print("square the even numbers: {}".format(even_squares))
square_dict = {x : x * x for x in range(5)}
print("the squared number dictionary: {}".format(square_dict))
square_set = {x * x for x in range(-5, 5)}
print("a set can only contain unique objects: {}".format(square_set))
zeros = [ 0 for _ in even_numbers]
print("use a list as index: {}".format(zeros))
pairs = [(x, y) for x in range(2) for y in range(3)]
print("a list of pared numbers: {}".format(pairs))
increasing_pairs = [(x, y) for x in range(5) for y in range(x + 1, 5)]
print("a list of increased numbers: {}".format(increasing_pairs))

# generate number by need
def lazy_range(n):
    i = 0
    while i < n:
        yield i
        i += 1
lazy_evens_below_20 = [i for i in lazy_range(20) if i % 2 == 0]
print("the even number below 20: {}".format(lazy_evens_below_20))

# generate random number
import random
four_uniform_randoms = [random.random() for _ in range(4)]
print("random 4 uniform numbers: {}".format(four_uniform_randoms))
# specify seed to get reproducible results
random.seed(10)
print("a reproducible random number: {}".format(random.random()))
random.seed(10)
print("a reproduced random number: {}".format(random.random()))
# random selection from range
print("random select from range 0 to 9: {}".format(random.randrange(10)))
print("random select from range 7 to 9: {}".format(random.randrange(8, 10)))
# random reorder the elements
up_to_ten = [x for x in range(10)]
random.shuffle(up_to_ten)
print("random order of 0 to 9: {}".format(up_to_ten))
# random select element
my_favorite_fruit = random.choice(["apple","banana","orange"])
print("random select elements: {}".format(my_favorite_fruit))
# random select element without duplicate
lottery_numbers = [x for x in range(60)]
winning_numbers = random.sample(lottery_numbers, 6)
print("random select unduplicated elements: {}".format(winning_numbers))
# random select element with duplicate
ten_with_replacement = [random.choice(range(10)) for _ in range(10)]
print("random select duplicatible elements: {}".format(ten_with_replacement))

# regular expression
import re
# use "not" to convert result to boolean value
result = not re.match("a", "cat") # returned value is None by default
print("'cat' starts with 'a': {}".format(not result)) # convert to boolean
result = not re.search("a", "cat")
print("'cat' has 'a': {}".format(not result))
result = re.split("[yo]","python")
print("split python by 'y' and 'o' get: {}".format(result))
result = re.sub("[0-9]","-","R2D2")
print("replace digit in R2D2 with dash: {}".format(result))

# object oriented programming
class Set:
 def __init__(self,values=None):
  self.dict = {}
  if values is not None:
   for value in values:
    if value not in self.dict:
     self.add(value)
 def __repr__(self):
  return str(self.dict.keys())
 def add(self, value):
  self.dict[value] = True
 def contains(self, value):
  return value in self.dict
 def remove(self, value):
  del self.dict[value]

s = Set([1,2,3])
print("the initial set: {}".format(s))
s.add(4)
print("after 4 added: {}".format(s))
print("the set contains 4: {}".format(s.contains(4)))
s.remove(3)
print("3 is removed: {}".format(s))
print("the set contains 3: {}".format(s.contains(3)))
s.add(4)
print("try adding one more 4: {}".format(s))

import functools as ft
# functional tools
def exp(base, power):
 return base ** power
# without functional tools
def two_to_the(power):
 return exp(2, power)
print("the specifically defined two_to_the(3): {}".format(two_to_the(3)))
# functools provides partial arguments for exp
# fulfills the first argument by default
new_two_to_the = ft.partial(exp, 2)
print("the newly defined new_two_to_the(3): {}".format(new_two_to_the(3)))
# with specified argument name
# second argument could be fulfilled in advance
square_of = ft.partial(exp, power=2)
print("also easily defined square_of(3): {}".format(square_of(3)))

# there are different ways to achieve the same purpose
def double(x):
 return 2 * x
xs = [1,2,3,4]
print("the original list is: {}".format(xs))
# use for
twice_xs = [double(x) for x in xs]
print("twice the list with for loop: {}".format(twice_xs))
# use map, should be wrapped with list() to display content in Python3
twice_xs = list(map(double, xs))
print("use map to apply func to var: {}".format(twice_xs))
# use partial with map to construct a new function
list_doubler = ft.partial(map, double)
twice_xs = list(list_doubler(xs))
print("use partial with map: {}".format(twice_xs))
# use map with multiple arguments
def multiply(x, y): return x * y
products = list(map(multiply, [1,2],[4,5]))
print("the products of [1,2] and [4,5]: {}".format(products))

# filter works as a list comprehension if
# filter need a function to return the boolean
def is_even(x):
 return x % 2 == 0
x_evens = [x for x in xs if is_even(x)]
print("for loop based filter: {}".format(x_evens))
x_evens = list(filter(is_even, xs))
print("filter works the same as map: {}".format(x_evens))
# combined with partial
list_evener = ft.partial(filter, is_even)
x_evens = list(list_evener(xs))
print("filter could also work with partial: {}".format(x_evens))

# reduce works on the elements iteratively
x_product = ft.reduce(multiply, xs)
print("use reduce to iteratively multiply numbers in list: {}"
      .format(x_product))
list_product = ft.partial(ft.reduce, multiply)
print("combine partial with reduce to create function: {}"
      .format(list_product(xs)))

# use index and elements in non-pythonic way
for index in range(len(xs)):
 element = xs[index]
 print("non-pythonic way: {} -- {}".format(str(index),str(element)))
# python way does not use index to specify list members
index = 0
for element in xs:
 print("pythonic way: {} -- {}".format(str(index),str(element)))
 index += 1
# use enumerate as the pythonic solution
# replace element with "_" if only need index
for index, element in enumerate(xs):
 print("enumerate way: {} -- {}".format(str(index),str(element)))

# use zip to pack or unpack lists
list1 = ['a','b','c']
list2 = [1,2,3]
zipped = list(zip(list1,list2))
print("zipped list of ['a','b','c'] and [1,2,3]: {}".format(zipped))
# use "*" to pass elements of zipped
# as individual argument to zip for unzipping
letters, numbers = zip(*zipped)
print("unzipped letters: {}".format(letters))
print("unzipped numbers: {}".format(numbers))
# zip the zipped object to unzip it
unzipped = list(zip(*zipped))
print("unzipped together: {}".format(unzipped)) 
# "*" could be very convenient
def add(a,b): return a + b
print("the result of add(1,2): {}".format(add(1,2)))
# add([1,2]) will be an error
print("the result of add(*[1,2]): {}".format(add(*[1,2]))) # this works

# a function can take another function as input and returns a function
def double(f):
 def g(x):
  return 2 * f(x)
 return g
# it works for single argument
def addone(x):
 return x + 1
addonethendouble = double(addone)
print("double func take addone func as parameter, input 3: {}"
      .format(addonethendouble(3))) # (3+1)*2=8
print("same as above, input 1: {}".format(addonethendouble(-1))) # (-1+1)*2=0
# it does not work below
def add(x, y):
 return (x + y)
addthendouble = double(add)
# print addthendouble(1,2) will generate error

# *args and **kwargs take arbitrary arguments
# args is a tuple of unnamed arguments
# kwargs is a dict of named arguments
def magic(*args, **kwargs):
 print("unnamed args: ", args)
 print("keyword args: ", kwargs)
magic(1,2,key1="word1",key2="word2")
# so this works
def double_correct(f):
 def g(*args, **kwargs):
  return 2 * f(*args, **kwargs)
 return g
addanddouble = double_correct(add)
print("double func take add func as parameter, input 1 and 2 : {}"
      .format(addanddouble(1,2))) # (1+2)*2=6

# For further exploration
# official tutorial at https://docs.python.org/3/tutorial
# IPython at http://ipython.org/ipython-doc/3/interactive/tutorial.html
# and also http://ipython.org/documentation.html
# and http://ipython.org/presentation.html
# A good reference book of Python for Data Analysis by William McKinney