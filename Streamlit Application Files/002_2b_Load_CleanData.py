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

df_All = None

# Verify if DF are already loaded, to don't rerun it again. 
Cleanfiles = "PT_Cleaned.csv"
#Cleanfiles = "All_Countries.csv"    
df_All = pd.read_csv(Cleanfiles, dtype={'Constructor': str, 'Brand': str})

st.write("Data is ready to start demo")
