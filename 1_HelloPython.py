# list comprehensions
even_numbers = [x for x in range(5) if x % 2 == 0]
print(even_numbers)
squares = [x * x for x in range(5)]
print(squares)
even_squares = [x * x for x in even_numbers]
print(even_squares)
square_dict = {x : x * x for x in range(5)}
print(square_dict)
square_set = {x * x for x in range(-5, 5)}
print(square_set)
zeros = [ 0 for _ in even_numbers]
print(zeros)
pairs = [(x, y)
         for x in range(3)
         for y in range(3)]
print(pairs)
increasing_pairs = [(x, y)
                    for x in range(3)
                    for y in range(x + 1, 3)]
print(increasing_pairs)

# generate number by need
def lazy_range(n):
    i = 0
    while i < n:
        yield i
        i += 1
lazy_evens_below_20 = [i for i in lazy_range(20) if i % 2 == 0]
print(lazy_evens_below_20)

# generate random number
import random
four_uniform_randoms = [random.random() for _ in range(4)]
print(four_uniform_randoms)
# specify seed to get reproducible results
random.seed(10)
print(random.random())
random.seed(10)
print(random.random())
# random selection from range
random.seed(10)
print(random.randrange(10))
print(random.randrange(5, 10))
# random reorder the elements
up_to_ten = [x for x in range(10)]
random.shuffle(up_to_ten)
print(up_to_ten)
# random select element
my_favorite_fruit = random.choice(["apple","banana","orange"])
print(my_favorite_fruit)
# random select element without duplicate
lottery_numbers = [x for x in range(60)]
winning_numbers = random.sample(lottery_numbers, 6)
print(winning_numbers)
# random select element with duplicate
ten_with_replacement = [random.choice(range(10))
                         for _ in range(10)]
print(ten_with_replacement)

# regular expression
import re
# use "not" to convert result to boolean value
result = not re.match("a", "cat")
print("'cat' starts with 'a': " + str(not result))
result = not re.search("a", "cat")
print("'cat' has 'a': " + str(not result))
result = re.split("[yo]","python")
print("split python by 'y' and 'o' get: " + str(result))
result = re.sub("[0-9]","-","R2D2")
print("replace digit in R2D2 with dash: " + result)

# object oriented programming
class Set:
 def __init__(self,values=None):
  self.dict = {}
  if values is not None:
   for value in values:
    self.add(value)
 def __repr__(self):
  return "Set: " + str(self.dict.keys())
 def add(self, value):
  self.dict[value] = True
 def contains(self, value):
  return value in self.dict
 def remove(self, value):
  del self.dict[value]

s = Set([1,2,3])
s.add(4)
print s.contains(4)
s.remove(3)
print s.contains(3)

print "# functional tools"
# the function of exp takes two arguments
def exp(base, power):
 return base ** power
# without functional tools
def two_to_the(power):
 return exp(2, power)
# with functional tools
# provides partial arguments for exp
# which fulfills the first argument by default
from functools import partial
two_to_the = partial(exp, 2)
print two_to_the(3)
# with specified argument name
# second argument could be fulfilled in advance
square_of = partial(exp, power=2)
print square_of(3)
# there are different ways to achieve the same purpose
def double(x):
 return 2 * x
xs = [1,2,3,4]
# use for
twice_xs = [double(x) for x in xs]
print twice_xs
# use map
twice_xs = map(double, xs)
print twice_xs
# use map with partial
list_doubler = partial(map, double)
twice_xs = list_doubler(xs)
print twice_xs
# use map with multiple arguments
def multiply(x, y): return x * y
products = map(multiply, [1,2],[4,5])
print products
# filter works as a list comprehension if
def is_even(x):
 return x % 2 == 0
x_evens = [x for x in xs if is_even(x)]
print x_evens
x_evens = filter(is_even, xs)
print x_evens
# combined with partial
list_evener = partial(filter, is_even)
x_evens = list_evener(xs)
print x_evens
# reduce works on the elements iteratively
x_product = reduce(multiply, xs)
print x_product
list_product = partial(reduce, multiply)
x_product = list_product(xs)
print x_product
# use index and elements in non-pythonic way
for index in range(len(xs)):
 element = xs[index]
 print str(index) + " : " + str(element)
# or
index = 0
for element in xs:
 print str(index) + " : " + str(element)
 index += 1
# use enumerate as the pythonic solution
# replace element with "_" if only need index
for index, element in enumerate(xs):
 print str(index) + " : " + str(element)

print "# use zip to pack or unpack lists"
list1 = ['a','b','c']
list2 = [1,2,3]
zipped = zip(list1,list2)
print zipped
# use "*" to pass elements of zipped
# as individual argument to zip for unzipping
letters, numbers = zip(*zipped)
print letters
print numbers
# zip the zipped object to unzip it
unzipped = zip(*zipped)
print unzipped 
# "*" could be very convenient
def add(a,b): return a + b
print add(1,2)
# add([1,2]) will be an error
print add(*[1,2]) # this works

# sometimes a function takes 
# another function as input
# and returns a function
def doubler(f):
 def g(x):
  return 2 * f(x)
 return g
# it works for single argument
def f1(x):
 return x + 1
g = doubler(f1)
print g(3) # (3+1)*2=8
print g(-1) # (-1+1)*2=0
#it does not work below
def f2(x, y):
 return x + y
g = doubler(f2)
# print g(1,2) will generate error
# *args and **kwargs take arbitrary arguments
# args is a tuple of unnamed arguments
# kwargs is a dict of named arguments
def magic(*args, **kwargs):
 print "unnamed args: ", args
 print "keyword args: ", kwargs
magic(1,2,key1="word1",key2="word2")
# so this works
def doubler_correct(f):
 def g(*args, **kwargs):
  return 2 * f(*args, **kwargs)
 return g
g = doubler_correct(f2)
print g(1,2) # (1+2)*2=6
