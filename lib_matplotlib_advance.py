import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)

# each of the axes's scale could be set seperatedly
# with set_xscale or set_yscale
fig,axes = plt.subplots(1,2,figsize=(10,4))
axes[0].plot(x,x**2,x,np.exp(x))
axes[0].set_title("Normal Scale")
axes[1].plot(x,x**2,x,np.exp(x))
axes[1].set_yscale("log")
axes[1].set_title("Logarithmic scale (y)")

# set customized tick location and tick labels
fig,axes = plt.subplots(figsize=(10,4))
axes.plot(x,x**2,x,x**3)
axes.set_xticks([1,2,3,4,5])
axes.set_xticklabels([r'$\alpha$',r'$\beta$',r'$\gamma$'
                      ,r'$\delta$',r'$\epsilon$'],fontsize=18)
yticks = [0,50,100,150]
axes.set_yticks(yticks)
axes.set_yticklabels(["$%.1f$" %y for y in yticks],fontsize=18)

# use scientific notation instead of very large numbers
from matplotlib import ticker
fig,axes = plt.subplots(1,1)
axes.plot(x,x**2,x,np.exp(x))
axes.set_title("Scientific Notation")
axes.set_yticks([0,50,100,150])
formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
formatter.set_powerlimits((-1,1))
axes.yaxis.set_major_formatter(formatter)

# modify the distance between numbers and the axes, default is 3
matplotlib.rcParams['xtick.major.pad'] = 10
matplotlib.rcParams['ytick.major.pad'] = 10

# modify the padding of the labels on the axes
fig,axes = plt.subplots(1,1)
axes.plot(x,x**2,x,np.exp(x))
axes.set_yticks([0,50,100,150])
axes.set_title("label and axis spacing")
# the default padding is 3
axes.xaxis.labelpad = 10
axes.yaxis.labelpad = 10
axes.set_xlabel("X label")
axes.set_ylabel("Y label")

# as axes tick pad settings are global, they should be reset to default
matplotlib.rcParams['xtick.major.pad'] = 3
matplotlib.rcParams['ytick.major.pad'] = 3

# sometimes labels are out of the save figure image
# fig.savefig('my_fig.png')

# adjust the axes position to have labels included in the output image
fig.subplots_adjust(left=0.15,right=0.9,bottom=0.2,top=0.9)
fig.savefig('my_fig.png')

# grid could be added to plot, and could be customized in style
fig,axes = plt.subplots(1,2,figsize=(10,3))
axes[0].plot(x,x**2,x,np.exp(x),lw=2)
axes[0].grid(True)
axes[1].plot(x,x**2,x,np.exp(x),lw=2)
axes[1].grid(color='b',alpha=0.5,linestyle='dashed',linewidth=0.5)

# customize the color, size, and visibility of axis spines
fig,axes = plt.subplots(figsize=(6,2))
axes.spines['bottom'].set_color('blue')
axes.spines['top'].set_color('blue')
axes.spines['left'].set_color('red')
axes.spines['left'].set_linewidth(2)
axes.spines['right'].set_color("none")
axes.yaxis.tick_left()

# set dual axes in a figure to show two data with different units
fig,ax1 = plt.subplots()
ax1.plot(x,x**2,lw=2,color="blue")
ax1.set_ylabel(r"area $(m^2)$",fontsize=18,color="blue")
for label in ax1.get_yticklabels():
    label.set_color("blue")
ax2 = ax1.twinx()
ax2.plot(x,x**3,lw=2,color="red")
ax2.set_ylabel(r"volume $(m^3)$)",fontsize=18,color="red")
for label in ax2.get_yticklabels():
    label.set_color("red")

# center of crossed axes could be placed in the middle of the figure
# default plot
fig,ax = plt.subplots()
xx = np.linspace(-1,1,100)
ax.plot(xx,xx**3)
ax.set_title("Default plot")
# position resetted plot
fig,ax = plt.subplots()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))
# ax.xaxis.set_ticks_position('bottom')
# ax.yaxis.set_ticks_position('left')
ax.plot(xx,xx**3)
ax.set_title("Spines repositioined")

# differen kinds of plot, such as scatter, step, bar, or fill are available
# complete list is available at http://matplotlib.org/gallery.html
n = np.array([0,1,2,3,4,5])
fig,axes = plt.subplots(1,4,figsize=(12,3))
axes[0].scatter(xx,xx + 0.25*np.random.randn(len(xx)))
axes[0].set_title("scatter")
axes[1].step(n,n**2,lw=2)
axes[1].set_title("step")
axes[2].bar(n,n**2,align="center",width=0.5,alpha=0.5)
axes[2].set_title("bar")
axes[3].fill_between(x,x**2,x**3,color="green",alpha=0.5)
axes[3].set_title("fill_between")

# annotating text could be added to plot with text function
fig,ax = plt.subplots()
ax.plot(xx,xx**2,xx,xx**3)
ax.text(0.15,0.2,r"$y=x^2$",fontsize=20,color="blue")
ax.text(0.65,0.1,r"$y=x^3$",fontsize=20,color="green")
ax.set_title("With annotating text")

# for multiple subplots and insets

# with subplots() function
fig,axes = plt.subplots(2,3)
fig.tight_layout()

# with subplot2grid function
fig = plt.figure()
# (3,3) means 3 rows and and 3 columns in total
# (0,0) means from the first row and first column 
ax1 = plt.subplot2grid((3,3),(0,0),colspan=3)
ax1.set_title("(3,3),(0,0),colspan=3")
# (1,0) means from the second row and first column
ax2 = plt.subplot2grid((3,3),(1,0),colspan=2)
ax2.set_title("(3,3),(1,0),colspan=2")
ax3 = plt.subplot2grid((3,3),(1,2),rowspan=2)
ax3.set_title("(3,3),(1,2),rowspan=2")
ax4 = plt.subplot2grid((3,3),(2,0))
ax4.set_title("(3,3),(2,0)")
ax5 = plt.subplot2grid((3,3),(2,1))
ax5.set_title("(3,3),(2,1)")
fig.tight_layout()

# with gridspec function
import matplotlib.gridspec as gridspec
fig = plt.figure()
gs = gridspec.GridSpec(2,3,height_ratios=[2,1],width_ratios=[1,2,1])
for g in gs:
    ax = fig.add_subplot(g)
fig.tight_layout()

# add axes within current figure
fig,ax = plt.subplots()
ax.plot(xx,xx**2,xx,xx**3)
fig.tight_layout()
inset_ax = fig.add_axes([.62,.16,.3,.3]) # X Y width height
inset_ax.plot(xx,xx**2,xx,xx**3)
inset_ax.set_title("zoom near origin")
inset_ax.set_xlim(-.2,.2)
inset_ax.set_ylim(-.005,.01)
inset_ax.set_xticks([-.1,0,.1])
inset_ax.set_yticks([0,.005,.01])

# use colormap or contour figures to plot functions with two variables
# more samples at http://www.scipy.org/Cookbook/Matplotlib/Show_colormaps
alpha = 0.7
phi_ext = 2*np.pi*0.5
def flux_qubit_potential(phi_m,phi_p):
    return 2+alpha-2*np.cos(phi_m)*np.cos(phi_p)-alpha*np.cos(phi_ext-2*phi_p)
phi_m = np.linspace(0,2*np.pi,100)
phi_p = np.linspace(0,2*np.pi,100)
X,Y = np.meshgrid(phi_p,phi_m)
Z = flux_qubit_potential(X,Y)
# plot colormap with pcolor() function
fig,ax=plt.subplots()
p = ax.pcolor(X/(2*np.pi),Y/(2*np.pi),Z,cmap=matplotlib.cm.RdBu,
              vmin=abs(Z).min(),vmax=abs(Z).max())
cb = fig.colorbar(p,ax=ax)
# with imshow() function
fig,ax=plt.subplots()
im = ax.imshow(Z,cmap=matplotlib.cm.RdBu,extent=[0,1,0,1],
               vmin=abs(Z).min(),vmax=abs(Z).max())
im.set_interpolation('bilinear')
cb = fig.colorbar(im,ax=ax)
# with contour() function
fig,ax=plt.subplots()
cnt = ax.contour(Z,cmap=matplotlib.cm.RdBu,extent=[0,1,0,1],
               vmin=abs(Z).min(),vmax=abs(Z).max())
cb = fig.colorbar(cnt,ax=ax)

# use Axes3D class to create 3D figures
from mpl_toolkits.mplot3d.axes3d import Axes3D

# surface plot
fig = plt.figure(figsize=(14,6))
# a simple one
ax = fig.add_subplot(1,2,1,projection='3d')
p = ax.plot_surface(X,Y,Z,rstride=4,cstride=4,linewidth=0)
# a polished one
ax = fig.add_subplot(1,2,2,projection='3d')
p = ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=matplotlib.cm.coolwarm,
                    linewidth=0,antialiased=False)
cb = fig.colorbar(p,shrink=0.5)

# wire frame
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(1,1,1,projection='3d')
p = ax.plot_wireframe(X,Y,Z,rstride=4,cstride=4)

# contour with projections
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(1,1,1,projection='3d')
ax.plot_surface(X,Y,Z,rstride=4,cstride=4,alpha=.25)
cset = ax.contour(X,Y,Z,zdir='z',offset=-np.pi,cmap=matplotlib.cm.coolwarm)
cset = ax.contour(X,Y,Z,zdir='x',offset=-np.pi,cmap=matplotlib.cm.coolwarm)
cset = ax.contour(X,Y,Z,zdir='y',offset=3*np.pi,cmap=matplotlib.cm.coolwarm)
ax.set_xlim3d(-np.pi,2*np.pi)
ax.set_ylim3d(0,3*np.pi)
ax.set_zlim3d(-np.pi,2*np.pi)

# further reading
# http://www.matplotlib.org
# https://github.com/matplotlib/matplotlib
# http://matplotlib.org/gallery.html
# http://www.loria.fr/~rougier/teaching/matplotlib
# http://scipy-lectures.github.io/matplotlib/matplotlib.html
