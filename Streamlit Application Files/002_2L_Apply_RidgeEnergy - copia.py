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
#----- 
# Create a figure and a grid of subplots
#----- 
num_rows = 2
num_cols = 3
fig, axs = plt.subplots(num_rows, num_cols, figsize=(12, 8))
#----- 

#for Ene in Energies:
ax = axs[i // num_cols, i % num_cols]
for i, Ene in enumerate(Energies):
# Select the current subplot
    


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
    df_Pred['Variation'] = df_Pred["Predicted_CO2"] - df_Pred['CO2_wltp']
#-- 
#-- update original dataset
#--    
    df_nuevo.loc[df_nuevo['Energy'] == Ene, "Predicted_CO2"] = df_Pred["Predicted_CO2"]
#-- 
#-- plot Variance
#--    

    fig, ax = plt.subplots()
    ax.hist(df_Pred['Variation'], bins=10)
    ax.set_xlabel('Prediction Vs Real Values difference')
    ax.set_ylabel('Num Obs')
    ax.set_title('Belgium prediction Vs Real Values '+Ene)
    ax.set_xlim(-50, 50)
    plt.tight_layout()
    plt.show()
    st.pyplot(fig)

#-- 
#-- Show info 
#--    
df_nuevo.groupby("Energy").agg({"CO2_wltp": ["min", "max", "mean"], "Predicted_CO2": ["min", "max", "mean"]})
st.write(df_nuevo.head(25))



