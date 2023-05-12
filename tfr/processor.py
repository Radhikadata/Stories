import json
import os

import geopandas as gpd
import pandas as pd
import plotly.express as px

DATA_FOLDER = os.getcwd()
PREPROCESS_FOLDER  = f"{DATA_FOLDER}/preprocess"
OUTPUT_FOLDER = f"{DATA_FOLDER}/output"
INDIA_POLYGON = f"{PREPROCESS_FOLDER}/india-polygon.shp"
INDIA_POLYGON_GEOJSON = f"{PREPROCESS_FOLDER}/india-polygon.shp.json"
TFR_EXCEL = f"{DATA_FOLDER}/tfr/S4_4.xlsx"
STFR_HTML_OUTPUT = f'{OUTPUT_FOLDER}/tfr_index.html'

def dataprocees():
    map_df = gpd.read_file(INDIA_POLYGON)
    map_df.to_file(INDIA_POLYGON_GEOJSON, driver='GeoJSON')
    map_df.head()
    with open(INDIA_POLYGON_GEOJSON, 'r') as file:
       India_states = json.load(file)

    TFR_df = pd.read_excel(TFR_EXCEL)

    df1 = map_df.set_index('st_nm').join(TFR_df.set_index('State/union territory'))
    df1= df1.replace('na', 0)

    df1.head()

    df1.reset_index(level=0, inplace=True)


    df1 = df1.rename(columns={"st_nm": "State/UT"})
    df1.head()


    max_value = df1['TFR'].max()
    return (df1, max_value, India_states)

def mapperprocess(df1, max_value, India_states):

    fig = px.choropleth(df1, geojson=India_states, locations='State/UT',
    color='TFR', color_continuous_scale="matter", range_color=(0, max_value),
                        featureidkey="properties.st_nm", projection="gnomonic",
                        hover_data=['Year','TFR','State/UT'],title= 'Decline in TFR (acc to the existing State boundaries)',
                        animation_frame="Year", animation_group="State/UT")


    fig.update_geos(fitbounds="locations", resolution=50, visible=False)
    fig.update_layout= dict(title = 'State-wise TFR', font={'size':18, 'color':'#7f7f7f', 'family':'Courier New, monospace'},anchor='center',
                            geo = dict(showframe = True,projection = {'type':'equirectangular'}), height=500, figsize=(15, 15))


    fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 3000

    fig.write_html(STFR_HTML_OUTPUT)

    return fig