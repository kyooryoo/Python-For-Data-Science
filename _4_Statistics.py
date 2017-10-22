# for describing a set of data
from matplotlib import pyplot as plt
from collections import Counter
num_friends = [100,49,41,40,25] # the sample data here is not complete
friend_counts = Counter(num_friends)
xs = range(101)
ys = [friend_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0,101,0,25])
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()

# number of data point
num_points = len(num_friends)
print("The # of data points is: " + str(num_points))
# the largest and smallest values
largest_value = max(num_friends)
print("The largest value got from max() is: " + str(largest_value))
smallest_value = min(num_friends)
print("The smallest value got from min() is: " + str(smallest_value))
# use sorting
sorted_values = sorted(num_friends)
print("The sorted number of friends values are: " + str(sorted_values))
smallest_value = sorted_values[0]
print("The smallest value got from sorted result is: " + str(smallest_value))
largest_value = sorted_values[-1]
print("The largest value got from sorted result is: " + str(largest_value))
second_smallest_value = sorted_values[1]
print("The 2nd smallest value is: " + str(second_smallest_value))
second_largest_value = sorted_values[-2]
print("The 2nd largest value is: " + str(second_largest_value))

def mean(x):
    return sum(x) / len(x)
print("The mean of all values is: " + str(mean(num_friends)))

def median(v):
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2
    if n % 2 == 1:
        return sorted_v[midpoint]
    else:
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2
print("The median of all values is: " + str(median(num_friends)))

# return the pth-percentile value in x
def quantile(x, p):
    p_index = int(p * len(x))
    return sorted(x)[p_index]
q10 = quantile(num_friends, 0.1)
q25 = quantile(num_friends, 0.25)
q75 = quantile(num_friends, 0.75)
q90 = quantile(num_friends, 0.9)
print("The 10 percentile value in sample data is: " + str(q10))
print("The 25 percentile value in sample data is: " + str(q25))
print("The 75 percentile value in sample data is: " + str(q75))
print("The 90 percentile value in sample data is: " + str(q90))

# mode is the most common value
def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    # dict.iteritems() is removed in Python 3, use dict.items() instead
    return [x_i for x_i, count in counts.items() if count == max_count]
print("The mode of sample data is: " + str(mode(num_friends)))

def data_range(x):
    return max(x) - min(x)
print("The range of sample data is: " + str(data_range(num_friends)))

# variance is a more complex measure of dispersion than range
from _3_LinearAlgebraFunctions import sum_of_squares
def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]
def variance(x):
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)
print("The variance of sample data is: " + str(variance(num_friends)))

import math
def standard_deviation(x):
    return math.sqrt(variance(x))
sd = standard_deviation(num_friends)
print("The standard deviation of sample sata is: " + str(sd))

def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)
ir = interquartile_range(num_friends)
print("The interquartile range of sample data is: " + str(ir))

# covariance measures how two variables vary in tendem from their means
from _3_LinearAlgebraFunctions import dot
daily_minutes = [10,5,4,4,2]
def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)
result = covariance(num_friends, daily_minutes)
print("The covariance of sample data is: " + str(result))

# correlation is standardized covariance which is always between -1 and 1 
# it could be impacted by outliers which should be removed in advance
def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0
result = correlation(num_friends, daily_minutes)
print("The correlation of sample data is: " + str(result))

# pay attention to Simpson's Paradox
# for example, two groups of people compare their average age 
# the mean of age values of group A may larger than group B
# however, it is possible that the average age of both adults and chuldren
# of group A are smaller than group B
# just because group A has much more adults in percentage than group B
