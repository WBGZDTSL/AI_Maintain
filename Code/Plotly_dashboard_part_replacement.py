#Library
from dash import Dash, dcc, html, Input, Output, dash_table
import pandas as pd
import plotly.express as px
#%%Dash Environment build
app = Dash(__name__)

df = pd.read_excel('Data_Template.xlsx', sheet_name='Sheet1', header=0, index_col=None)## Data export
df['concat_month'] = df['Predict_End_Year'].astype(str) + '/' + df['Predict_End_Month'].astype(str)


end_date = [stamp for stamp in df['concat_month'].unique()]
colors = {
    'background': '#111111',
    'text': '#00549E'
}

app.layout = html.Div([
    html.H1(children='Chiller part replacement visualization',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
            ),

    html.Div(children='Chiller Parts Expected Fail Date',
             style={
                 'textAlign': 'center',
                 'color': colors['text']
             }
             ),

    dcc.Graph(
        id='expect_fault_date',
        # figure=test()
    ),
    html.Div(
        children="Enter a certain month: like 2022/9",
        style={
            'textAlign': 'left',
            'color': colors['text']
        }
    ),
    dcc.Input(
        # html.Br(),
        placeholder='Enter: yyyy/mm',
        type='text',
        value='',
        id='date-textbox'
    ),
    html.Button('Check', id='textbox-button', n_clicks=0),
    html.Br(),
    html.Br(),
    dash_table.DataTable(
        id='table1',
        columns=[
            {"name": i, "id": i, "hideable": True}
            for i in
            ['Chiller', 'Description', 'Part Code', 'Product_Start_date', 'Predict_End_date', 'Predict_End_FY']
        ],
        data=df.to_dict('records'),
        filter_action="native",
        sort_action="native",
        sort_mode="single",
        row_selectable="multi",
        page_action="native",
        page_current=0,
        page_size=6,
        style_cell={
            'minWidth': 80, 'maxWidth': 80, 'width': 80
        },
        style_cell_conditional=[
            {
                'if': {'column_id': c},
                'textAlign': 'left'
            } for c in ['Chiller', 'Description', 'Part Code']
        ],
        style_data={
            'whiteSpace': 'normal',
            'height': 'auto'
        }
    ),
    html.Br(),
    html.Br(),

],

    style={'width': '90%', "margin-left": '5%'}

)


@app.callback(
    Output('expect_fault_date', 'figure'),
    Output('table1', 'data'),
    Input('textbox-button', 'n_clicks'),
    Input('date-textbox', 'value')
)
def test(n_clicks, value):
    if n_clicks > 0:
        filtered_df = df[df['concat_month'] == value]

        if filtered_df.empty and value != '':
            fig = px.scatter(filtered_df, x="Predict_End_date", y="Part Code",
                             color="Chiller", hover_name="Description",
                             log_x=False, size_max=10,
                             labels=dict(Predict_End_date="Chiller Part Fail Date"),
                             title='No part is about to fail this month')
            # fig.update_layout(transition_duration=500)
            data = filtered_df.to_dict('records')
        elif value == '':
            fig = px.scatter(df, x="Predict_End_date", y="Part Code",
                             color="Chiller", hover_name="Description",
                             log_x=False, size_max=10,
                             labels=dict(Predict_End_date="Chiller Part Fail Date"))

            fig.update_layout(transition_duration=500)
            data = df.to_dict('records')
        else:
            fig = px.scatter(filtered_df, x="Predict_End_date", y="Part Code",
                             color="Chiller", hover_name="Description",
                             log_x=False, size_max=10,
                             labels=dict(Predict_End_date="Chiller Part Fail Date"))

            fig.update_layout(transition_duration=500)
            data = filtered_df.to_dict('records')
    else:
        fig = px.scatter(df, x="Predict_End_date", y="Part Code",
                         color="Chiller", hover_name="Description",
                         log_x=False, size_max=10,
                         labels=dict(Predict_End_date="Chiller Part Fail Date"))

        fig.update_layout(transition_duration=500)
        data = df.to_dict('records')
    return fig, data


if __name__ == '__main__':
    app.run_server(debug=True)
