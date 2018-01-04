import numpy as np

arr = np.arange(0,11)

# know the meaning of index, start include and end exclude an index
# know the application of semicolon and some short cut
print("an array from which to take elements out: {}".format(arr))
print("the element at index 4: {}".format(arr[4]))
print("the elements betwee index 6 and 9: {}".format(arr[6:9]))
print("the elements from begin to index 5: {}".format(arr[:5]))
print("the elements beyond index 5: {}".format(arr[5:]))

# broadcast a value to many elements in an array
arr[3:6] = 100
print("modify elements from index 3 to index 6 to 100: \n{}".format(arr))

# pay attention to reference of array
# you might think you created another instance of the array slice
# but it is actually only a reference to the original array
arr_ref = arr[3:6]
print("the reference array: {}".format(arr_ref))
arr_ref[:] = 99
print("the modified reference array: {}".format(arr_ref))
print("the original array: {}".format(arr))
# for creating a copy of the array or its slice
arr_copy = arr[3:6].copy()
print("the copy array: {}".format(arr_copy))
arr_copy[:] = 88
print("the modified copy array: {}".format(arr_copy))
print("the original array: {}".format(arr))

# work with matrix
arr_2d = np.array([[5,15,20],[18,27,36],[28,35,42]])
print("a matrix: \n{}".format(arr_2d))
print("use [0][0] to retrieve the 1x1 element: {}".format(arr_2d[0][0]))
print("use [1] to retrieve the second row: {}".format(arr_2d[1]))
print("or use [2,1] to retrieve the 3x2 element: {}".format(arr_2d[2,1]))
print("use [:2,1:] to retrieve part of the matrix: \n{}".format(arr_2d[:2,1:]))

# work with boolean array
print("the array to compare: {}".format(arr))
arr_bool = arr <= 50
print("the result of array > 50: \n{}".format(arr_bool))
# consume the boolean array
arr_slice = arr[arr_bool]
print("the elements no more than 50: {}".format(arr_slice))
print("just use arr[arr>50] to get: {}".format(arr[arr>50]))