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
grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]
decile = lambda grade: grade // 10 * 10
# Counter function does not work in Python v3.x
histogram = Counter(decile(grade) for grade in grades)
plt.bar([x - 4 for x  in histogram.keys()],histogram.values(),8)
# x-axis from -5 to 105 and y-axis from 0 to 5
plt.axis([-5, 105, 0, 5])
# x-axis labels at 0, 10, ..., 100
plt.xticks([10 * i for i in range(11)])
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution fo Exam Grades")
plt.show()
