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
import os

@st.cache_data
@st.cache_resource

def cargar_fichero():
    df_All = pd.DataFrame()
    ### Update source file according to location
    Cleanfiles = "/Users/livalacaisse/Documents/DataScience/CO2/000-C02 First Delivery/Concatenate/PT_FR_ES_IT_DT.csv"
    
    # Debugging information
    print("Current working directory:", os.getcwd())
    print("File path being used:", os.path.abspath(Cleanfiles))
    print("File exists:", os.path.exists(Cleanfiles))
    
    try:
        df_All = pd.read_csv(Cleanfiles, dtype={'Constructor': str, 'Brand': str})
    except FileNotFoundError as e:
        st.error(f"File not found: {Cleanfiles}. Please check the path and file name.")
        st.stop()
    except Exception as e:
        st.error(f"An error occurred: {e}")
        st.stop()
    
    return df_All

df_All = cargar_fichero()

st.title(" CO2 project ")
st.sidebar.title("Table of contents")
pages = ["Introduction", "Dataset", "Preprocessing", "Data Visualization", "Modelling", "Predictions", "Apply Model", "Train & Predict","Refresh Data"]
#pages = ["Introduction", "Dataset", "Preprocessing", "Data Visualization", "SubMenu","Modelling", "Predictions", "Select Energy", "Compare", "Train & Predict","Refresh Data"]

page=st.sidebar.radio("Go to", pages)

#---------------------   Introduction 
if page == "Introduction" : 
  st.write("CO2 Use Case Introduction") 
  exec(open('Introduction.py').read()) 
  st.write("Video source: European Parliament Multimedia Centre ") 
  st.write("https://multimedia.europarl.europa.eu/en/video/v_N01_AFPS_230504_FIT1")
  exec(open('002_2b_Load_CleanData.py').read())
#---------------------   Show initial dataset information 
if page == "Dataset" : 

  st.write("### Dataset - Diego")

  col1, col2, col3 = st.columns((2,1,2))  

  col1.image('Mapa Europa.png')

  Select1 = col2.radio("Select an option", ["All Countries","All Energy" ,"Portugal", "Italy", "Germany", "France", "Spain"])
  if Select1   == "All Countries": image = Image.open('Pie_byCountry.png')
  elif Select1 == "All Energy": image = Image.open('Pie_byEnergy.png')
  elif Select1 == "Portugal":   image = Image.open('Pie_ptEnergy.png')
  elif Select1 == "Italy":      image = Image.open('Pie_itEnergy.png')
  elif Select1 == "Germany":    image = Image.open('Pie_deEnergy.png')
  elif Select1 == "France":     image = Image.open('Pie_frEnergy.png')
  elif Select1 == "Spain":      image = Image.open('Pe_esEnergy.png')

  col3.image(image, caption='Input data Summary', use_column_width=True)

#---------------------   Preprocessing
if page == "Preprocessing":
  st.write("Pre-processing - Diego")
  image = Image.open('CorrGlobal.png')
  st.image(image, caption='Globl Correlation Matrix', use_column_width=True)
#---------------------   Data Visualization
if page == "Data Visualization":

    with st.sidebar.expander("Subpages"):
        subpages = ["Overview", "Corelation Analysis", "Show Global file"]
        subpage = st.sidebar.radio("Go to", subpages)

    if subpage == "Overview":
      
        st.subheader("Data Set Profiling Report")
        st.write("Here will come the key refelctions and comentary")
        components.iframe("https://co2-viz-report.tiiny.site/", 1000, 1200, True)
        st.write("     ")      
        
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

    elif subpage == "Correlation Analysis":
        
      st.header("Correlations Analysis")
        
        #### Update the link depending on demonstration 
        #components.iframe('CO2_viz_report.html')
        
        
        progress_text = "Operation in progress. Please wait."


    elif subpage == "Show Global file":
        st.write("Data Examples and numbers")
        exec(open('002_2b_Show_CleanData_info.py').read())

    elif subpage == "ZZZ":
        st.write("Esta es la subpágina 2.3")
        exec(open('002_2b_Show_CleanData_info.py').read())
#---------------------    Creating modeling submenu 


#if page == SubMenu :    
#    st.write("Modeling - Liva")
#    with st.sidebar.expander("Subpages"):
#        Subpages = ["AAA", "BBB", "Show Global file", "??"]
#        subpage = st.sidebar.radio("Go to", Subpages)

#   if subpage == "AAA":
#        st.write("### XXXXXX")
#
#    elif subpage == "BBB":
#        st.write("### DataSet Summary")
#        progress_text = "Operation in progress. Please wait."
#        my_bar = st.progress(0, text=progress_text)
#
#        for percent_complete in range(100):
##            time.sleep(0.5)
#            my_bar.progress(percent_complete + 1, text=progress_text)
#
#        exec(open('002_2b_Show_CleanData_Piechart.py').read())
#        my_bar.empty()

  
#---------------------   Modeling 
if page =="Modelling":
    st.write("Modeling - Liva")
    with st.sidebar.expander("Subpages"):
        Subpages = ["AAA", "BBB", "Show Global file", "??"]
        subpage = st.sidebar.radio("Go to", Subpages)

    if subpage == "AAA":
        st.write("### XXXXXX")

    elif subpage == "BBB":
        st.write("### DataSet Summary")
       
        exec(open('002_2b_Show_CleanData_Piechart.py').read())
        my_bar.empty()

    elif subpage == "Show Global file":
        st.write(" Data Examples and numbers ")
        exec(open('002_2b_Show_CleanData_info.py').read())
# ---------------------   Predictions  
elif page == "Predictions" :  
         
     st.write("Predictions: Real vs Predicted values Variance")  
     exec(open('002_2L_Apply_RidgeEnergy.py').read())
# ---------------------   Select Energy

if page == "Apply Model" :   
     st.write("Applying trained model to a new Dataset (Belgium)" )
     
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

#if page == "Compare" :      
##     
#     col1, col2= st.columns((1, 2))
#
#     with col1:
#        df_SelectedVars = pd.read_csv("ReductionsByEnergy.csv")
#        selected_energy = st.radio("Select an energy", df_SelectedVars["Energy"].unique())

#        df_features = df_SelectedVars[df_SelectedVars['Energy'] == selected_energy]
#        Top_features = df_features["Selected_vars"].unique()
#        col1.write(Top_features)

#     # Mostrar el gráfico en la columna derecha
#     with col2:
#        exec(open('002_2N_ComparePred_realVal.py').read())
        
# ---------------------   Extras - re-train & apply
if page == "Train & Predict" : 
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


if page == "Refresh Data" :     
  Cleanfiles = "All_Countries.csv"    
  df_All = pd.read_csv(Cleanfiles, dtype={'Constructor': str, 'Brand': str})
