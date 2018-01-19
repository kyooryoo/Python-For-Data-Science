# following code show examples of customized legend reference from
# https://stackoverflow.com/questions/4700614/how-to-put-the-legend-out-of-the-plot

import matplotlib.pyplot as plt
import numpy as np

def myPlot():
    x = np.arange(10)
    plt.figure()
    ax = plt.subplot(111)
    
    for i in range(5):
        ax.plot(x, i * x, label='$y = %ix$' % i)

# default
myPlot()
plt.legend()

# right top out
myPlot()
plt.legend(bbox_to_anchor=(1, 1),edgecolor='white')

# right middle out
myPlot()
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5),edgecolor='white')

# center top cut
myPlot()
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.10),
          ncol=3, fancybox=True, shadow=True)

# bottom out
myPlot()
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),
          fancybox=True, shadow=True, ncol=5)

