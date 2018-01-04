# this script is about operations on numpy array
import numpy as np
arr = np.arange(0,11)
print("the original array is: {}".format(arr))

# array could be added together directly
print("add the original array to itself: {}".format(arr+arr))
print("subtract the original array from itself: {}".format(arr-arr))
print("multiply the original array with itself: {}".format(arr*arr))

# scalar operations happens to each element of an array
print("add 100 to each element: {}".format(arr+100))

# divide 0 by 0 get nan and warning
print("devide the original array by itself: {}".format(arr/arr))

# devide other number by 0 get inf and warning
print("devide 1 with the original array: {}".format(1/arr))
print("devide the original array with 0: {}".format(arr/0))

# some numpy functions on array
print("the square root of original array, np.sqrt(arr): \n{}"
      .format(np.sqrt(arr)))
print("the exponential of original array, np.exp(arr): \n{}"
      .format(np.exp(arr)))
print("the max value in original array, np.max(arr): {}".format(np.max(arr)))
print("same result could get from arr.max(): {}".format(arr.max()))
print("np.sin(arr): {}".format(np.sin(arr)))
print("np.log(arr): {}".format(np.log(arr)))

# some extra content from notes
arr_2d = np.zeros((10,10))
print("the original 2d array: \n{}".format(arr_2d))
arr_width = arr_2d.shape[1]
for i in range(arr_width):
    arr_2d[i] = i
print("the row modified matrix: \n{}".format(arr_2d))
print("use [[2,4,8]] to retrieve the third, fifth, and ninth row: \n{}"
      .format(arr_2d[[2,4,8]]))

# some advanced operation
print("sum by column: {}".format(arr_2d.sum(axis=0)))
print("standard deviation: {}".format(arr.std()))

# for more detailed info about universal functions
# https://docs.scipy.org/doc/numpy/reference/ufuncs.html
# https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.statistics.html