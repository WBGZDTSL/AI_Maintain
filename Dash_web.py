#%%
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
import time
from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px
#%%

df = pd.read_excel('chiller_data_preprocessed_v1.1.xlsx', sheet_name='Sheet1', header=0, index_col=None)
#%%
app = Dash(__name__)
# a = df['Predict_End_date']
# end_date = [int(stamp) for stamp in df['Predict_End_date'].unique()]

# temp = time.mktime()
app.layout = html.Div([
    dcc.Dropdown(['YKQRQSK15CSG', 'YKZSZSK75DJGS'], 'YKZSZSK75DJGSl'),
    dcc.Graph(
        id='expect_fault_date',
        # figure=test()
    ),
    dcc.Slider(
        df['Predict_End_Year'].min(),
        df['Predict_End_Year'].max(),
        step=None,
        value=df['Predict_End_Year'].min(),
        marks={str(year): str(year) for year in df['Predict_End_Year'].unique()},
        id='year-slider'
    )
])

@app.callback(
    Output('expect_fault_date', 'figure'),
    Input('year-slider', 'value'))
def test(selected_year):
    filtered_df = df[df['Predict_End_Year'] == selected_year]
    fig = px.scatter(filtered_df, x="Predict_End_date", y="Part Code",
                     color="Chiller", hover_name="Description",
                     log_x=False, size_max=55)

    fig.update_layout(transition_duration=500)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
