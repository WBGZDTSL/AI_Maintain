import pandas as pd

import plotly.express as px
import plotly.graph_objects as go

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output

#%%
df = pd.read_excel(r'C:\Users\jweiban\PycharmProjects\Git-base\AI Maintain\chiller_data_preprocessed_v1.1.xlsx',
                   sheet_name='Sheet1', header=0, index_col=None)
df1= df.groupby(['Hours','Qty'])
df1.reset_index(inplace=True)
#%%
# app = dash.Dash(__name__)
