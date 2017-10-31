# the functions for Vectors
from functools import partial, reduce

def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v, w)]

def vector_substract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]

def vector_sum(vectors):
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result
# another way for sum vectors:
def vector_sum_1(vectors):
    return reduce(vector_add, vectors)
# or
vector_sum_2 = partial(reduce, vector_add)

def scalar_multiply(c, v):
    return [c * v_i for v_i in v]

def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

# doc product is the sum of products of 
# the same positioned elements in vectors v and w
def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    return dot(v, v)

import math
def magnitude(v):
    return math.sqrt(sum_of_squares(v))

def squared_distance(v, w):
    return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
    return math.sqrt(squared_distance(v, w))

# as the equivalent
def distance(v, w):
    return magnitude(vector_subtract(v, w))


# the functions fo matrics
def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

def get_row(A, i):
    return A[i]

def get_col(A, j):
    return [A_i[j] for A_i in A] # for each row A_i

def make_matrix(num_rows, num_cols, entry_fn):
    return [[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]

# following is an example of entry_fn
def is_diagonal(i, j):
    return 1 if i == j else 0

indentity_matrix = make_matrix(5, 5, is_diagonal)
print(indentity_matrix)

# For further exploration
# study Linear Algebra at https://www.math.ucdavis.edu/~linear/
# or http://joshua.smcvt.edu/linearalgebra
# or http://www.math.brown.edu/~treil/papers/LADW/LADW.html
# use NumPy for scientific computing with Python at http://www.numpy.org

