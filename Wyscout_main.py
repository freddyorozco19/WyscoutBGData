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
        st.Page("main/WyscoutBG_Data.py", title="BG Data", icon=":material/leaderboard:"),
        st.Page("main/Wyscout_JoinData.py", title="Join Data", icon=":material/lists:")]}
nav = st.navigation(navigation_tree, position="sidebar")
nav.run()
