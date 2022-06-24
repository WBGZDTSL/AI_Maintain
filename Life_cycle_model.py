import lifelines
import matplotlib.pyplot as plt
from lifelines.datasets import load_waltons,load_rossi
from lifelines import KaplanMeierFitter
from lifelines import CoxPHFitter

#%%
#KaplanMeierFitter Moedl
df = load_waltons()  # returns a Pandas DataFrame

T = df['T']
E = df['E']

kmf = KaplanMeierFitter()
kmf.fit(T, event_observed=E)  # more succiently, kmf.fit(T,E)

kmf.survival_function_
kmf.median_survival_time_

kmf.plot()
plt.show()

#%%
#Cox Model
rossi = load_rossi()
rossi.head()
cph = CoxPHFitter()
cph.fit(rossi, duration_col='week', event_col='arrest')
cph.plot()
plt.show()
