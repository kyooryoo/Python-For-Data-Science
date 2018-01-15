import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,100)
y = x*2
z = x**2

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)
ax.set_title("The Title")
ax.set_xlabel("X Label")
ax.set_ylabel("Y Label")

fig = plt.figure()
ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([.2,.6,.2,.2])
ax1.plot(x,y,color='red')
ax2.plot(x,y,color='red')
ax1.set_xlabel("X Label")
ax1.set_ylabel("Y Label")
ax2.set_xlabel("X Label")
ax2.set_ylabel("Y Label")

fig = plt.figure()
ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([.15,.5,.4,.4])
ax1.plot(x,z,color='blue')
ax2.plot(x,y,color='blue')
ax2.set_xlim(20,22)
ax2.set_ylim(30,50)
ax1.set_xlabel("X")
ax1.set_ylabel("Z")
ax2.set_xlabel("X")
ax2.set_ylabel("Y")

fig,axes = plt.subplots(nrows=1,ncols=2,figsize=(8,2))
axes[0].plot(x,y,color='blue',lw=4,ls='--')
axes[1].plot(x,z,color='red',lw=4)
plt.tight_layout()

