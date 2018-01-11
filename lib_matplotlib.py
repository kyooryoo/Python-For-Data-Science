# matplotlib is a plotting library for Python similar to MatLab plotting tool
# more info https://matplotlib.org/gallery/index.html

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x**2

# functional way of plotting
plt.plot(x,y)
plt.xlabel('X label')
plt.ylabel('Y label')
plt.title('Title')
plt.show()

# color of plotting could be specified with color=xxx
# here xxx could be 'red' or RGB hex code as '#ff0000'
# line width could be customized with linewidth para
# the default line width is 1, and lw is its short form
# alpha para controls the transparency of the line
# linestyle or ls arg could defines the line style
# which takes :,-,--,step, and other special args
# marker has lots of relating setting options
plt.subplot(1,2,1)
plt.plot(x,y,color='red',linewidth=4,alpha=0.5,ls=':')
plt.subplot(1,2,2)
plt.plot(y,x,color='#00ff00',lw=2,linestyle='--',
         marker='o',markersize=10,markerfacecolor='yellow',
         markeredgewidth=2,markeredgecolor='red')
plt.show()

# object oriented way of plotting
fig = plt.figure() # create a figure object
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y,label='y=x^2')
axes.plot(x,x,label='y=x')
axes.set_xlabel('X label')
axes.set_ylabel('Y label')
axes.set_title('Title')
# consume the labels to legend
# legend has location code from 0 to 10, 0 for best
# or could have a tuple of persent marks like (0.1,0.1)
axes.legend(loc=0)

fig = plt.figure()
# numbers in the following list are location marks
# which in percent from 0 to 1 and starts from left bottom
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])
# a short version of defining red and dash line style
axes1.plot(x,y,'r--')
# a short version of defining green and star marked line style
axes2.plot(y,x,'g*-')

# plot multiple ones in one row or column
fig,axes = plt.subplots(nrows=1,ncols=2)
for current_ex in axes:
    current_ex.plot(x,y)
axes[0].plot(y,x)    
axes[1].plot(y,x)

# for fixing overlapping plots, use
plt.tight_layout()

# figure size could be specified during figure initilization
# the number in figsize is about length and hight in inches
# use set_xlim to limit display area, so does set_ylim
fig = plt.figure(figsize=(6,2))
axes = fig.add_axes([0,0,1,1])
axes.set_xlim([0,3])
axes.set_ylim([0,10])
axes.plot(x,y)

# input x1,y1,x2,y2,x3,y3... to plot multiple ones together
fig,axes = plt.subplots(nrows=1,ncols=2,figsize=(8,2))
axes[0].plot(x,x**2,x,x**3,x,x**4)
axes[1].plot(x,x**2,x,x**3,x,x**4)
# use tight arg to get tightly fitted range
axes[1].axis('tight')

# figure could be saved as image with savefig method
# image type is specified with extention names
# dpi could be specified here or in figure initilization
fig.savefig('my_fig.png',dpi=200)

# there also other specific plotting tools in matplotlib
# plotting scattered dots by default
plt.scatter(x,y)

# plotting histgrams
from random import sample
data = sample(range(1,1000),100)
plt.hist(data)

# plotting box plot
data = [np.random.normal(0,std,100) for std in range(1,4)]
plt.boxplot(data,vert=True,patch_artist=True)

# further reading materials
# http://www.matplotlib.org
# https://github.com/matplotlib/matplotlib
# http://matplotlib.org/gallery.html
# http://www.loria.fr/~rougier/teaching/matplotlib
# http://scipy-lectures.github.io/matplotlib/matplotlib.html