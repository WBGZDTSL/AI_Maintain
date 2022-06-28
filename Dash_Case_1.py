import pandas as pd
import numpy as np
import lifelines
import matplotlib.pyplot as plt
from sklearn import preprocessing
import pickle
import datetime
import time
#%%
from os import mkdir
from os.path import join, exists
from datetime import date
#%%input data
data=pd.read_csv('Data.csv')
#%%reformat
a1=pd.to_datetime(data["Start_date"],format='%Y/%m/%d')
a1.dt.strftime('%Y-%m-%d')
a2=pd.to_datetime(data["End_date"],format='%Y/%m/%d')
a2.dt.strftime('%Y-%m-%d')
#%%
work_days = (a2 - a1)/24
#%%
def count_differ_days(self,time_a):
    a = pd.Series(time_a, index=range(len(a1)))
    d1 = pd.to_datetime(a, format='%Y-%m-%d')
    return (a2 - d1)/24
#%%
# time_a=2022-06-06
a = pd.Series("20220606", index=range(len(a1)))
d1 = pd.to_datetime(a, format='%Y-%m-%d')
work_days2 = (a2 - d1)/24
#%%
count_differ_days("20240622")


