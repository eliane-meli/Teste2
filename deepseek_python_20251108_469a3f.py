import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import calendar

# Configuração da página
st.set_page_config(
    page_title="Dashboard de Análise de Expedidos",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Dados fixos do arquivo CSV
data = {
    'Data': ['02/04/2025', '03/04/2025', '04/04/2025', '05/04/2025', '06/04/2025', '07/04/2025', '08/04/2025', '09/04/2025', '10/04/2025', 
             '11/04/2025', '12/04/2025', '13/04/2025', '14/04/2025', '15/04/2025', '16/04/2025', '17/04/2025', '18/04/2025', '19/04/2025', 
             '20/04/2025', '21/04/2025', '22/04/2025', '23/04/2025', '24/04/2025', '25/04/2025', '26/04/2025', '27/04/2025', '28/04/2025', 
             '29/04/2025', '30/04/2025', '01/05/2025', '02/05/2025', '03/05/2025', '04/05/2025', '05/05/2025', '06/05/2025', '07/05/2025', 
             '08/05/2025', '09/05/2025', '10/05/2025', '11/05/2025', '12/05/2025', '13/05/2025', '14/05/2025', '15/05/2025', '16/05/2025', 
             '17/05/2025', '18/05/2025', '19/05/2025', '20/05/2025', '21/05/2025', '22/05/2025', '23/05/2025', '24/05/2025', '25/05/2025', 
             '26/05/2025', '27/05/2025', '28/05/2025', '29/05/2025', '30/05/2025', '31/05/2025', '01/06/2025', '02/06/2025', '03/06/2025', 
             '04/06/2025', '05/06/2025', '06/06/2025', '07/06/2025', '08/06/2025', '09/06/2025', '10/06/2025', '11/06/2025', '12/06/2025', 
             '13/06/2025', '14/06/2025', '15/06/2025', '16/06/2025', '17/06/2025', '18/06/2025', '19/06/2025', '20/06/2025', '21/06/2025', 
             '22/06/2025', '23/06/2025', '24/06/2025', '25/06/2025', '26/06/2025', '27/06/2025', '28/06/2025', '29/06/2025', '30/06/2025', 
             '01/07/2025', '02/07/2025', '03/07/2025', '04/07/2025', '05/07/2025', '06/07/2025', '07/07/2025', '08/07/2025', '09/07/2025', 
             '10/07/2025', '11/07/2025', '12/07/2025', '13/07/2025', '14/07/2025', '15/07/2025', '16/07/2025', '17/07/2025', '18/07/2025', 
             '19/07/2025', '20/07/2025', '21/07/2025', '22/07/2025', '23/07/2025', '24/07/2025', '25/07/2025', '26/07/2025', '27/07/2025', 
             '28/07/2025', '29/07/2025', '30/07/2025', '31/07/2025', '01/08/2025', '02/08/2025', '03/08/2025', '04/08/2025', '05/08/2025', 
             '06/08/2025', '07/08/2025', '08/08/2025', '09/08/2025', '10/08/2025', '11/08/2025', '12/08/2025', '13/08/2025', '14/08/2025', 
             '15/08/2025', '16/08/2025', '17/08/2025', '18/08/2025', '19/08/2025', '20/08/2025', '21/08/2025', '22/08/2025', '23/08/2025', 
             '24/08/2025', '25/08/2025', '26/08/2025', '27/08/2025', '28/08/2025', '29/08/2025', '30/08/2025', '31/08/2025', '01/09/2025', 
             '02/09/2025', '03/09/2025', '04/09/2025', '05/09/2025', '06/09/2025', '07/09/2025', '08/09/2025', '09/09/2025', '10/09/2025', 
             '11/09/2025', '12/09/2025', '13/09/2025', '14/09/2025', '15/09/2025', '16/09/2025', '17/09/2025', '18/09/2025', '19/09/2025', 
             '20/09/2025', '21/09/2025', '22/09/2025', '23/09/2025', '24/09/2025', '25/09/2025', '26/09/2025', '27/09/2025', '28/09/2025', 
             '29/09/2025', '30/09/2025', '01/10/2025', '02/10/2025', '03/10/2025', '04/10/2025', '05/10/2025', '06/10/2025', '07/10/2025', 
             '08/10/2025', '09/10/2025', '10/10/2025', '11/10/2025', '12/10/2025', '13/10/2025', '14/10/2025', '15/10/2025', '16/10/2025', 
             '17/10/2025', '18/10/2025', '19/10/2025', '20/10/2025', '21/10/2025', '22/10/2025', '23/10/2025', '24/10/2025', '25/10/2025', 
             '26/10/2025', '27/10/2025', '28/10/2025', '29/10/2025', '30/10/2025', '31/10/2025', '01/11/2025', '02/11/2025', '03/11/2025', 
             '04/11/2025', '05/11/2025', '06/11/2025', '07/11/2025', '08/11/2025', '09/11/2025', '10/11/2025', '11/11/2025', '12/11/2025', 
             '13/11/2025'],
    'QNTD Expedida': [2475, 2104, 2960, 2400, 3882, 6137, 7809, 10649, 10911, 10044, 9370, 8178, 8845, 16321, 16301, 22098, 16711, 8158, 
                      14190, 12077, 16902, 27031, 25757, 26024, 22877, 19005, 19199, 29518, 31333, 35694, 27461, 31416, 26451, 24608, 53037, 
                      31399, 42348, 41256, 37706, 27944, 29067, 55238, 36637, 57576, 54880, 43901, 33928, 43772, 50505, 49801, 51256, 49193, 
                      40880, 30300, 39191, 50277, 43911, 43240, 47150, 31429, 28126, 40629, 52257, 46678, 43525, 51916, 47433, 35056, 45904, 
                      70762, 63275, 71986, 70669, 58450, 41919, 49248, 67547, 59803, 51564, 65863, 51052, 33571, 40996, 62804, 55694, 65200, 
                      65011, 52538, 48382, 36782, 60563, 59097, 70953, 66839, 58645, 40422, 52969, 60719, 53162, 79515, 72300, 77665, 45779, 
                      47015, 65396, 73325, 76125, 73145, 66633, 42648, 54540, 62050, 63390, 62544, 56525, 49127, 43766, 47988, 60906, 71523, 
                      62895, 64790, 60502, 42072, 44110, 58029, 72370, 65755, 65548, 58503, 42110, 44800, 57503, 64304, 62638, 72161, 61043, 
                      42482, 50566, 60000, 69955, 66098, 63987, 59159, 40647, 48719, 56355, 63364, 54576, 50932, 46893, 35800, 52025, 60263, 
                      65750, 68997, 73149, 58037, 51499, 44488, 63783, 72824, 70183, 66173, 50856, 41574, 57041, 62401, 69574, 67903, 57354, 
                      44531, 39775, 51783, 51278, 47651, 47560, 62118, 52940, 41625, 48424, 52264, 58446, 60936, 62987, 45656, 41033, 50760, 
                      58162, 69946, 67995, 37822, 38846, 30377, 60183, 62138, 65497, 69131, 58058, 42346, 45267, 29351, 37601, 68654, 53727, 
                      53592, 30993, 33038, 52061, 53389, 46707, 41444, 39357, 33519, 27605, 52288, None, None, None, None, None, None, None, 
                      None, None, None],
    'Dias da Semana': ['Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo', 
                       'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 
                       'Sabado', 'Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo', 'Segunda', 'Terça', 'Quarta', 
                       'Quinta', 'Sexta', 'Sabado', 'Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo', 'Segunda', 
                       'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 
                       'Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 
                       'Sexta', 'Sabado', 'Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo', 'Segunda', 'Terça', 
                       'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo', 
                       'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 
                       'Sabado', 'Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo', 'Segunda', 'Terça', 'Quarta', 
                       'Quinta', 'Sexta', 'Sabado', 'Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo', 'Segunda', 
                       'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 
                       'Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 
                       'Sexta', 'Sabado', 'Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo', 'Segunda', 'Terça', 
                       'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo', 
                       'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 
                       'Sabado', 'Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo', 'Segunda', 'Terça', 'Quarta', 
                       'Quinta', 'Sexta', 'Sabado', 'Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo', 'Segunda', 
                       'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 
                       'Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 
                       'Sexta', 'Sabado', 'Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo', 'Segunda', 'Terça', 
                       'Quarta', 'Quinta']
}

# Criar DataFrame
df = pd.DataFrame(data)

# Converter colunas de data
df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y', errors='coerce')

# Extrair mês e ano
df['Mês'] = df['Data'].dt.month
df['Ano'] = df['Data'].dt.year
df['Mês_Ano'] = df['Data'].dt.to_period('M')

# Ordem correta dos dias da semana
dias_ordem = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo']
df['Dias da Semana'] = pd.Categorical(df['Dias da Semana'], categories=dias_ordem, ordered=True)

# Filtrar apenas dados com quantidade expedida válida
df_valido = df[df['QNTD Expedida'].notna()].copy()

# Calcular métricas
total_expedido = df_valido['QNTD Expedida'].sum()
media_diaria = df_valido['QNTD Expedida'].mean()
media_mensal = df_valido.groupby('Mês_Ano')['QNTD Expedida'].mean().mean()
dias_com_dados = len(df_valido)

# Encontrar dia com maior e menor volume
dia_maior_volume = df_valido.loc[df_valido['QNTD Expedida'].idxmax()]
dia_menor_volume = df_valido.loc[df_valido['QNTD Expedida'].idxmin()]

# Calcular média por dia da semana
media_dia_semana = df_valido.groupby('Dias da Semana')['QNTD Expedida'].mean().reindex(dias_ordem)

# Calcular tendência (média móvel de 7 dias)
df_valido = df_valido.sort_values('Data')
df_valido['Media_Movel'] = df_valido['QNTD Expedida'].rolling(window=7, min_periods=1).mean()

# Interface do Streamlit
st.title("📊 Dashboard de Análise de Expedidos")
st.markdown("---")

# KPIs principais
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Expedido", f"{total_expedido:,.0f}".replace(",", "."))
    
with col2:
    st.metric("Média Diária", f"{media_diaria:,.0f}".replace(",", "."))
    
with col3:
    st.metric("Dias com Dados", dias_com_dados)
    
with col4:
    st.metric("Média Mensal", f"{media_mensal:,.0f}".replace(",", "."))

st.markdown("---")

# Gráficos
col1, col2 = st.columns(2)

with col1:
    st.subheader("Volume Expedido por Data")
    
    fig = px.line(df_valido, x='Data', y='QNTD Expedida',
                 title='Volume Diário Expedido',
                 labels={'QNTD Expedida': 'Quantidade Expedida', 'Data': 'Data'})
    
    # Adicionar média móvel
    fig.add_scatter(x=df_valido['Data'], y=df_valido['Media_Movel'],
                   mode='lines', name='Média Móvel (7 dias)',
                   line=dict(color='red', dash='dash'))
    
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Distribuição por Dia da Semana")
    
    fig = px.bar(x=media_dia_semana.index, y=media_dia_semana.values,
                title='Média de Volume por Dia da Semana',
                labels={'x': 'Dia da Semana', 'y': 'Quantidade Média'})
    
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

# Análise mensal
st.markdown("---")
st.subheader("Análise Mensal")

# Calcular totais mensais
mensal = df_valido.groupby('Mês_Ano').agg({
    'QNTD Expedida': ['sum', 'mean', 'count']
}).round(0)
mensal.columns = ['Total Mensal', 'Média Diária', 'Dias Úteis']
mensal = mensal.reset_index()
mensal['Mês_Ano'] = mensal['Mês_Ano'].astype(str)

col1, col2 = st.columns(2)

with col1:
    fig = px.bar(mensal, x='Mês_Ano', y='Total Mensal',
                title='Total Expedido por Mês',
                labels={'Total Mensal': 'Total Expedido', 'Mês_Ano': 'Mês'})
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = px.line(mensal, x='Mês_Ano', y='Média Diária',
                 title='Média Diária por Mês',
                 labels={'Média Diária': 'Média Diária', 'Mês_Ano': 'Mês'})
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

# Estatísticas detalhadas
st.markdown("---")
st.subheader("Estatísticas Detalhadas")

col1, col2 = st.columns(2)

with col1:
    st.write("**Dia com Maior Volume:**")
    st.write(f"- Data: {dia_maior_volume['Data'].strftime('%d/%m/%Y')}")
    st.write(f"- Dia: {dia_maior_volume['Dias da Semana']}")
    st.write(f"- Volume: {dia_maior_volume['QNTD Expedida']:,.0f}".replace(",", "."))
    
    st.write("**Dia com Menor Volume:**")
    st.write(f"- Data: {dia_menor_volume['Data'].strftime('%d/%m/%Y')}")
    st.write(f"- Dia: {dia_menor_volume['Dias da Semana']}")
    st.write(f"- Volume: {dia_menor_volume['QNTD Expedida']:,.0f}".replace(",", "."))

with col2:
    # Calcular estatísticas
    Q1 = df_valido['QNTD Expedida'].quantile(0.25)
    Q3 = df_valido['QNTD Expedida'].quantile(0.75)
    IQR = Q3 - Q1
    
    st.write("**Estatísticas Descritivas:**")
    st.write(f"- Média: {df_valido['QNTD Expedida'].mean():,.0f}".replace(",", "."))
    st.write(f"- Mediana: {df_valido['QNTD Expedida'].median():,.0f}".replace(",", "."))
    st.write(f"- Desvio Padrão: {df_valido['QNTD Expedida'].std():,.0f}".replace(",", "."))
    st.write(f"- Q1 (25%): {Q1:,.0f}".replace(",", "."))
    st.write(f"- Q3 (75%): {Q3:,.0f}".replace(",", "."))

# Tabela de dados
st.markdown("---")
st.subheader("Dados Detalhados")

# Filtros
st.write("**Filtros:**")
col1, col2, col3 = st.columns(3)

with col1:
    meses = st.multiselect("Selecionar Meses:", 
                          options=sorted(df_valido['Mês_Ano'].unique()),
                          default=sorted(df_valido['Mês_Ano'].unique()))

with col2:
    dias_semana = st.multiselect("Selecionar Dias da Semana:",
                                options=dias_ordem,
                                default=dias_ordem)

with col3:
    volume_min, volume_max = st.slider("Filtrar por Volume:",
                                      min_value=int(df_valido['QNTD Expedida'].min()),
                                      max_value=int(df_valido['QNTD Expedida'].max()),
                                      value=(int(df_valido['QNTD Expedida'].min()), 
                                             int(df_valido['QNTD Expedida'].max())))

# Aplicar filtros
df_filtrado = df_valido[
    (df_valido['Mês_Ano'].isin(meses)) &
    (df_valido['Dias da Semana'].isin(dias_semana)) &
    (df_valido['QNTD Expedida'] >= volume_min) &
    (df_valido['QNTD Expedida'] <= volume_max)
]

st.dataframe(df_filtrado[['Data', 'Dias da Semana', 'QNTD Expedida']].sort_values('Data', ascending=False), 
             use_container_width=True)

# Download dos dados filtrados
csv = df_filtrado[['Data', 'Dias da Semana', 'QNTD Expedida']].to_csv(index=False)
st.download_button(
    label="📥 Download dos Dados Filtrados",
    data=csv,
    file_name="dados_expedidos_filtrados.csv",
    mime="text/csv"
)

st.markdown("---")
st.write("Desenvolvido com Streamlit | Dados fixos do arquivo: Analise de Expedidos - Cópia de Expedido (2).csv")