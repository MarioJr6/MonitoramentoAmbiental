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

# Armazenando a url da fonte dos dados para leitura
url = 'https://ti.saude.rs.gov.br/covid19/download'
url2 = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTZfjxdY8_x5WNd9_NE3QQPeche-dMdY5KdvNpq8H4W-lmUTidwrKpV0uLzLtihV7UAPIl68WvugMsN/pub?gid=0&single=true&output=tsv'

# Realizando a a leitura dos dados de casos
df_casos = pd.read_csv(url, encoding="UTF-8", sep=";")

# Leitura dos meus dados das coletas no esgoto
df_esgoto = pd.read_table(url2)

# Formatando para o tipo data
df_casos['DATA_SINTOMAS']=pd.to_datetime(df_casos['DATA_SINTOMAS'], format='%d/%m/%Y')
df_casos['DATA_CONFIRMACAO']=pd.to_datetime(df_casos['DATA_CONFIRMACAO'], format='%d/%m/%Y')

# Agrupando os dados de forma que eu tenha todas as datas do ano
grouped = pd.pivot_table(data=df_casos, index='DATA_SINTOMAS', columns='MUNICIPIO', values='CRITERIO', aggfunc='count').fillna(0).reset_index()

# Mantendo somente as colunas que desejo trabalhar
colunas = ['DATA_SINTOMAS', 'CAPÃO DA CANOA', 'CAXIAS DO SUL', 'PASSO FUNDO', 
          'SANTA MARIA', 'SANTA ROSA', 'SÃO LEOPOLDO', 'TORRES']
grouped = grouped[colunas]

# Realizando o meu filtro temporal
grouped = grouped[grouped['DATA_SINTOMAS']>='2023-01-01']

# Filtrando os Municípios
municipios = ['CAPÃO DA CANOA', 'CAXIAS DO SUL', 'PASSO FUNDO','SANTA MARIA', 
              'SANTA ROSA', 'SÃO LEOPOLDO', 'TORRES']
filtro_municipios = df_esgoto['Município'].isin(municipios)
df_esgoto[filtro_municipios]

# Limpeza dos dados
df_esgoto['Data de coleta']=pd.to_datetime(df_esgoto['Data de coleta'], format='%d/%m/%Y')
df_esgoto = df_esgoto[df_esgoto['Data de coleta']>='2023-01-01']

# Formatação para o tipo float
df_esgoto['carga_viral_n1'] = df_esgoto['carga_viral_n1'].astype(float)

with coluna_filtro: 
    muni = st.selectbox('Selecione o Município desejado', sorted(df_esgoto['Município'].unique())) 
