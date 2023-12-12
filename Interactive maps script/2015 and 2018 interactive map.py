#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import folium
import pandas as pd
import geopandas as gpd
from folium.plugins import MarkerCluster
from branca.colormap import linear
import os

LUCAS_unified = pd.read_csv('LUCAS_merged(2009,2015,2018).csv',low_memory = False)
years = [2015,2018]
countries = LUCAS_unified['Country'].unique()

os.makedirs('map', exist_ok=True)

for year in years:
    data_filtered = LUCAS_unified[LUCAS_unified['Year'] == year]
    gdf = gpd.GeoDataFrame(data_filtered, geometry=gpd.points_from_xy(data_filtered['LONG'], data_filtered['LAT']))
    gdf = gdf[gdf['Country'].isin(countries)]

    map_center = [data_filtered['LAT'].mean(), data_filtered['LONG'].mean()]
    m = folium.Map(location=map_center, zoom_start=6, control_scale=True)

    marker_cluster = MarkerCluster().add_to(m)
    for idx, row in gdf.iterrows():
        popup_html = f"<b>Country:</b> {row['Country']}<br><b>Year:</b> {row['Year']}<br>" \
                     f"<b>Latitude:</b> {row['LAT']}<br><b>Longitude:</b> {row['LONG']}<br>" \
                     f"<b>PTotal:</b> {row['PTotal']} (mg/kg)<br><b>N:</b> {row['N']} (g/kg)<br>" \
                     f"<b>P:</b> {row['P']} (mg/kg)<br><b>K:</b> {row['K']} (mg/kg)<br>" \
                     f"<b>CaCO3:</b> {row['CaCO3']} (g/kg)<br><b>Land Cover:</b> {row['Land Cover']}<br>" \
                     f"<b>Land Use:</b> {row['Land Use']}<br><b>EC:</b> {row['EC']} mS/m<br>" \
                     f"<b>OC:</b> {row['OC']} (g/kg)<br><b>pH_H2O:</b> {row['pH_H20']}"
        folium.Marker([row['LAT'], row['LONG']], popup=folium.Popup(popup_html, max_width=300)).add_to(marker_cluster)

    map_filename = os.path.join('maps', f'map_{year}.html')
    m.save(map_filename)

