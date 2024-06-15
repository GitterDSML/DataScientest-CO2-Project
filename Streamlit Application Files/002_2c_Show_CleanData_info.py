#!/usr/bin/env python
# coding: utf-8
# In[3]:


#################################################################################
###        Read  All_Countries.csv 
###   This is countries  Clean Files concatenated in previous process.
###   To Draw a pie char to show some inf as repartition by energy.
##################################################################################
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


# Read the CSV files into a DataFrame        
Cleanfiles = "All_Countries.csv"

df_All = pd.read_csv(Cleanfiles, dtype={'Constructor': str, 'Brand': str})

df_grouped = df_All.groupby(['Country']).size().reset_index(name='Volumen')
Title = "All Countries Vehicles by Energy"

fig = px.pie(df_grouped, values='Volumen', names='Country', title= Title, width=800, height=800, hole=0.3)
fig.update_traces(textposition='outside', textinfo='percent+label+value')

fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig.update_layout(title_x=0.5)
st.plotly_chart(fig)

df_grouped = df_All.groupby(['year']).size().reset_index(name='Volumen')
Title = "All Countries Vehicles by Year"

fig = px.pie(df_grouped, values='Volumen', names='year', title= Title, width=800, height=800, hole=0.3)
fig.update_traces(textposition='outside', textinfo='percent+label+value')

fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig.update_layout(title_x=0.5)

st.plotly_chart(fig)


