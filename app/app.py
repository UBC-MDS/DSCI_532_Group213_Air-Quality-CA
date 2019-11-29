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



# path = '/users/sakiga/Desktop/MDS_Block3/LABS_532/Milestone1/DSCI_532_Group213_death_by_risk_factors/app'
# os.chdir(path)

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
                      title = "Death percentage of {} over total death among countries in 2017".format(cols[11:].replace('_',' '))
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
    ).properties(width=600, height=500)
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
    alt.Y("{}:Q".format(factor_name)),
    alt.Tooltip(['year:N','continent:N', '{}:Q'.format(factor_name)]),
    color = alt.condition(selection, 'continent:N', alt.value('grey')),
    opacity = alt.condition(selection, alt.value(0.9), alt.value(0.2))
).properties(
    title="Trend of {} over time , 1990 - 2017".format(factor_name.replace("_"," ")),
    width=600,
    height=320)
    return line 

app.layout = html.Div([

# structure the dashboard so you can add components into it
    ### ADD CONTENT HERE like: html.H1('text')
    html.H1('Death by Risk Factors'),
    html.H2('Death by risk factors in 2017'),
    html.Iframe(
        sandbox='allow-scripts',
        id='plot',
        height='600',
        width='700',
        style={'border-width': '0'},

        ################ The magic happens here
        srcDoc=open('bar_chart.html').read()
        ################ The magic happens here
        ),

    html.H2('map stuff'),

    dcc.Dropdown(
        id='dd-chart',
        options=[
            {'label': 'High blood pressure', 'value': 'properties.high_blood_pressure'},
            {'label': 'smoking', 'value': 'properties.smoking'},
            {'label': 'High blood sugar', 'value': 'properties.high_blood_sugar'},
            {'label': 'Air pollution outdoor & indoor', 'value': 'properties.air_pollution_outdoor_&_indoor'},
            {'label': 'Obesity', 'value': 'properties.obesity'},
            
            # Missing option here
        ],
        value='properties.high_blood_pressure', #setting default value
        style=dict(width='45%',
                   verticalAlign="middle")
        ),




    html.Iframe(
        sandbox='allow-scripts',
        id='plot_map',
        height='600',
        width='800',
        style={'border-width': '0'},

        ################ The magic happens here
        srcDoc=draw_map().to_html()
        ################ The magic happens here
        ),
    html.H2('Radio button'),
    dcc.RadioItems(
    id='line-fcts',
    options=[
            {'label': 'High blood pressure', 'value': 'high_blood_pressure'},
            {'label': 'smoking', 'value': 'smoking'},
            {'label': 'High blood sugar', 'value': 'high_blood_sugar'},
            {'label': 'Air pollution outdoor & indoor', 'value': 'air_pollution_outdoor_&_indoor'},
            {'label': 'Obesity', 'value': 'obesity'},
            
            # Missing option here
        ],
        
        value = "high_blood_pressure",
        labelStyle={'display': 'inline-block'}
        ),

    html.Iframe(
        sandbox='allow-scripts',
        id='line_plot',
        height='600',
        width='800',
        style={'border-width': '0'},

        ################ The magic happens here
        srcDoc=line_graph().to_html()
        ################ The magic happens here
        ),


  
        
        
])


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