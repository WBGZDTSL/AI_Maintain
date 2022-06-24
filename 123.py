import lifelines
import matplotlib.pyplot as plt
from lifelines.datasets import load_waltons
from lifelines import KaplanMeierFitter

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
