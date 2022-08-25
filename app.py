import os
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

app.layout = html.Div([
    html.H4('Simple stock plot with adjustable axis'),
    html.Button("Switch Axis", n_clicks=0, 
                id='button'),
    dcc.Graph(id="graph"),
    dcc.Checklist(
        id="checklist",
        options=["north", "east", "south","west","all"],
        value=[],
        inline=True
    ),
])


@app.callback(
    Output("graph", "figure"), 
    Input("button", "n_clicks"),
    Input("checklist","value"))
def display_graph(n_clicks, value):
    stream= os.popen('git rev-parse --show-toplevel')
    dir = stream.read().strip()



    df = pd.read_csv(dir+'/combinedSalesData.csv') # replace with your own data source

    # groups = df.groupby(by='region')


    if n_clicks % 2 == 0:
        x, y = 'time', 'sales'
    else:
        x, y = 'sales', 'time'

    if("all" in value):
        fig = px.line(df, 
        x=x, y=y, color='region', title="sales of pink morsel by region over time")
        return fig


    mask = df.region.isin(value)
    fig = px.line(df[mask], 
        x=x, y=y, color='region', title="sales of pink morsel by region over time")

    # fig = px.line(df, x=x, y=y, color='region', title="sales of pink morsel by region over time")    
    return fig


app.run_server(debug=True)