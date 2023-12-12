#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import seaborn as sns
import matplotlib.pyplot as plt
import imageio
import os
import pandas as pd
import numpy as np
from matplotlib.colors import ListedColormap


Lucas_2018 = pd.read_csv('Cleaned_2018.csv')
#Physicochemical properties with their description and SI units
property_units = {'P': {'description': 'Phosphorus Content', 'unit': 'mg/kg'}, 'N': {'description': 'Total Nitrogen Content', 'unit': 'g/kg'},
    'K': {'description': 'Extractable Potassium Content', 'unit': 'mg/kg'},'CaCO3': {'description': 'Carbonates Content', 'unit': 'g/kg'},
    'pH_CaCl2': {'description': 'pH in CaCl2 solution', 'unit': ''},'pH_H2O': {'description': 'pH in soil-water suspension', 'unit': ''}}

output_directory = 'density_plots/'
os.makedirs(output_directory, exist_ok=True)
images = []

for land_use_system in land_use_systems:
    land_use_data = Lucas_2018[Lucas_2018['Land Use'] == land_use_system]
    land_use_data = land_use_data.fillna(0)
    land_use_data[properties_to_visualize] = land_use_data[properties_to_visualize].apply(pd.to_numeric, errors='coerce')

    # centering the map by calculating the latitude and longitude means
    center_latitude = land_use_data['LAT'].mean()
    center_longitude = land_use_data['LONG'].mean()

    # Creating the map using
    for idx, property_name in enumerate(properties_to_visualize):
        land_use_data[property_name] = land_use_data[property_name].fillna(0)

        fig, ax = plt.subplots(figsize=(12, 8))
        cmap = sns.light_palette("seagreen", as_cmap=True, reverse=False, n_colors=100)
        cmap = ListedColormap(cmap(np.arange(cmap.N))[:-20, :])
        sns.scatterplot(data=land_use_data, x='LONG', y='LAT', hue=property_name, size=property_name, sizes=(20, 200), palette=cmap, ax=ax, linewidths=np.log1p(land_use_data[property_name]), edgecolor='grey', vmin=0)
        
        property_description = property_units[property_name]['description']
        property_unit = property_units[property_name]['unit']

        ax.set_title(f'Distribution of {property_description} ({property_unit}) in {land_use_system}')
        ax.set_xlabel('Longitude')
        ax.set_ylabel(f'{property_description} ({property_unit})')
        ax.get_xaxis().set_ticks([])

        
        legend = ax.legend(title=property_description, bbox_to_anchor=(1.05, 1), loc='upper left')
        legend.set_title(property_description)
        legend.set_bbox_to_anchor((1.02, 1))
        
        ax.axis('off')
        
        # Saving the scatter plot as an image
        img_path = f'{output_directory}{land_use_system}_{property_name}_scatter.png'
        plt.savefig(img_path, bbox_inches='tight', pad_inches=0)
        plt.close()

        # Add the saved image to GIF
        images.append(imageio.imread(img_path))

gif_path = f'{output_directory}distribution_plots.gif'
imageio.mimsave(gif_path, images, duration=2)

