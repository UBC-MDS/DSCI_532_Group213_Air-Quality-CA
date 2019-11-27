import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__, assets_folder='assets')
server = app.server

app.title = 'Dash app with pure Altair HTML'

app.layout = html.Div([

# structure the dashboard so you can add components into it
    ### ADD CONTENT HERE like: html.H1('text')
    html.H1('Death by Risk Factors'),
    html.H2('Death by risk factors in 2017'),
    html.Iframe(
        sandbox='allow-scripts',
        id='plot',
        height='2000',
        width='1500',
        style={'border-width': '5px'},

        ################ The magic happens here
        srcDoc=open('bar_chart.html').read()
        ################ The magic happens here
        )
 
])

if __name__ == '__main__':
    app.run_server(debug=True)