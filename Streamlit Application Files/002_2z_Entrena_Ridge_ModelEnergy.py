#################################################################################
###           Train and apply
##################################################################################
import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import pearsonr
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import joblib

#-------------- Variable comming from Streamlit 
Ene = selected_energy
Top_features = Selected_features
#---------------

#if Ene == "petrol" : Cleanfile = "df_Petrol.csv"
#if Ene == "diesel" : Cleanfile = "df_Diesel.csv"
#if Ene == "hybrid petrol" :Cleanfile = "df_Hibrid_Petrol.csv" 
#if Ene == "hybrid diesel" :Cleanfile = "df_Hibrid_Diesel.csv"
#if Ene == "lpg" : Cleanfile = "df_lpg.csv"

Cleanfile = "PT_Cleaned.csv"
st.write("cleanfile: "+Cleanfile)
df_Clean = pd.read_csv(Cleanfile)

#---------------

Target_Var = "CO2_wltp"
NumVar=12
Alpha=0.5
Splits=5
V_Country = "ALL_Countries"
model = Ridge(alpha=Alpha)
Redct_Type = "PCA"

#-------------- Variable comming from Streamlit 
Ene = selected_energy
Top_features = Selected_features
#---------------

df_energy = df_Clean[df_Clean['Energy'] == Ene]

result_df = pd.DataFrame(columns=["Reduction_type", "TargetVar", "Energy", "R2","RMSE"])

#-- Select vars needed for training model 
y_target = df_energy[Target_Var] 
X_features = df_energy[Top_features].copy() 
X_train, X_test, y_train, y_test = train_test_split(X_features, y_target, test_size=0.2)
 
#-- Train and predict results

model.fit(X_train, y_train)
joblib.dump(model, 'Test_RidgeModel_'+Ene+'.plk')
predictions = model.predict(X_test)  

results = pd.DataFrame({'Predict': predictions, 'Real values': y_test})

st.write(" ****************************************** ")
st.write(" Ridge Regression "+  Ene )
r2 = r2_score(y_test, predictions)
st.write(" R² score:", r2)
mse = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)
st.write(" RMSE:", rmse)
st.write(" ****************************************** ")

result_df = pd.concat([result_df, pd.DataFrame({'Reduction_type': [Redct_Type], 'TargetVar': [Target_Var], 'R2': [r2], 'Energy': [Ene], 'RMSE': [rmse]})], ignore_index=True)
