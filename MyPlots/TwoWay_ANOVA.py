# Use interaction_plot from Statesmodels lib 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.factorplots import interaction_plot

# transfer the raw data to a dataframe
data = [[[45,51,52,48,54],[42,44,47,49,50]],
        [[46,50,50,50,52],[45,48,49,47,48]]]
index = ['Urban','Rural']
columns = ['Physician Assistant','Nurse Practitioner']
df = pd.DataFrame(data=data,index=index,columns=columns)

# transfer raw data to list for plotting
# prepare x and y axis identifiers
plot_data = []
oc = []
lo = []
for column in df.columns:
    for row in df.index:
        for x in df[column][row]:
            plot_data.append(x)
            oc.append(column)
            lo.append(row)

# transfer x and y identifiers to series and plot
plot_data = pd.Series(plot_data,name="Salary in thousands of USD")
oc = pd.Series(oc,name="Occupation")
lo = pd.Series(lo,name="Location")
fig, axes = plt.subplots(nrows=2,ncols=1,figsize=(6,8))
interaction_plot(oc,lo,plot_data,colors=['red','blue'],func=np.mean,
    markers=['s','^'], ms=5,ax=axes[0])
axes[0].legend(bbox_to_anchor=(1,1),edgecolor='white')
interaction_plot(lo,oc,plot_data,colors=['blue','red'], 
    markers=['^','s'], ms=5,ax=axes[1])
axes[1].legend(bbox_to_anchor=(1,1),edgecolor='white')