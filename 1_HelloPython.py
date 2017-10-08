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
# use not to convert result to boolean value
result = not re.match("a", "cat")
print("cat starts with a: " + str(not result))
result = not re.search("a", "cat")
print("cat has a: " + str(not result))
result = re.split("[yo]","python")
print("split python by y and o get: " + str(result))
result = re.sub("[0-9]","-","R2D2")
print("replace digit in R2D2 with dash: " + result)
