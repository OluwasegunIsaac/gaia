#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import folium
import geopandas as gpd
from folium.plugins import MarkerCluster
import os


LUCAS_unified = pd.read_csv('LUCAS_merged(2009,2015,2018).csv',low_memory = False)
year = 2009
countries = LUCAS_unified['Country'].unique()

# Create a directory to save the images
os.makedirs('maps', exist_ok=True)

# Filter data for the current year
data_filtered = LUCAS_unified[LUCAS_unified['Year'] == 2009]

# Creatig the GeoDataFrame for map
gdf = gpd.GeoDataFrame(data_filtered, geometry=gpd.points_from_xy(data_filtered['LONG'], data_filtered['LAT']))
gdf = gdf[gdf['Country'].isin(countries)]

# centering the mean of the coordinates for creation of the folium map
map_center = [data_filtered['LAT'].mean(), data_filtered['LONG'].mean()]
m = folium.Map(location=map_center, zoom_start=6, control_scale=True)
marker_cluster = MarkerCluster().add_to(m)

# pop-ups for each of the data geographic points
for idx, row in gdf.iterrows():
    popup_html = f"<b>Country:</b> {row['Country']}<br><b>Year:</b> {row['Year']}<br>" \
                 f"<b>Latitude:</b> {row['LAT']}<br><b>Longitude:</b> {row['LONG']}<br>" \
                 f"<b>PTotal:</b> {row['PTotal']} (mg/kg)<br>"
    folium.Marker([row['LAT'], row['LONG']], popup=folium.Popup(popup_html, max_width=300)).add_to(marker_cluster)

# Saaving the map as HTML file
map_filename = os.path.join('mapS', f'map_{year}.html')
m.save(map_filename)

