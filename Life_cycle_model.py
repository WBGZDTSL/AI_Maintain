%matplotlib inline
%config InlineBackend.figure_format = 'retina'
import lifelines
import matplotlib.pyplot as plt
from lifelines.datasets import load_waltons,load_rossi
from lifelines import KaplanMeierFitter
from lifelines import CoxPHFitter
import pandas as pd
import numpy as np
from sklearn import preprocessing
import pickle
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
cph.fit(rossi, duration_col='week', event_col='arrest')#model fitting
cph.plot()
#plt.show()
#
cph.print_summary(model="untransformed variables", decimals=3)
#
cph.check_assumptions(rossi, p_value_threshold=0.05, show_plots=True)
#
from lifelines.statistics import proportional_hazard_test
results = proportional_hazard_test(cph, rossi, time_transform='rank')
results.print_summary(decimals=3, model="untransformed variables")
#
cph.fit(rossi, 'week', 'arrest', strata=['wexp'])
cph.print_summary(model="wexp in strata")
#
cph.check_assumptions(rossi, show_plots=True)
#
rossi['age**2'] = (rossi['age'] - rossi['age'].mean())**2
rossi['age**3'] = (rossi['age'] - rossi['age'].mean())**3
#
cph.fit(rossi, 'week', 'arrest', strata=['wexp'], formula="bs(age, df=4, lower_bound=10, upper_bound=50) + fin +race + mar + paro + prio")
cph.print_summary(model="spline_model"); print()
cph.check_assumptions(rossi, show_plots=True, p_value_threshold=0.05)
#
rossi_strata_age = rossi.copy()
rossi_strata_age['age_strata'] = pd.cut(rossi_strata_age['age'], np.arange(0, 80, 3))
rossi_strata_age[['age', 'age_strata']].head()
# drop the orignal, redundant, age column
rossi_strata_age = rossi_strata_age.drop('age', axis=1)
cph.fit(rossi_strata_age, 'week', 'arrest', strata=['age_strata', 'wexp'])
#
cph.print_summary(3, model="stratified age and wexp")
cph.plot()
#plt.show()
#
cph.check_assumptions(rossi_strata_age)
#
from lifelines.utils import to_episodic_format
# the time_gaps parameter specifies how large or small you want the periods to be.
rossi_long = to_episodic_format(rossi, duration_col='week', event_col='arrest', time_gaps=1.)
rossi_long.head(25)
#
rossi_long['time*age'] = rossi_long['age'] * rossi_long['stop']
#
from lifelines import CoxTimeVaryingFitter
ctv = CoxTimeVaryingFitter()
ctv.fit(rossi_long,
        id_col='id',
        event_col='arrest',
        start_col='start',
        stop_col='stop',
        strata=['wexp']
#
ctv.plot()
# plt.show()



