import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

# Draw a pie Chart.

def Func_DrawPie (df_grouped, Title ):
    fig = px.pie(df_grouped, values='Volumen', names='Energy', title= Title, 
             width=500, height=400, hole=0.3, color_discrete_sequence=px.colors.qualitative.Plotly)
    fig.update_traces(textposition='outside', textinfo='percent+label+value')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    fig.update_layout(title_x=0.5)
#    st.plotly_chart(fig)
    return(fig)
