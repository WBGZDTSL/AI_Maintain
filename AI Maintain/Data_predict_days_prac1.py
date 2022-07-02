import pandas as pd
from sklearn import linear_model
#%%input data
data1=pd.read_csv("Data_predict_days.csv")
#%%
X = data1[['First_damage_days', 'Second_damage_days','Tired_damage_days']]
y = data1['Predict_next_damage_days']
#%%sklearn-liner regression
reg = linear_model.LinearRegression()
reg.fit(X, y)
#%% decision-making tree
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
#%%
z=data1['Damagable_status']
dec_tree = DecisionTreeClassifier()
dec_tree = dec_tree.fit(X, z)
#%%product data by tree
data2 = tree.export_graphviz(dec_tree, out_file=None, feature_names=['First_damage_days', 'Second_damage_days','Tired_damage_days'])
#%%
graph = pydotplus.graph_from_dot_data(data2)
graph.write_png('mydecisiontree.png')
img=pltimg.imread('mydecisiontree.png')
imgplot = plt.imshow(img)
plt.show()
#%%BP neural network
import numpy as np
import matplotlib as mpl
from sklearn.preprocessing import  MinMaxScaler
#%%







