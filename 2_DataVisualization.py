# for installing the library of matplotlib:
# http://matplotlib.org/users/installing.html#installing-an-official-release

# this script is written and tested in windows 10 with python v3
from matplotlib import pyplot as plt

# use line chart to show the trend of some data
year = [1950,1960,1970,1980,1990,2000,2010]
gdp = [300.2,543.3,1075.9,2862.5,5979.6,10289.7,14958.3]
# create a line chart with year on x-axis and gdp on y-axis
plt.plot(year,gdp,color='green',marker='o',linestyle='solid')
# add a title
plt.title("Nominal GDP")
# add a label to the y-axis
plt.ylabel("Billions of $")
plt.show()

# use bar chart to show quantity varies between descrete items
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]
xs = [i for i, _ in enumerate(movies)]
plt.bar(xs, num_oscars)
plt.ylabel(" # of Academy Awards")
plt.title("My Favorite Movies")
# label x-axis with movie names at bar centers
plt.xticks([i for i, _ in enumerate(movies)], movies)
plt.show()

# histogram
# import Counter from collections lib
from collections import Counter
grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]
decile = lambda grade: grade // 10 * 10
# Counter function does not work in Python v3.x
histogram = Counter(decile(grade) for grade in grades)
plt.bar([x for x  in histogram.keys()],histogram.values(),8)
# x-axis from -5 to 105 and y-axis from 0 to 5
plt.axis([-5, 105, 0, 5])
# x-axis labels at 0, 10, ..., 100
plt.xticks([10 * i for i in range(11)])
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution fo Exam Grades")
plt.show()

# pay attention to the start point of y-axis
mentions = [500, 505]
years = [2013, 2014]
# in Unix replace following with: 
# plt.bar([2012.6,2013.6],mentions,0.8)
plt.bar([2013,2014],mentions,0.8)
plt.xticks(years)
plt.ylabel("# of times I heard people say 'data science'")
# in Unix add: plt.ticklabel_format(useOffset=False)
# y-axis not start from 0 can be misleading
plt.axis([2012.5,2014.5,499,506])
plt.title("Look at the 'HUGE' increase")
plt.show()
plt.bar([2013,2014],mentions,0.8)
plt.xticks(years)
plt.ylabel("# of times I heard people say 'data science'")
# with more sensible axes, the difference is less impressive
plt.axis([2012.5,2014.5,0,550])
plt.title("Not So Huge Anymore")
plt.show()

# multiple line chart
variance = [1,2,4,8,16,32,64,128,256]
bias_squared = [256,128,64,32,16,8,4,2,1]
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]
# call plt.plot multiple times to draw series of lines
plt.plot(xs, variance, 'g-', label='variance') # green solid line
plt.plot(xs, bias_squared, 'r-.', label='bias^2') # red dot-dashed line
plt.plot(xs, total_error, 'b:', label='total error') # blue dotted line
plt.legend(loc=9)
plt.xlabel("model complexity")
plt.title("The Bias-Variance Tradeoff")
plt.show()

# use scatterplots to visualize two paired sets of data
friends = [70,65,72,63,71,64,60,64,67]
minutes = [175,170,205,120,220,130,105,145,190]
labels = ['a','b','c','d','e','f','g','h','i']
plt.scatter(friends,minutes)
# label each point
for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label, 
            xy=(friend_count, minute_count), # put label with its point 
            xytext=(5,-5), textcoords='offset points')
plt.title("Daily Minutes vs. Number of Friends")
plt.xlabel("# of friends")
plt.ylabel("daily minutes spent on the site")
plt.show()

# specify the scale to show a less misleading picture
test_1_grades = [90,90,85,97,80] # with less variance
test_2_grades = [100,85,60,90,70] # with more variance
# add or remove the setting below to find the difference
# plt.axis("equal")
plt.scatter(test_1_grades,test_2_grades)
plt.title("Axes aren't comparable")
plt.xlabel("test 1 grade")
plt.ylabel("test 2 grade")
plt.show()

# For further exploration
# seaborn for enhance visualization at http://seaborn.pydata.org
# D3.js for interactive visualization on web at https://d3js.org
# Bokeh of python in D3.js style at https://bokeh.pydata.org/en/latest
# the Python way of R lib ggplot2 at https://pypi.python.org/pypi/ggplot

