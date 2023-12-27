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

df_esgoto = pd.read_table('https://docs.google.com/spreadsheets/d/e/2PACX-1vTZfjxdY8_x5WNd9_NE3QQPeche-dMdY5KdvNpq8H4W-lmUTidwrKpV0uLzLtihV7UAPIl68WvugMsN/pub?gid=0&single=true&output=tsv')

muni = ['CAPÃO DA CANOA', 'CAXIAS DO SUL', 'PASSO FUNDO','SANTA MARIA', 'SANTA ROSA', 'SÃO LEOPOLDO', 'TORRES']

df_esgoto['Data de coleta']=pd.to_datetime(df_esgoto['Data de coleta'], format='%d/%m/%Y')
df_esgoto=df_esgoto[df_esgoto['Data de coleta']>='2023-01-01']
df_esgoto['carga_viral_n1'] = df_esgoto['carga_viral_n1'].astype(float)

fig = make_subplots(specs=[[{"secondary_y": True}]])

with coluna_filtro: 
    municipio = st.selectbox('Selecione o município',muni)

    filtro = df_esgoto['Município']==municipio
    df_esgoto_filtrado = df_esgoto[filtro]

with coluna_grafico: 
    fig.add_trace(
      go.Bar(x=df_esgoto_filtrado['Data de coleta'], y=df_esgoto_filtrado['carga_viral_n1'], name="Carga Viral no esgoto",
             ),
      secondary_y=False,
  )

    

    
