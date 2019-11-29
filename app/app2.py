import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import altair as alt
import json
import geopandas as gpd
import os
import dash_bootstrap_components as dbc

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
factors_data = pd.read_csv('../data/clean_data_line_plot.csv')

app = dash.Dash(__name__, assets_folder='assets')
server = app.server

app.title = 'Dash app with pure Altair HTML'

##wrangling for map
df = pd.read_csv("../data/clean_number-of-deaths-by-risk-factor.csv")

#source: https://www.naturalearthdata.com/downloads/110m-cultural-vectors/
#source:https://towardsdatascience.com/a-complete-guide-to-an-interactive-geographical-map-using-python-f4c5197e23e0
shapefile = '../data/geographic_data/ne_110m_admin_0_countries.shp'
gdf = gpd.read_file(shapefile)[['ADMIN', 'ADM0_A3', 'geometry']]
gdf.columns = ['country', 'country_code', 'geometry']
gdf.head()

df1 = df.query("year == 2017")
df1.drop(['country'], axis =1 ,inplace = True)
geo_df = gdf.merge(df1, left_on = 'country_code', right_on = 'code')
geo_df.drop(['code'], axis =1 ,inplace = True)
geo_df.iloc[:,4:] = geo_df.iloc[:,4:].div(geo_df.iloc[:,4:].sum(axis=1), axis=0)
# convert to json file
choro_json = json.loads(geo_df.to_json())
choro_data = alt.Data(values=choro_json['features'])

##wrangling ends

#draw_map() function
# source: https://medium.com/dataexplorations/creating-choropleth-maps-in-altair-eeb7085779a1 
def draw_map(cols = 'properties.high_blood_pressure', source = choro_data):
    """
    Draw heatmap for given quantitative value in world map
    
    Parameters:
    cols -- (string) columns in source
    source -- (json) data source
    
    Examples:
    draw_map('properties.smoking')
    
    """
    
    p_map = alt.Chart(source, 
                      title = "Global death percentage of {} over total death in 2017".format(cols[11:].replace('_',' '))
                     ).mark_geoshape(
        fill='lightgray',
        stroke='black'
    ).encode(
        alt.Color(cols, type='quantitative', 
                  scale=alt.Scale(scheme='yelloworangered'), 
                  title = "Proportion of death"),
         tooltip = [alt.Tooltip('properties.country:O', title = 'country'), 
                    alt.Tooltip('{}:Q'.format(cols), title = '{}'.format(cols[11:].replace('_',' ')), 
                                format = ".2%")]
    ).properties(width=800, height=450).configure_title(fontSize=25)
    return  p_map

#ends



selection = alt.selection_single()

#line_graph function
def line_graph(factor_name='high_blood_sugar', data=factors_data):
    '''
    plot the interactive line graph 
    '''
    line = alt.Chart(data).mark_line(point=True).add_selection(selection
).encode(
    alt.X("year:N", axis=alt.Axis(labelAngle=45)),
    alt.Y("{}:Q".format(factor_name),title="{}".format(factor_name.replace('_',' '))),
    alt.Tooltip(['year:N','continent:N', '{}:Q'.format(factor_name)]),
    color = alt.condition(selection, 'continent:N', alt.value('grey')),
    opacity = alt.condition(selection, alt.value(0.9), alt.value(0.2))
).properties(
    title="Trend of {} over time , 1990 - 2017".format(factor_name.replace("_"," ")),
    width=800,
    height=350).configure_title(fontSize=25
    ).configure_axis(
    labelFontSize=15,
    titleFontSize=20
)
    return line 

#layout starts
app.layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label='Overview', children=[
            html.Iframe(
            sandbox='allow-scripts',
            id='plot',
            height='600',
            width='950',
            style={'border-width': '0'},

            ################ The magic happens here
            srcDoc=open('../script/bar_chart.html').read()
            ################ The magic happens here
            ),
        ]),
        dcc.Tab(label='World Spread', children=[
           dcc.Dropdown(
            id='dd-chart',
            options=[
                    {'label': 'High blood pressure', 'value': 'properties.high_blood_pressure'},
                    {'label': 'smoking', 'value': 'properties.smoking'},
                    {'label': 'High blood sugar', 'value': 'properties.high_blood_sugar'},
                    {'label': 'Air pollution outdoor & indoor', 'value': 'properties.air_pollution_outdoor_&_indoor'},
                    {'label': 'Obesity', 'value': 'properties.obesity'},
                
                ],
                value='properties.high_blood_pressure', #setting default value
                style=dict(width='45%',
                        verticalAlign="middle")
            ),

            html.Iframe(
                sandbox='allow-scripts',
                id='plot_map',
                height='500',
                width='1100',
                style={'border-width': '0'},

                ################ The magic happens here
                srcDoc=draw_map().to_html()
                ################ The magic happens here
            ),
        ]),
        dcc.Tab(label='Trend', children=[

            html.Iframe(
                sandbox='allow-scripts',
                id='line_plot',
                height='500',
                width='1000',
                style={'border-width': '0'},

                ################ The magic happens here
                srcDoc=line_graph().to_html()
                ################ The magic happens here
                ),

            dcc.RadioItems(
            id='line-fcts',
            options=[
                    {'label': 'High blood pressure', 'value': 'high_blood_pressure'},
                    {'label': 'smoking', 'value': 'smoking'},
                    {'label': 'High blood sugar', 'value': 'high_blood_sugar'},
                    {'label': 'Air pollution outdoor & indoor', 'value': 'air_pollution_outdoor_&_indoor'},
                    {'label': 'Obesity', 'value': 'obesity'},
                    
                ],
                
                value = "high_blood_pressure",
                labelStyle={'display': 'inline-block'}
                ),

        ])
    ], colors={
            "border": "white",
            "primary": "gold",
            "background": "cornsilk"
        }),
        html.Div(id='tabs-content-props')
], style={'textAlign':'center'})


@app.callback(
    dash.dependencies.Output('plot_map', 'srcDoc'),
    [dash.dependencies.Input('dd-chart', 'value')])

def update_map(column_name):
    '''
    Takes in an xaxis_column_name and calls make_plot to update our Altair figure
    '''
    updated_map = draw_map(column_name).to_html()
    return updated_map  

@app.callback(
    dash.dependencies.Output('line_plot', 'srcDoc'),
    [dash.dependencies.Input('line-fcts', 'value')])

def update_line_graph(factor_name):
    '''
    Takes in a factor_name and calls line_graph to update the Altair figure
    '''
    updated_line_graph = line_graph(factor_name).to_html()
    return updated_line_graph

if __name__ == '__main__':
    app.run_server(debug=True)