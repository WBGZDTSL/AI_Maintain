import pandas as pd
import numpy as np
import lifelines
import matplotlib.pyplot as plt
from sklearn import preprocessing
import pickle
import datetime as dt
import time
#%%
from os import mkdir
from os.path import join, exists
from datetime import date
#%%input data
data=pd.read_csv('Data.csv')
#%%
a1=dt.datetime.strptime(data.iloc[1,8],'%Y-%m-%d').date()
a2=dt.datetime.strptime(data.iloc[1,9],'%Y-%m-%d').date()
a3=(a2-a1).days
#%%
# def count_differ_days(self,time_a):
#     a = pd.Series(time_a, index=range(len(a1)))
#     d1 = pd.to_datetime(a, format='%Y-%m-%d')
#     return (a2 - d1)/24
#count_differ_days("20240622")
#%%
df = pd.read_excel('chiller_data_preprocessed_v1.1.xlsx', sheet_name='Sheet1', header=0, index_col=None)
# a = df['Predict_End_date']
end_date = [int(stamp) for stamp in df['Predict_End_date'].unique()]