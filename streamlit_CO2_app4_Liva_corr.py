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

# Custom CSS to increase the text section width
st.markdown(
    """
    <style>
    .reportview-container .main .block-container {
        max-width: 1200px;
        padding-left: 5%;
        padding-right: 5%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

@st.cache_data
@st.cache_resource

def cargar_fichero():
  df_All = pd.DataFrame()
#  Cleanfiles = "All_Countries.csv"   
  Cleanfiles = "/Users/livalacaisse/Documents/DataScience/CO2/000-C02 First Delivery/Cleaned_countries/Cl_no_FR/PT_Cleaned.csv"
  return(pd.read_csv(Cleanfiles, dtype={'Constructor': str, 'Brand': str}))

df_All = cargar_fichero()

st.title(" CO2 project ")
st.sidebar.title("Table of contents")
pages = ["Introduction", "Dataset", "Preprocessing", "Data Analysis", "Modelling", "Evaluate Predictions", "Apply Model", "Train & Predict"]
#pages = ["Introduction", "Dataset", "Preprocessing", "Data Visualization", "SubMenu","Modelling", "Predictions", "Select Energy", "Compare", "Train & Predict","Refresh Data"]

page=st.sidebar.radio("Go to", pages)

#---------------------   Introduction 
if page == "Introduction" : 
  st.write("Introduction") 
  exec(open('Introduction.py').read()) 
  st.write("Video source: European Parliament Multimedia Centre ") 
  st.write("https://multimedia.europarl.europa.eu/en/video/v_N01_AFPS_230504_FIT1")
  exec(open('002_2b_Load_CleanData.py').read())
#---------------------   Show initial dataset information 
if page == "Dataset" : 
#-   Add submenu  one for dataset description the other for this part
  st.write("Dataset")
  with st.sidebar.expander("Subpages"):
    Subpages = ["Data Statistics", "Data Audit","DataSet example"]
    subpage = st.sidebar.radio("Go to", Subpages)

  if subpage == "Data Statistics":
      from Func_DrawPie import Func_DrawPie      
            
      col1, col2, col3 = st.columns((2,1,2))  
      df_groupCountry = pd.read_csv("VolsByCountry.csv") 
      col1.image('Mapa Europa.png')    

      Select1 = col2.radio("Select an option", ["All Countries","All Energy" ,"Portugal", "Italy", "Germany", "France", "Spain"])
               
      if Select1 == "All Countries":  df_groupCountry = pd.read_csv("VolsByCountry.csv")      
      if Select1 == "All Energy":     df_groupCountry = pd.read_csv("VolsByEnergy.csv") 
      if Select1 == "Portugal":  df_groupCountry = pd.read_csv("group_5.csv")      
      if Select1 == "Italy":     df_groupCountry = pd.read_csv("group_4.csv") 
      if Select1 == "Germany":   df_groupCountry = pd.read_csv("group_3.csv") 
      if Select1 == "France":    df_groupCountry = pd.read_csv("group_2.csv") 
      if Select1 == "Spain":     df_groupCountry = pd.read_csv("group_0.csv") 
      
      Title = Select1
      col3.plotly_chart(Func_DrawPie(df_groupCountry,Title))
  
  if subpage == "Data Audit":
        
# Add the dataset description table
        st.write("### Original Dataset Description")
        dataset_description = {
            "FieldName": ["ID", "Country", "VFN", "Mp", "Mh", "Man", "MMS", "Tan", "T", "Go to", "Go to", "Mk", "Cn", "Ct", "Cr", "R", "M", "Mt", "Enedc", "Ewltp", "W", "At1", "At2", "Ft", "Fm", "ec", "ep", "z", "IT", "Ernedc", "Erwltp", "From", "Vf", "Status", "year", "registration", "Fuel consumption", "Electric range"],
            "Description": [
                "The type approval number of the vehicle type.",
                "Refers to the member state of the European Union in which the vehicle is registered.",
                "The identification number of the vehicle family to which the vehicle belongs.",
                "+++++ Description Mp",
                "The name of the vehicle manufacturer according to the European Union standard denomination.",
                "The name of the vehicle manufacturer according to the original equipment manufacturer's declaration.",
                "The name of the vehicle manufacturer according to the MS registry denomination.",
                "The type approval number of the vehicle type.",
                "Refers to the vehicle type, such as 'Car' or 'Motorcycle'.",
                "Is a specific variant of the vehicle model.",
                "Is the specific version of the vehicle model.",
                "Is the make of the vehicle.",
                "The commercial name of the vehicle.",
                "It is the category of the approved vehicle type.",
                "The category of the vehicle registered.",
                "(Mass in running order Completed/complete vehicle)",
                "+++++ Description M",
                "+++++ Description Mt",
                "The test mass of the vehicle.",
                "Specific CO2 emissions according to the test procedure.",
                "The wheelbase of the vehicle.",
                "The width of the steering axle of the vehicle.",
                "The width of the other axle of the vehicle.",
                "The type of fuel used by the vehicle.",
                "The fuel mode used by the vehicle.",
                "The capacity of the vehicle's engine in cubic centimeters.",
                "The vehicle's engine power in kilowatts.",
                "The electrical energy consumption of the vehicle in watt-hours per kilometer traveled.",
                "The innovative technology or group of innovative technologies used in the vehicle.",
                "CO2 emission reductions achieved by innovative technologies according to the NEDC test procedure.",
                "CO2 emission reductions achieved by innovative technologies according to the WLTP test procedure.",
                "The date of registration of the vehicle.",
                "The fuel consumption of the vehicle.",
                "Indicates whether the data is provisional (P) or final (F).",
                "The reporting year of the data.",
                "The date of registration of the vehicle.",
                "The fuel consumption of the vehicle.",
                "The electric autonomy of the vehicle in kilometers."
            ],
            "Type": ["int64", "object", "object", "object", "object", "object", "object", "object", "object", "object", "object", "object", "object", "object", "object", "int64", "int64", "float64", "float64", "float64", "float64", "float64", "float64", "object", "object", "float64", "float64", "float64", "object", "float64", "float64", "float64", "float64", "object", "int64", "object", "float64", "float64"],
            "Variable T": ["Quant", "Cat", "Cat", "Cat", "Cat", "Cat", "Cat", "Cat", "Cat", "Cat", "Cat", "Cat", "Cat", "Cat", "Cat", "Quant", "Quant", "Quant", "Quant", "Quant", "Quant", "Quant", "Quant", "Cat", "Cat", "Quant", "Quant", "Quant", "Cat", "Quant", "Quant", "Quant", "Quant", "Cat", "Cat", "Cat", "Quant", "Quant"]
        }
        dataset_description_df = pd.DataFrame(dataset_description)
        st.table(dataset_description_df)
                
  if subpage == "DataSet example":
        st.write( "Dataset content example")
        df_grouped = df_All.groupby(['Country']).size().reset_index(name='Volumen')
        st.write(df_All.head(25))

#---------------------   Preprocessing
if page == "Preprocessing":
  st.write("Pre-processing - Diego")
  image = Image.open('CorrGlobal.png')
  st.image(image, caption='Globl Correlation Matrix', use_column_width=True)
#---------------------   Data Visualization
if page == "Data Analysis":

  with st.sidebar.expander("Subpages"):
    subpages = ["Overview", "Correlation Analysis", "Show Global file"]
    subpage = st.sidebar.radio("Go to", subpages)

  if subpage == "Overview":
      
    st.subheader("Data Set Profiling Report")
    st.write("""
    - The cleaned dataset includes 24 variables: 12 numeric, 8 categorical, and 4 alphanumeric. It no longer has missing values.
    - The target variable, **CO2_wltp**, has a right-skewed distribution with a significant concentration of values between approximately 0 and 200, with a notable spike at 0 representing electric vehicles. This right-skewness suggests that rebalancing techniques might be necessary during preprocessing.
    - Skewness is also observed in all quantitative variables specific to fuel types (e.g., **Fuel consumption**, **Power_kw**). Therefore, we may need to assess these separately and consider modeling by fuel type, as different variables may be required.
    - There is an imbalance in the **Energy** (fuel type) variable, with a majority of vehicles being petrol and diesel, and the **Fuel mode** variable is skewed towards M (mono-fuel).
    - The dataset contains duplicates, which are naturally occurring since the same vehicle variant can be presented in the market multiple times.
    - The dataset represents 52 different brands, with **Volkswagen, Citroen, Renault, and Peugeot** among the largest, and includes 3,638 distinct models.
    - There are **911 vehicle types and 47,808 different versions** of vehicles. The high cardinality can be challenging for many machine learning algorithms because it can lead to a large number of features if one-hot encoding is applied, potentially causing overfitting and high computational costs. We need to analyze the relevance of these variables to avoid unnecessary complexity and overfitting risks.
    """)
    components.iframe("https://co2-viz-report.tiiny.site/", 1000, 1200, True)
    st.write("     ")
    #st.subheader("Overview by country")
    #st.image('Pie_byCountry.png')
        
    #st.subheader("Overview by year")
    #st.image('Pie_byYear.png')       
        
   #st.subheader("Vehicles by Fuel Type in Different Territories")
        ##options = {
        #   "All countries": 'Pie_byEnergy.png',
        #    "Portugal": 'Pie_ptEnergy.png',
        #    "Italy": 'Pie_itEnergy.png',
        #    "Germany": 'Pie_deEnergy.png',
        #    "France": 'Pie_frEnergy.png',
        #   "Spain": 'Pie_esEnergy.png'
        #}

    #selected_option = st.selectbox("Select an option", list(options.keys()))
    #image_path = options[selected_option]
    #image = Image.open(image_path)
    #st.image(image, caption='Input data Summary', use_column_width=True)

  elif subpage == "Correlation Analysis":
        
    st.header("Correlation Exploration")
    st.write("""
    As the next step, we explored the correlation. We discovered the following notable correlations:
    - **CO2_wltp (CO2 emissions) and Fuel consumption**: High positive correlation (**0.83**), suggesting that higher fuel consumption strongly correlates with higher CO2 emissions.
    - **CO2_wltp and El_Consumpt_whkm (Electric consumption)**: Strong negative correlation (**-0.81**), indicating that as electric consumption increases, CO2 emissions decrease, which is expected as electric vehicles produce zero emissions.
    - **CO2_wltp and Electric range (km)**: Moderate negative correlation (**-0.54**), suggesting that vehicles with a higher electric range tend to have lower CO2 emissions.
    
    Other notable correlations:
    - **Fuel consumption and Power_KW**: Moderate positive correlation (**0.59**), indicating that more powerful vehicles tend to consume more fuel.
    - **Engine_cm3 (Engine size) and Power_KW (Engine power)**: High correlation (**0.64**), indicating that larger engines tend to produce more power.
    """)
    glob_corr_url="https://lh3.googleusercontent.com/d/1NxmmKCLuH8SDSNxTcvHDhMXlazwx2ST5"
    st.image(glob_corr_url, caption='Description of the image', use_column_width=True)
 
    st.write("### Detailed Breakdown by Fuel Type")
    st.write("The detailed breakdown by fuel type highlights specific attributes influencing CO2 emissions across different vehicle categories, suggesting that we may need to apply tailored strategies for emission reduction based on fuel type.")
    
    st.write("**Diesel Vehicles**: Show strong positive correlations with vehicle mass, engine size, and axle width, while negative correlations with eco-innovation and newer models.")
    
    st.write("**Hybrid Diesel Vehicles**: Exhibit strong negative correlations with eco-innovation, expected range, and electric range, indicating advancements in these areas significantly reduce CO2 emissions.")
    
    st.write("**Hybrid Petrol Vehicles**: Similar to hybrid diesel, with additional notable negative correlation with year, suggesting newer models are more efficient.")
    
    st.write("**LPG Vehicles**: Show high positive correlations with engine size and power, with significant negative correlations with electric consumption and expected range.")
    
    st.write("**Petrol Vehicles**: Correlate strongly with power and fuel consumption, while eco-innovation and newer models negatively correlate with CO2 emissions.")  
    
    fuel_type = st.selectbox("Select a fuel type", ["Correlations all", "Correlations diesel", "Correlations petrol", "Correlations hybrid diesel", "Correlations hybrid petrol", "Correlations lpg"])

    if fuel_type == "Correlations all":
        st.image("https://lh3.googleusercontent.com/d/1sMcEfLF9X4ii5DHsJ6KN-iOyLDDy6F9h", caption="Correlations all", use_column_width=True)
    elif fuel_type == "Correlations diesel":
        st.image("https://lh3.googleusercontent.com/d/1pXyMGI172zm9Yw5RvqcSQtIkDk1ZmVUO", caption="Correlations diesel", use_column_width=True)
    elif fuel_type == "Correlations petrol":
        st.image("https://lh3.googleusercontent.com/d/1XuvdNPI2afdXN3UWZQGRm5ivcsBzc7OZ", caption="Correlations petrol", use_column_width=True)
    elif fuel_type == "Correlations hybrid diesel":
        st.image("https://lh3.googleusercontent.com/d/1mdKPunS58DuuIGzS5pCshoEJpAQc5i8l", caption="Correlations hybrid diesel", use_column_width=True)
    elif fuel_type == "Correlations hybrid petrol":
        st.image("https://lh3.googleusercontent.com/d/1fUGYbTtiqVFOLCu6Mu1VEk67eiTr-zxA", caption="Correlations hybrid petrol", use_column_width=True)
    elif fuel_type == "Correlations lpg":
        st.image("https://lh3.googleusercontent.com/d/1oY-I7zgACMz3ZuHmFTAKPmRQpt2zdl32", caption="Correlations lpg", use_column_width=True)

        
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
        exec(open('002_2b_Show_CleanData_Piechart.py').read())

    elif subpage == "Show Global file":
        st.write(" Data Examples and numbers ")
        exec(open('002_2b_Show_CleanData_info.py').read())
# ---------------------   Predictions  
elif page == "Evaluate Predictions" :  
         
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


#if page == "Refresh Data" :     
#  Cleanfiles = "All_Countries.csv"    
#  df_All = pd.read_csv(Cleanfiles, dtype={'Constructor': str, 'Brand': str})
