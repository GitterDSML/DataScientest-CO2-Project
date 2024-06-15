#################################################################################
###        Read  All_Countries.csv 
###   This is countries  Clean Files concatenated in previous process.
###   Showing some data examples and volumes
##################################################################################
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

# Verify if DF are already loaded, to don't rerun it again. 

#if df_All == None:
#    Cleanfiles = "All_Countries.csv"  
Cleanfiles = "PT_Cleaned.csv"    
df_All = pd.read_csv(Cleanfiles, dtype={'Constructor': str, 'Brand': str})

df_grouped = df_All.groupby(['Country']).size().reset_index(name='Volumen')
Title = "All Countries Dataset"
st.write(df_All.head(20))

col1, col2 = st.columns(2)
with col1: 
    st.write(df_grouped.head(20))
with col2: 
    df_grouped = df_All.groupby(['year']).size().reset_index(name='Volumen')
    st.write(df_grouped.head(20))
