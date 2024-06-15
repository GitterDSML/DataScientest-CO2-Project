import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
import subprocess
from PIL import Image
import plotly.express as px
import streamlit.components.v1 as components

st.title(" CO2 project ")
st.sidebar.title("Table of contents")
pages = ["Introduction", "Dataset", "Preprocessing", "Data Visualization", "SubMenu","Modelling", "Predictions", "Select Energy", "Compare", "Train & Predict","Refresh Data"]
page=st.sidebar.radio("Go to", pages)

#---------------------   Introduction 
if page == pages[0] : 
  st.write("CO2 Use Case Introduction") 
  exec(open('Introduction.py').read()) 
  st.write("Video source: European Parliament Multimedia Centre ") 
  st.write("https://multimedia.europarl.europa.eu/en/video/v_N01_AFPS_230504_FIT1")
  exec(open('002_2b_Load_CleanData.py').read())
#---------------------   Show initial dataset information 
if page == pages[1] : 

  st.write("### Dataset - Diego")

  col1, col2 = st.columns((1, 2))
  Select1 = col1.radio("Select an option", [1, 2, 3, 4, 5, 6, 7, 8])
  if Select1 == 1: image = Image.open('Pie_CountrybyYear.png')
  elif Select1 == 2: image = Image.open('Pie_byCountry.png')
  elif Select1 == 3: image = Image.open('Pie_byEnergy.png')
  elif Select1 == 4: image = Image.open('Pie_ptEnergy.png')
  elif Select1 == 5: image = Image.open('Pie_itEnergy.png')
  elif Select1 == 6: image = Image.open('Pie_deEnergy.png')
  elif Select1 == 7: image = Image.open('Pie_frEnergy.png')
  elif Select1 == 8: image = Image.open('Pe_esEnergy.png')

  col2.image(image, caption='Input data Summary', use_column_width=True)
#---------------------   Preprocessing
elif page == pages[2]:
  st.write("Pre-processing - Diego")
  image = Image.open('CorrGlobal.png')
  st.image(image, caption='Globl Correlation Matrix', use_column_width=True)
#---------------------   Data Visualization
elif page == pages[3]:
    st.header("### Visualisation - Liva")

    with st.sidebar.expander("Subpages"):
        subpages = ["Overview", "BBB", "Show Global file"]
        subpage = st.sidebar.radio("Go to", subpages)

    if subpage == "Overview":
      
        st.subheader("Data Set Profiling Report")
        st.write("Here will come the key refelctions and comentary")
        components.iframe("https://co2-viz-report.tiiny.site/", 1000, 1200, True)
        st.write("     ")
        st.subheader("Overview by country")
        st.image('Pie_byCountry.png')
        
        st.subheader("Overview by year")
        st.image('Pie_byYear.png')       
        
        st.subheader("Vehicles by Fuel Type in Different Territories")
        options = {
            "All countries": 'Pie_byEnergy.png',
            "Portugal": 'Pie_ptEnergy.png',
            "Italy": 'Pie_itEnergy.png',
            "Germany": 'Pie_deEnergy.png',
            "France": 'Pie_frEnergy.png',
            "Spain": 'Pie_esEnergy.png'
        }

        selected_option = st.selectbox("Select an option", list(options.keys()))
        image_path = options[selected_option]
        image = Image.open(image_path)
        st.image(image, caption='Input data Summary', use_column_width=True)

    elif subpage == "BBB":
        
        st.write("### DataSet Correlations")
        
        #### Update the link depending on demonstration 
        components.iframe('CO2_viz_report.html')
        progress_text = "Operation in progress. Please wait."


    elif subpage == "Show Global file":
        st.write("Data Examples and numbers")
        exec(open('002_2b_Show_CleanData_info.py').read())

    elif subpage == "ZZZ":
        st.write("Esta es la subpágina 2.3")
        exec(open('002_2b_Show_CleanData_info.py').read())
#---------------------    Creating modeling submenu 
elif page == pages[4] :    
    st.write("Modeling - Liva")
    with st.sidebar.expander("Subpages"):
        Subpages = ["AAA", "BBB", "Show Global file", "??"]
        subpage = st.sidebar.radio("Go to", Subpages)

    if subpage == "AAA":
        st.write("### XXXXXX")

    elif subpage == "BBB":
        st.write("### DataSet Summary")
        progress_text = "Operation in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.5)
            my_bar.progress(percent_complete + 1, text=progress_text)

        exec(open('002_2b_Show_CleanData_Piechart.py').read())
        my_bar.empty()
#---------------------   Modeling 
elif page == pages[5]:
    st.write("Modeling - Liva")
    with st.sidebar.expander("Subpages"):
        Subpages = ["AAA", "BBB", "Show Global file", "??"]
        subpage = st.sidebar.radio("Go to", Subpages)

    if subpage == "AAA":
        st.write("### XXXXXX")

    elif subpage == "BBB":
        st.write("### DataSet Summary")
        progress_text = "Operation in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.5)
            my_bar.progress(percent_complete + 1, text=progress_text)

        exec(open('002_2b_Show_CleanData_Piechart.py').read())
        my_bar.empty()

    elif subpage == "Show Global file":
        st.write(" Data Examples and numbers ")
        exec(open('002_2b_Show_CleanData_info.py').read())
# ---------------------   Predictions  
elif page == pages[6] :  
         
     st.write("Predictions")  
     exec(open('002_2L_Apply_RidgeEnergy.py').read())
# ---------------------   Select Energy
elif page == pages[7] :      
     
     col1, col2 = st.columns((5, 5))

     with col1:
        df_SelectedVars = pd.read_csv("ReductionsByEnergy.csv")
        selected_energy = st.radio("Select an energy", df_SelectedVars["Energy"].unique())

        df_features = df_SelectedVars[df_SelectedVars['Energy'] == selected_energy]
        Top_features = df_features["Selected_vars"].unique()
#        col1.write(Top_features)
 
        exec(open('Draw_Variables_Radar.py').read())

     with col2:
        exec(open('002_2M_Apply_RidgeOneEnergy.py').read())
# ---------------------   Compare 
elif page == pages[8] :      
     
     col1, col2= st.columns((1, 2))

     with col1:
        df_SelectedVars = pd.read_csv("ReductionsByEnergy.csv")
        selected_energy = st.radio("Select an energy", df_SelectedVars["Energy"].unique())

        df_features = df_SelectedVars[df_SelectedVars['Energy'] == selected_energy]
        Top_features = df_features["Selected_vars"].unique()
        col1.write(Top_features)

     # Mostrar el gráfico en la columna derecha
     with col2:
        exec(open('002_2N_ComparePred_realVal.py').read())
# ---------------------   Extras - re-train & apply
elif page == pages[9] : 
  col1, col2, col3 = st.columns((5,5,10))
  Ene = 'petrol'
  df_features = []
  Selected_features = []
  df_pred = pd.DataFrame()
  SelectedVars = "ReductionsByEnergy.csv"
  df_SelectedVars = pd.read_csv(SelectedVars)
  #df_SelectedVars = df_SelectedVars[df_SelectedVars['Reduction_type'] == 'PCA']

  with col1:
    selected_energy = st.radio("Select an energy", df_SelectedVars["Energy"].unique())
    Ene = selected_energy
    df_features = df_SelectedVars[df_SelectedVars['Energy'] == Ene]

    #st.write(df_features["Selected_vars"])

    Selected_features = st.multiselect("Select your Variables", df_features["Selected_vars"].unique(), key="Selected_vars")
    #st.write("Your selection is", Selected_features)
  with col2:
     if Selected_features:
      exec(open('002_2z_Entrena_Ridge_ModelEnergy.py').read())
  with col3:
    if Selected_features:
      exec(open('002_2z_Aplica_Ridge_ModelEnergy.py').read())

  #-- 
  #-- Show prediction data
  #--    
  if df_pred.empty:
      st.write("")
  else:
    st.write(df_pred)

elif page == pages[10] :     
  Cleanfiles = "All_Countries.csv"    
  df_All = pd.read_csv(Cleanfiles, dtype={'Constructor': str, 'Brand': str})
