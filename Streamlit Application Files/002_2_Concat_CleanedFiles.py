#!/usr/bin/env python
# coding: utf-8
# In[3]:

#################################################################################
###           Concat_CleanedFiles
###   Read  Countries Cleaned files in previous process.
###   Concatenate them in a global "All_countries" file.
###   delete unnamed if exists.
###   in case of existing rows without country or energy, this rows are deleted
###   --  Use a function to draw a pie char with energy repartition by energy.
##################################################################################
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
#import Func_DrawPie

# Read the CSV files into a DataFrame        
Cleanfiles = [r"C:\Users\mied1\02 - Proyecto DataScientest\CleanedFiles\ES_Cleaned.csv",
              r"C:\Users\mied1\02 - Proyecto DataScientest\CleanedFiles\FR_Cleaned.csv",
              r"C:\Users\mied1\02 - Proyecto DataScientest\CleanedFiles\DT_Cleaned.csv",
              r"C:\Users\mied1\02 - Proyecto DataScientest\CleanedFiles\IT_Cleaned.csv",
              r"C:\Users\mied1\02 - Proyecto DataScientest\CleanedFiles\PT_Cleaned.csv"]

df_All = pd.DataFrame([]) 
i=0

for file in Cleanfiles:    
   
     df_Clean = pd.read_csv(file, dtype={'Constructor': str, 'Brand': str})
  
     df_Clean =df_Clean.dropna(subset=['Country'])
     df_Clean =df_Clean.dropna(subset=['Energy'])
     #df_Clean =df_Clean.dropna(subset=['CO2_wltp'], inplace=True)
     df_Clean['CO2_wltp'] = df_Clean['CO2_wltp'].fillna(0)
 
     if "Unnamed: 0" in df_Clean.columns:
        df_Clean = df_Clean.drop("Unnamed: 0", axis=1)             
         
     df_Clean['CO2_wltp_quartiles'] = pd.qcut(df_Clean['CO2_wltp'], q=4)
     df_Clean['CO2_Qtls'] = pd.qcut(df_Clean['CO2_wltp'], q=4, labels=['1', '2', '3', '4'])

     df_All = pd.concat([df_All, df_Clean])  
     #df_Clean.to_csv(file, index=False)   

     #df_grouped = df_Clean.groupby(['Country', 'Energy']).size().reset_index(name='Volumen')
  
     #Country = df_Clean["Country"].unique()
     #Title =str(Country) + " Vehicles by Energy"
#     Func_DrawPie.Func_DrawPie (df_grouped, Title )  

     print(df_Clean.shape)    
