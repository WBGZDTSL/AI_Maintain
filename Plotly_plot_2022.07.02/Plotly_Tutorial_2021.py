import cufflinks as cf
import pandas as pd
import numpy as np
import chart_studio.plotly as py
import seaborn as sns
import plotly.express as px
%matplotlib inline
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
cf.go_offline()
#%%
import plotly.graph_objects as go
df_stocks= px.data.stocks()
a1= df_stocks['date']
# df_stocks.head(20)
px.line(df_stocks,x='date',y='GOOG',labels={'x':'Date','y':'Price'})
#%%
df_us = px.data.gapminder().query("country == 'United States'")
flights= sns.load_dataset("flights")
