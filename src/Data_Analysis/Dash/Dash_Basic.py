import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output

df = pd.read_csv('src/Data_Analysis/Dash/Dash.csv')
app = Dash()
app.title = "Interactive Dashboard"
num_cols = df.select_dtypes(include='number').columns
app.layout = html.Div([
    html.H1("Interactive Dashboard with pie plot"),
    html.Label("Select a value to show in the pie chart"),
    dcc.Dropdown(id = 'column-dropdown',
        options = [{'lable': col, 'value': col} for col in num_cols],
        value = num_cols[0]),
    dcc.Graph(id = 'pie-chart')
])

@app.callback(Output('pie-chart', 'figure'),Input('column-dropdown', 'value'))
def update_pie(select_col):
    grouped = df.groupby('Area')[select_col].sum().reset_index()
    fig = px.pie(grouped, names='Area', values=select_col, title=f"distribution of {select_col} by Area", hole=0.4, color_discrete_sequence= px.colors.qualitative.Set3_r)
    return fig


if __name__ == '__main__':
    app.run(debug=True)