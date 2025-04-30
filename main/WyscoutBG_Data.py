import streamlit as st
#import hydralit_components as hc
import datetime
import base64
import pandas as pd
from io import BytesIO
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as mplt
import matplotlib.font_manager as font_manager
import mplsoccer
from mplsoccer import Pitch, VerticalPitch, FontManager
import sklearn
from sklearn.preprocessing import StandardScaler
from scipy.spatial import ConvexHull
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.patheffects as path_effects
from scipy.ndimage import gaussian_filter
import seaborn as sns
from matplotlib import colors as mcolors
import requests
from PIL import Image
from matplotlib.patches import Rectangle
import math
import io


########################################################################################################################################################################################################################################################################

font_path = 'Resources/keymer-bold.otf'  # Your font path goes here
font_manager.fontManager.addfont(font_path)
prop2 = font_manager.FontProperties(fname=font_path)

font_path2 = 'Resources/BasierCircle-Italic.ttf'  # Your font path goes here
font_manager.fontManager.addfont(font_path2)
prop3 = font_manager.FontProperties(fname=font_path2)

########################################################################################################################################################################################################################################################################

#with st.form(key='form4'):
    #uploaded_file = st.file_uploader("Choose a excel file", type="csv")
    #submit_button2 = st.form_submit_button(label='Aceptar')

with st.form(key='form4'):
    uploaded_file = st.file_uploader("Choose a excel file", type="xlsx")
    #DataMode = st.checkbox("Activate calculated columns")
    submit_button2 = st.form_submit_button(label='Aceptar')

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

#st.markdown("<style> div { text-align: center } </style>", unsafe_allow_html=True)
########################################################################################################################################################################################################################################################################

st.subheader("EXPLORE WY DATA")

########################################################################################################################################################################################################################################################################
# FILTROS

filteropt01, filteropt02, filteropt03 = st.columns(3)

with filteropt01:

    TeamList = df['Team'].drop_duplicates().tolist()
    TeamList.insert(0, "All Teams")  
    TeamSel = st.selectbox('Team', TeamList)
    dfbk_filteropt_01 = df
    if TeamSel == "All Teams":
        df = dfbk_filteropt_01
    else:
        df = df[df['Team'] == TeamSel].reset_index(drop=True)

with filteropt02:

    MinSel = st.slider('Minutes (%)', 0, 100)
    MaxMin = df['Minutes played'].max()
    MinSelT = (MinSel*MaxMin)/100
    df = df[df['Minutes played'] >= MinSelT].reset_index(drop=True)

with filteropt03:

    MaxAge = round(df['Age'].max())
    MinAge = round(df['Age'].min())
    AgeSel = st.slider('Age', MinAge, MaxAge, (MinAge, MaxAge), 1)
    #df = df[df['Age'] >= AgeSel].reset_index(drop=True)
    df = df[df['Age'] <= AgeSel[1]]
    df = df[df['Age'] >= AgeSel[0]].reset_index(drop=True)



########################################################################################################################################################################################################################################################################
# 

df['90s'] = round((df['Minutes played']/90), 2)
df = df[[col for col in df.columns if col != '90s'][:20] + ['90s'] + [col for col in df.columns if col != '90s'][20:]]
#df = df.drop(['Wyscout id', 'Team logo', 'Height', 'Weight']).reset_index(drop=True)
df = df.drop(['Wyscout id', 'Team logo', 'Height', 'Weight'], axis=1)

st.dataframe(df)


#
# Selección de jugador
player = st.selectbox("Selecciona un jugador", df["Player"].unique())
player_data = df[df["Player"] == player].iloc[0]

# Mostrar resumen
st.markdown("### Resumen del jugador")
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown(f"**{player_data['Full name']}**")
    st.markdown(player_data["Team"])
    st.markdown(player_data["Primary position"])
with col2:
    st.markdown(player_data["Competition"])

# KPIs principales
col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)
col1.metric("Goles", player_data["Goals"])
col2.metric("Asistencias", player_data["Assists"])
col3.metric("Pases", int(player_data["Duels per 90"]))
col4.metric("Entradas", int(player_data["Aerial duels per 90"]))
col5.metric("Intercepciones", int(player_data["xG"]))
col6.metric("Rating", round(player_data["xA"], 2))
