import streamlit as st

R_Variables =pd.read_csv( "ReductionsByEnergy.csv")
#R_Energies = R_Variables["Energy"].unique()

Ene = selected_energy

#for Ene in R_Energies:  

df_Energy = R_Variables.loc[R_Variables["Energy"] == Ene]
fig = px.line_polar(df_Energy, r='Importance', theta='Selected_vars', line_close=True, markers=True, template="plotly_dark")
fig.update_layout(title="\n Most important variables for: "+Ene+ "\n")
fig.update_polars(radialaxis_range=[0, 0.3])
fig.update_traces(marker=dict(color='red'), selector=dict(type='scatter', mode='markers'))

st.plotly_chart(fig)