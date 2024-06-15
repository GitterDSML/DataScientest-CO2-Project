
# ##############   Fin trainning now apply to a new dataset #######################


from scipy.stats import pearsonr
from sklearn.linear_model import Ridge
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import joblib

Ene = selected_energy
Top_features = Selected_features

df_nuevo = pd.read_csv( r"C:\Users\mied1\02 - Proyecto DataScientest\CleanedFiles\BE_Cleaned.csv")
#----- 
df_Prediction = df_nuevo[df_nuevo['Energy'] == Ene]  
df_Pred = df_Prediction[Top_features]
#--
MyRidgeModel = joblib.load('Test_RidgeModel_'+Ene+'.plk')
   
#-- 
#-- apply model
#--    
df_Pred["Predicted_CO2"] = MyRidgeModel.predict(df_Pred)
df_Pred["CO2_wltp"] = df_nuevo["CO2_wltp"]                              
df_Pred['Variation'] = df_Pred["Predicted_CO2"] - df_Pred['CO2_wltp']
#-- 
#-- update original dataset
#--    
#df_nuevo = df_nuevo.loc[df_nuevo['Energy'] == Ene, "Predicted_CO2"] = df_Pred["Predicted_CO2"]
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

df_pred = df_Pred


