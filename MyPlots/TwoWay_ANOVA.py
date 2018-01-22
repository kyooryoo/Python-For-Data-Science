# A simple plot
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
# check the raw data
df

# transform the raw data to facilitate plotting
plot_df = pd.DataFrame(columns=["Occupation","Location","Salaries"])
for col in df.columns:
    for row in df.index:
        for x in df[col][row]:
            ins = pd.DataFrame([[col,row,x]],
                               columns=["Occupation","Location","Salaries"])
            plot_df = plot_df.append(ins)

# transfer the data type of salary from object to numeic
plot_df['Salaries'] = pd.to_numeric(plot_df['Salaries'])
# reset the index to make it looks better, optional
plot_df.reset_index(drop=True,inplace=True)
# check the data frame before plotting
plot_df

fig, axes = plt.subplots(nrows=2,ncols=1,figsize=(6,8))
interaction_plot(plot_df["Occupation"],
                 plot_df["Location"],
                 plot_df["Salaries"],
                 colors=['red','blue'],
                 func=np.mean,
                 markers=['s','^'], 
                 ms=5,
                 ax=axes[0])
axes[0].legend(bbox_to_anchor=(1,.5),edgecolor='white',loc='center left')
interaction_plot(plot_df["Location"],
                 plot_df["Occupation"],
                 plot_df["Salaries"],
                 colors=['red','blue'],
                 func=np.mean,
                 markers=['s','^'], 
                 ms=5,
                 ax=axes[1])
axes[1].legend(bbox_to_anchor=(1,.5),edgecolor='white',loc='center left')

############################################################################
# a complete two way ANOVA
import pandas as pd
import statsmodels as sm
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.graphics.factorplots import interaction_plot
from scipy import stats

# read in some sample data
datafile="https://vincentarelbundock.github.io/Rdatasets/csv/datasets/ToothGrowth.csv"
data = pd.read_csv(datafile)
# info and head of the data
data.info()
data
# defie the significance value
alpha = 0.05

fig = interaction_plot(data.dose, data.supp, data.len,
             colors=['red','blue'], markers=['D','^'], ms=10)

N = len(data.len)
df_a = len(data.supp.unique()) - 1
df_b = len(data.dose.unique()) - 1
df_ab = df_a*df_b 
df_e = N - (len(data.supp.unique())*len(data.dose.unique()))

grand_mean = data['len'].mean()
ssa = sum([(data[data.supp ==l].len.mean()-grand_mean)**2 for l in data.supp])
ssb = sum([(data[data.dose ==l].len.mean()-grand_mean)**2 for l in data.dose])
sst = sum((data.len - grand_mean)**2)

vc = data[data.supp == 'VC']
oj = data[data.supp == 'OJ']
vc_dose_means = [vc[vc.dose == d].len.mean() for d in vc.dose]
oj_dose_means = [oj[oj.dose == d].len.mean() for d in oj.dose]
sse = sum((oj.len - oj_dose_means)**2) +sum((vc.len - vc_dose_means)**2)

ssab = sst-ssa-ssb-sse
msa = ssa/df_a
msb = ssb/df_b
msab = ssab/df_ab
mse =sse/df_e

f_a = msa/mse
f_b = msb/mse
f_ab = msab/mse

p_a = stats.f.sf(f_a, df_a, df_e)
p_b = stats.f.sf(f_b, df_b, df_e)
p_ab = stats.f.sf(f_ab, df_ab, df_e)

fc_a = stats.f.sf(alpha, df_a, df_e)
fc_b = stats.f.sf(alpha, df_b, df_e)
fc_ab = stats.f.sf(alpha, df_ab, df_e)

results = {'df':[df_a, df_b, df_ab, df_e],
           'SS':[ssa, ssb, ssab, sse],
           'MS':[msa, msb, msab, mse],
           'F':[f_a, f_b, f_ab, None],
           'P-value':[p_a, p_b, p_ab, None],
           'F crit':[fc_a, fc_b, fc_ab, None]}
columns=['df', 'SS','MS', 'F', 'P-value','F crit']
 
aov_table = pd.DataFrame(results, columns=columns,
    index=['supp', 'dose', 'Interaction', 'Within'])

def eta_squared(aov,ss):
    aov['eta_sq'] = 'NaN'
    aov['eta_sq'] = aov[:-1][ss]/sum(aov[ss])
    return aov
 
def omega_squared(aov,ss):
    mse = aov[ss][-1]/aov['df'][-1]
    aov['omega_sq'] = 'NaN'
    aov['omega_sq'] = (aov[:-1][ss]-(aov[:-1]['df']*mse))/(sum(aov[ss])+mse)
    return aov
  
eta_squared(aov_table,'SS')
omega_squared(aov_table,'SS')
print(aov_table)

# a short cut
formula = 'len ~ C(supp) + C(dose) + C(supp):C(dose)'
model = ols(formula, data).fit()
aov_table = anova_lm(model, typ=2)
eta_squared(aov_table,'sum_sq')
omega_squared(aov_table,'sum_sq')
print(aov_table)

# qqplot
res = model.resid 
fig = sm.api.qqplot(res, line='s')
plt.show()

# use library pyvttbl, library may need to be installed
from pyvttbl import DataFrame
df=DataFrame()
df.read_tbl(datafile)
df['id'] = range(len(df['len']))
print(df.anova('len', sub='id', bfactors=['supp', 'dose']))