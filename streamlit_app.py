import pandas as pd
import requests
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

# Configurações da página, padrão para os dashs do setor
st.set_page_config(
    page_title="Demo Mario",
    page_icon="	:snake:",
    layout="wide",
    initial_sidebar_state='collapsed'
)
col1, col2, col3 = st.columns([1,4,1])

col1.image('https://github.com/MarioJr6/MonitoramentoAmbiental/blob/main/Logo%20CEVS.png?raw=true', width=200)
col2.title('Painel de Monitoramento Ambiental de SARS-CoV-2')
col3.image('https://github.com/MarioJr6/MonitoramentoAmbiental/blob/main/Logo%20Estado.png?raw=true', width=300)

coluna_filtro, coluna_grafico = st.columns([1,2])

# Leitura dos dados
df_casos = pd.read_table('https://docs.google.com/spreadsheets/d/e/2PACX-1vSB6M4e3McfIwkph-nzq_SefdhzGx_6ycMmj8SHTzcXYrkUMe1P7Nza6BpKPva_HUhpDXBgwKXrHREx/pub?output=tsv')
df_esgoto = pd.read_table('https://docs.google.com/spreadsheets/d/e/2PACX-1vTZfjxdY8_x5WNd9_NE3QQPeche-dMdY5KdvNpq8H4W-lmUTidwrKpV0uLzLtihV7UAPIl68WvugMsN/pub?gid=0&single=true&output=tsv')


with coluna_filtro: 
    df_esgoto
    df_casos

    
