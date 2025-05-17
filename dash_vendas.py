# importações
import pandas as pd
import plotly.express as px
import streamlit as st
from sqlalchemy import create_engine
import urllib

# Conexão com SQL Server usando SQLAlchemy
params = urllib.parse.quote_plus(
    "DRIVER={SQL Server};"
    "SERVER=TrabalhoGustavo;"
    "DATABASE=AdventureWorks2022;"
    "Trusted_Connection=yes;"
)

engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

# Consulta otimizada: apenas colunas necessárias, usando alias e filtros claros
query = """
SELECT
    soh.OrderDate,
    soh.TotalDue,
    ad.StateProvinceID AS Regiao,
    pr.Name AS ProductName,
    sod.OrderQty,
    sod.UnitPrice,
    sod.LineTotal
FROM
    Sales.SalesOrderHeader AS soh
INNER JOIN
    Sales.SalesOrderDetail AS sod ON soh.SalesOrderID = sod.SalesOrderID
INNER JOIN
    Production.Product AS pr ON sod.ProductID = pr.ProductID
INNER JOIN
    Person.Address AS ad ON soh.ShipToAddressID = ad.AddressID
"""

# Leitura dos dados com pandas
df = pd.read_sql(query, engine)
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

# Extração de ano e mês para análise temporal
df['Ano'] = df['OrderDate'].dt.year
df['Mes'] = df['OrderDate'].dt.month

# Dados agregados para visualizações
vendas_por_regiao_produto = df.groupby(['Regiao', 'ProductName'])[
    'LineTotal'].sum().reset_index()
vendas_por_tempo = df.groupby(['Ano', 'Mes'])['LineTotal'].sum().reset_index()
vendas_por_tempo['Data'] = pd.to_datetime(
    dict(year=vendas_por_tempo['Ano'], month=vendas_por_tempo['Mes'], day=1))

# Streamlit - Interface
st.title("Dashboard de Vendas - AdventureWorks")

# Filtros com seleção padrão
todos_produtos = sorted(df['ProductName'].unique())
todas_regioes = sorted(df['Regiao'].unique())

data_inicio = st.date_input("Data Início", df['OrderDate'].min())
data_fim = st.date_input("Data Fim", df['OrderDate'].max())

# Multiselect com opção de selecionar tudo
produtos_selecionados = st.multiselect(
    "Produtos", ["Selecionar todos"] + todos_produtos, default=["Selecionar todos"]
)
if "Selecionar todos" in produtos_selecionados:
    produtos_filtrados = todos_produtos
else:
    produtos_filtrados = produtos_selecionados

regioes_selecionadas = st.multiselect(
    "Regiões", ["Selecionar todos"] + todas_regioes, default=["Selecionar todos"]
)
if "Selecionar todos" in regioes_selecionadas:
    regioes_filtradas = todas_regioes
else:
    regioes_filtradas = regioes_selecionadas

# Aplicação dos filtros
df_filtrado = df[
    (df['OrderDate'] >= pd.to_datetime(data_inicio)) &
    (df['OrderDate'] <= pd.to_datetime(data_fim)) &
    (df['ProductName'].isin(produtos_filtrados)) &
    (df['Regiao'].isin(regioes_filtradas))
]

# KPIs
st.metric("Total de Vendas", f"${df_filtrado['LineTotal'].sum():,.2f}")

# Gráficos
grafico_produto = px.bar(
    vendas_por_regiao_produto,
    x='ProductName',
    y='LineTotal',
    color='Regiao',
    title='Vendas de Produtos por Região'
)

grafico_tempo = px.line(
    vendas_por_tempo,
    x='Data',
    y='LineTotal',
    title='Vendas ao Longo do Tempo'
)

st.plotly_chart(grafico_produto)
st.plotly_chart(grafico_tempo)
