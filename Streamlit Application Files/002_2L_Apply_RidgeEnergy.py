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
df_nuevo = pd.read_csv( r"/Users/livalacaisse/Documents/DataScience/CO2/RidgeModel_Code/BE_Cleaned.csv")
df_Scoring = pd.read_csv("ScoringRidgeEnergy.csv")
#----- 
SelectedVars = "ReductionsByEnergy.csv"
df_SelectedVars = pd.read_csv(SelectedVars)
Energies = df_SelectedVars["Energy"].unique()

#for Ene in Energies:

for  Ene in Energies:

#--  
    df_Prediction = df_nuevo[df_nuevo['Energy'] == Ene]
    df_Score = df_Scoring[df_Scoring['Energy'] == Ene]  
    st.write(df_Score)
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
    fig = px.histogram(df_Pred, x='Variation', nbins=10)
    fig.update_layout(
    xaxis_title='Prediction Vs Real Values difference',
    yaxis_title='Num Obs',
    title='Variance ' + Ene,
    xaxis_range=[-50, 50],
    bargap=0.1,
    template='plotly_dark'
    )

    st.plotly_chart(fig)


#-- 
#-- Show info 
#--    
#df_nuevo.groupby("Energy").agg({"CO2_wltp": ["min", "max", "mean"], "Predicted_CO2": ["min", "max", "mean"]})
#st.write(df_nuevo.head(25))
