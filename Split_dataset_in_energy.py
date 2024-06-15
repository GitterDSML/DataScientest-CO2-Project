#!/usr/bin/env python
# coding: utf-8

# In[45]:


#############################################################
####   Import libraries 
#############################################################

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px

#############################################################
####   Load CO2 File and split by Energy.
#############################################################

Cleanfiles =( r"C:\Users\mied1\02 - Proyecto DataScientest\CleanedFiles\All_Countries.csv")
df = pd.read_csv(Cleanfiles)
C =  df.groupby(['Energy']).Energy.count()

#df_Electric      = df[df.Energy == 'electric']
#df_Electric.to_csv('df_Electric.csv', index=False, encoding='utf-8-sig')

df_Petrol        = df[df.Energy == 'petrol']
df_Petrol.to_csv('df_Petrol.csv', index=False, encoding='utf-8-sig')

df_Diesel        = df[df.Energy == 'diesel']
df_Diesel.to_csv('df_Diesel.csv', index=False, encoding='utf-8-sig')

df_Hibrid_Petrol = df[df.Energy == 'hybrid petrol']
df_Hibrid_Petrol.to_csv('df_Hibrid_Petrol.csv', index=False, encoding='utf-8-sig')

df_Hibrid_Diesel = df[df.Energy == 'hybrid diesel']
df_Hibrid_Diesel.to_csv('df_Hibrid_Diesel.csv', index=False, encoding='utf-8-sig')

df_lpg = df[df.Energy == 'lpg']
df_lpg.to_csv('df_lpg.csv', index=False, encoding='utf-8-sig')


# In[146]:


print( "\n ---- total: " ,df.shape[0],
      "\n" ,"df_Petrol       : " ,df_Petrol.shape[0],
      "\n" ,"df_Diesel       : " ,df_Diesel.shape[0],
      "\n" ,"df_Hibrid_Petrol: " ,df_Hibrid_Petrol.shape[0],
      "\n" ,"df_Hibrid_Diesel: " ,df_Hibrid_Diesel.shape[0],
      "\n" ,"df_lpg        : " ,df_lpg.shape[0])


# In[148]:


import geopandas as gpd
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

lineas_por_pais = df['Country'].value_counts()

# Leer los límites de los países
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Filtrar los países europeos
europa = ['Spain', 'France', 'Germany', 'Portugal', 'Italy', 'Belgium']
world = world[world['name'].isin(europa)]

# Asignar un valor a cada país
values = {'Spain': 'ES', 'France': 'FR', 'Germany': 'DE', 'Portugal': 'PT', 'Italy': 'IT', 'Belgium': 'BE'}
world['value'] = world['name'].map(values)
world = world.merge(lineas_por_pais, left_on='value', right_on='Country')

# Crear el mapa con Plotly Express
fig_map = px.choropleth(world, geojson=world.geometry, locations=world.index, color=world['count'],
color_continuous_scale='Blues', projection='natural earth',
hover_data={'count': True})

fig_map.update_geos(fitbounds="locations", visible=False)

fig_map.show()


# In[149]:


# Crear la tabla con Plotly Graph Objects
table = go.Table(
header=dict(values=['País', 'Count']),
cells=dict(values=[world['name'], world['count']])
)

# Crear la figura que contiene el mapa y la tabla
fig = go.Figure(data=[fig_map.data[0], table])

# Ajustar el estilo de la tabla para que coincida con el mapa
fig.update_traces(
selector=dict(type='table'),
header=dict(fill=dict(color='lightblue')),
cells=dict(fill=dict(color='white'))
)

# Ajustar el tamaño de la figura
fig.update_layout(
autosize=False,
width=800,
height=800
)

fig.show()

