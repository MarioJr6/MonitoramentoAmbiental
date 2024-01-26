import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import plotly.graph_objects as go
import streamlit_extras
import numpy as np

from plotly.subplots import make_subplots
from streamlit_extras.metric_cards import style_metric_cards

@st.cache_data
def fetch_and_clean_data(url):

  
  
    return data

d1 = fetch_and_clean_data(DATA_URL_1)
# Actually executes the function, since this is the first time it was
# encountered.

d2 = fetch_and_clean_data(DATA_URL_1)

