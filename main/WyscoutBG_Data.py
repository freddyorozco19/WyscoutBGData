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


# Función para mostrar tarjetas
def metric_card(title, value):
    st.markdown(f"""
        <div style="
            background-color:#1c1c1c;
            padding:20px;
            border-radius:15px;
            text-align:center;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
            border: 1px solid #444;
            margin-bottom: 10px;
        ">
            <p style='margin:0; font-size:14px; color:#aaa'>{title}</p>
            <p style='margin:0; font-size:28px; font-weight:bold; color:#f5f5f5'>{value}</p>
        </div>
    """, unsafe_allow_html=True)

# Selección de jugador
player = st.selectbox("Selecciona un jugador", df["Player"].unique())
player_data = df[df["Player"] == player].iloc[0]

# Datos generales del jugador
col_info1, col_info2 = st.columns([3, 1])
with col_info1:
    st.markdown(f"### {player_data['Full name']}")
    st.markdown(f"**Equipo:** {player_data['Team']}")
    st.markdown(f"**Posición:** {player_data['Primary position']}")
with col_info2:
    st.markdown(f"**Competition:** {player_data['Competition']}")

st.markdown("---")

# Métricas clave (puedes adaptar estos nombres si usas otros en el Excel)
col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)

with col1:
    metric_card("Goles", int(player_data.get("Goals", 0)))
with col2:
    metric_card("Asistencias", int(player_data.get("Assists", 0)))
with col3:
    metric_card("xG", int(player_data.get("xG", 0)))
with col4:
    metric_card("xA", int(player_data.get("xA", 0)))
with col5:
    metric_card("Duels per 90", int(player_data.get("Duels per 90", 0)))
with col6:
    rating = round(player_data.get("Duels per 90", 0), 2)
    metric_card("Duels per 90", rating)
