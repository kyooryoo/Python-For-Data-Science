"""
Numpy is a Linear Algebra Library for Python, upon which almost all of the
other libraries in PyData Ecosystem rely on. Numpy is fast, as it has bindings
to C libraries.
With Anaconda, use conda install numpy to install numpy. Without Anaconda, 
use pip install numpy to install numpy.
Numpy arrays, which has one dimention form of vector and two dimention form of
matrix, is the main way we use numpy.
"""
import numpy as np
# creat a list
my_list = [1,2,3]
print("a list: {}".format(my_list))
# cast a list to an array
arr = np.array(my_list)
print("a casted array: {}".format(arr))
# create a matrix
my_mat = [[1,2,3],[4,5,6],[7,8,9]]
print("a matrix: {}".format(my_mat))
# cast a matrix to an array
arr = np.array(my_mat)
print("a casted array: \n{}".format(arr)) 
# create an array froms cratch
arr = np.arange(0,10)
print("a created array from 0 to 9: {}".format(arr))
# the second para is the upper limit which is not included
# an optional third para could set the step size
arr = np.arange(0,11,2)
print("0 to 10 with step size of 2: {}".format(arr))
# some function for creating special arrays
arr = np.zeros(3)
print("an arry with 3 zeros: {}".format(arr))
arr = np.zeros((2,3))
print("a 2x3 matrix with zeros: {}".format(arr))
arr = np.ones(5)
print("an arry with 5 ones: {}".format(arr))
arr = np.ones((3,4))
print("an 3x4 matrix with ones:\n{}".format(arr))
# create array with linspace function
arr = np.linspace(0,10,4)
print("linspace(0,10,4):\n {}".format(arr))
# create identity matrix with eye function
arr = np.eye(4)
print("a size 4 idnetity matrix:\n{}".format(arr))
# create array from random numbers
arr = np.random.rand(5)
print("5 standardized random numbers: \n{}".format(arr))
arr = np.random.rand(5,5)
print("5x5 matrix of standardized random number: \n{}".format(arr))
arr = np.random.randn(5)
print("5 random numbers around 0: \n{}".format(arr))
arr = np.random.randint(1,100,10)
print("10 int random numbers between 1 and 99: \n{}".format(arr))
# use reshape function
arr = np.arange(0,25)
print("the original array: \n{}".format(arr))
arr = arr.reshape(5,5)
print("reshaped to 5x5 matrix: \n{}".format(arr))
# for retrieving some special values from an array
arr = np.random.randint(1,99,10)
print("an array of random number: {}".format(arr))
print("max is #{} in the random numbers: {}"
      .format(arr.argmax(),arr.max()))
print("min is #{} in the random numbers: {}"
      .format(arr.argmin(),arr.min()))
# call attribute to check the shape or data type of an array
arr = np.arange(0,5)
print("the shape of array {} is {}".format(arr,arr.shape))
arr = np.random.randint(1,100,25)
arr = arr.reshape(5,5)
print("the shape of matrix \n{} \nis {}".format(arr,arr.shape))
print("the data type of the matrix is: {}".format(arr.dtype))