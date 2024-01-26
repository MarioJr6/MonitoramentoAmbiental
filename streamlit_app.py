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
  df_casos = pd.read_csv(url, encoding="UTF-8", sep=";")
  df_casos['DATA_SINTOMAS']=pd.to_datetime(df_casos['DATA_SINTOMAS'], format='%d/%m/%Y')
  df_casos['DATA_CONFIRMACAO']=pd.to_datetime(df_casos['DATA_CONFIRMACAO'], format='%d/%m/%Y')

  # Agrupando os dados de forma que eu tenha todas as datas do ano
  grouped = pd.pivot_table(data=df_casos, index='DATA_SINTOMAS', columns='MUNICIPIO', values='CRITERIO', aggfunc='count').fillna(0).reset_index()

  colunas = ['DATA_SINTOMAS', 'CAPÃO DA CANOA', 'CAXIAS DO SUL', 'PASSO FUNDO',
           'SANTA MARIA', 'SANTA ROSA', 'TORRES']
  grouped = grouped[colunas]

  return grouped

d1 = fetch_and_clean_data('https://ti.saude.rs.gov.br/covid19/download?2023')

d1 
# Actually executes the function, since this is the first time it was
# encountered.


