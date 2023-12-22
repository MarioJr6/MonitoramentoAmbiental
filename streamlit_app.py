import pandas as pd
import requests
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

# Armazenando a url da fonte dos dados para leitura
url = 'https://ti.saude.rs.gov.br/covid19/download'
url2 = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTZfjxdY8_x5WNd9_NE3QQPeche-dMdY5KdvNpq8H4W-lmUTidwrKpV0uLzLtihV7UAPIl68WvugMsN/pub?gid=0&single=true&output=tsv'

# Realizando a a leitura dos dados de casos
df_casos = pd.read_csv(url, encoding="UTF-8", sep=";")

# Formatando para o tipo data
df_casos['DATA_SINTOMAS']=pd.to_datetime(df_casos['DATA_SINTOMAS'], format='%d/%m/%Y')
df_casos['DATA_CONFIRMACAO']=pd.to_datetime(df_casos['DATA_CONFIRMACAO'], format='%d/%m/%Y')

# Agrupando os dados de forma que eu tenha todas as datas do ano
grouped = pd.pivot_table(data=df_casos, index='DATA_SINTOMAS', columns='MUNICIPIO', values='CRITERIO', aggfunc='count').fillna(0).reset_index()

 Mantendo somente as colunas que desejo trabalhar
colunas = ['DATA_SINTOMAS', 'CAPÃO DA CANOA', 'CAXIAS DO SUL', 'PASSO FUNDO', 
           'SANTA MARIA', 'SANTA ROSA', 'SÃO LEOPOLDO', 'TORRES']
grouped = grouped[colunas]

# Realizando o meu filtro temporal
grouped = grouped[grouped['DATA_SINTOMAS']>='2023-01-01']
