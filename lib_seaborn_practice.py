import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid')
titanic = sns.load_dataset('titanic')
print("head of the sample titanic dataframe:\n{}".format(titanic.head()))

# do not forget the data parameter, kind here is optional
sns.jointplot(x='fare',y='age',data=titanic,kind="scatter")

sns.distplot(titanic['fare'],kde=False,color='red',bins=30)

sns.boxplot(x='class',y='age',data=titanic,palette='rainbow')

sns.swarmplot(x='class',y='age',data=titanic)

# be careful to use countplot instead of barplot
sns.countplot(x='sex',data=titanic)

# notice how to add title to the plot
sns.heatmap(titanic.corr(),cmap="coolwarm")
plt.title('titanic.corr()')

fg = sns.FacetGrid(data=titanic,col='sex')
#fg.map(sns.distplot,'age',kde=False,bins=10)
fg.map(plt.hist,'age')