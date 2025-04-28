# -*- coding: utf-8 -*-
"""
Created on Mon Apr  28 18:05:41 2025
@author: Freddy J. Orozco R.
@Powered: WinStats.
"""

import streamlit as st
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
#from PIL import Image
from matplotlib.patches import Rectangle
import math
from PIL import Image

############################################################################################################################################################################################################################

im = Image.open("Resources/Isotipo-FF046.ico")
st.set_page_config(layout="wide", page_icon=im)
st.logo("Resources/Isotipo-FF046.png")
navigation_tree = {"Main": [
        st.Page("main/OptaEventingData.py", title="Eventing Data", icon=":material/download:"),
        st.Page("main/OptaJoinData.py", title="Join Data", icon=":material/cell_merge:"),
        st.Page("main/OptaExploreData.py", title="Explore Data", icon=":material/search_insights:"),
        st.Page("main/OptaExploreMatchData.py", title="Explore Match Data", icon=":material/search_insights:"),
        st.Page("main/OptaExploreTeamData.py", title="Explore Team Data", icon=":material/analytics:"),
        st.Page("main/OptaExploreLeagueData.py", title="Explore League Data", icon=":material/analytics:"),   
        st.Page("main/OptaProMatchData.py", title="Pro Match Data", icon=":material/leaderboard:"),
        st.Page("main/OptaRegisterData.py", title="Register Data", icon=":material/lists:")]}

nav = st.navigation(navigation_tree, position="sidebar")
nav.run()
