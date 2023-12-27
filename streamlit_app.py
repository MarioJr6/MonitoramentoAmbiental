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
df_esgoto = pd.read_table('https://docs.google.com/spreadsheets/d/e/2PACX-1vTZfjxdY8_x5WNd9_NE3QQPeche-dMdY5KdvNpq8H4W-lmUTidwrKpV0uLzLtihV7UAPIl68WvugMsN/pub?gid=0&single=true&output=tsv')
df_casos = pd.read_csv('https://ti.saude.rs.gov.br/covid19/download', encoding="UTF-8", sep=";")

# Formatando para o tipo data as colunas data de sintomas e confirmacao
df_casos['DATA_SINTOMAS']=pd.to_datetime(df_casos['DATA_SINTOMAS'], format='%d/%m/%Y')
df_casos['DATA_CONFIRMACAO']=pd.to_datetime(df_casos['DATA_CONFIRMACAO'], format='%d/%m/%Y')

# Agrupando os dados para eu possuir todas as data do ano
grouped = pd.pivot_table(data=df_casos, index='DATA_SINTOMAS', columns='MUNICIPIO', values='CRITERIO', aggfunc='count').fillna(0).reset_index()

# Lista das colunas que desejo trabalhar
colunas = ['DATA_SINTOMAS', 'CAPÃO DA CANOA', 'CAXIAS DO SUL', 'PASSO FUNDO',
           'SANTA MARIA', 'SANTA ROSA', 'SÃO LEOPOLDO', 'TORRES']

# Filtro das colunas que desejo manter e da minha linha temporal
grouped = grouped[colunas]
grouped = grouped[grouped['DATA_SINTOMAS']>='2023-01-01']

# Lista para selectbox
muni = ['CAPÃO DA CANOA', 'CAXIAS DO SUL', 'PASSO FUNDO','SANTA MARIA', 'SANTA ROSA', 'SÃO LEOPOLDO', 'TORRES']

# Formatacao dos meus dados e filtro temporal
df_esgoto['Data de coleta']=pd.to_datetime(df_esgoto['Data de coleta'], format='%d/%m/%Y')
df_esgoto['carga_viral_n1'] = df_esgoto['carga_viral_n1'].astype(float)
df_esgoto=df_esgoto[df_esgoto['Data de coleta']>='2023-01-01']

# Subplots para o gráfico
fig = make_subplots(specs=[[{"secondary_y": True}]])

with coluna_filtro: 
    municipio = st.selectbox('Selecione o município',muni)

    filtro = df_esgoto['Município']==municipio
    df_esgoto_filtrado = df_esgoto[filtro]

with coluna_grafico:
    fig = fig.add_trace(
      go.Scatter(x=grouped['DATA_SINTOMAS'], y=grouped[municipio], name="Casos diários", mode="lines"),
      secondary_y=True,
  )

    fig = fig.add_trace(
      go.Bar(x=df_esgoto_filtrado['Data de coleta'], y=df_esgoto_filtrado['carga_viral_n1'], name="Carga Viral no esgoto",
             ),
      secondary_y=False,
  )

    fig
    

    
