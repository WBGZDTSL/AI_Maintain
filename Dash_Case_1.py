import pandas as pd
import numpy as np
import lifelines
import matplotlib.pyplot as plt
from sklearn import preprocessing
import pickle
#%%
from os import mkdir
from os.path import join, exists
#%%输入数据
data=pd.read_csv('Data.csv')
#%%


