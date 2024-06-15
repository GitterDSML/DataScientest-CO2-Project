#################################################################################
###         
###
##################################################################################
import streamlit as st  
import pandas as pd
import numpy as np
from scipy.stats import pearsonr
from sklearn.linear_model import Ridge
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

import joblib

#----- 
#----- 
df_nuevo = pd.read_csv( r"C:\Users\mied1\02 - Proyecto DataScientest\CleanedFiles\BE_Cleaned.csv")
#----- 
SelectedVars = "ReductionsByEnergy.csv"
df_SelectedVars = pd.read_csv(SelectedVars)
Energies = df_SelectedVars["Energy"].unique()

#for Ene in Energies:
Ene = selected_energy

#--  
df_Prediction = df_nuevo[df_nuevo['Energy'] == Ene]  
#--
MyRidgeModel = joblib.load('RidgeModel_'+Ene+'.plk')

df_features = df_SelectedVars[(df_SelectedVars['Energy'] == Ene )]
Top_features  = df_features["Selected_vars"].unique()    
df_Pred = df_Prediction[ df_features["Selected_vars"].unique()].copy()    
#-- 
#-- apply model
#--    
df_Pred["Predicted_CO2"] = MyRidgeModel.predict(df_Pred)
df_Pred["CO2_wltp"] = df_nuevo["CO2_wltp"]                 
df_Pred["Energy"] = df_nuevo["Energy"]                              
df_Pred['Variation'] = df_Pred["Predicted_CO2"] - df_Pred['CO2_wltp']
#-- 
#-- update original dataset
#--    
df_nuevo.loc[df_nuevo['Energy'] == Ene, "Predicted_CO2"] = df_Pred["Predicted_CO2"]
#-- 
#-- plot Variance
#--  
fig = px.scatter(df_Pred, x='CO2_wltp', y='Predicted_CO2', template='plotly_dark')
st.plotly_chart(fig)
#-- 
#-- Show info 
#--   
aggregated_dataO = df_Pred.groupby("Energy").agg({"CO2_wltp": ["min", "max", "mean"]})
st.write(aggregated_dataO.head(25))
aggregated_dataC = df_Pred.groupby("Energy").agg({ "Predicted_CO2": ["min", "max", "mean"]})
st.write(aggregated_dataC.head(25))

distinct_rows = df_Pred.drop_duplicates()
st.write(distinct_rows.head(25))
