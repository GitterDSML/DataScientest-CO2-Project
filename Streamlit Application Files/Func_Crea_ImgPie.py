#!/usr/bin/env python
# coding: utf-8

# In[20]:




import plotly.graph_objects as go
import plotly.io as pio
#pio.renderers.default = "svg"

def Func_Crea_ImgPie(df_grouped, Title):
    fig = go.Figure(data=[go.Pie(labels=df_grouped['Energy'], values=df_grouped['Volumen'])])
    fig.update_layout(title=Title)
    
    pio.write_image(fig, 'grafico.png')

    return 'grafico.png'

