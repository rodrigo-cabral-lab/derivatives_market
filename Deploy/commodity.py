#libs
import pandas as pd 
import os 
import numpy as np
from datetime import date
import matplotlib.pyplot as plt
import investpy
import streamlit as st
import matplotlib.dates as mpdates
import cufflinks as cf
import plotly.graph_objects as go
from plotly.offline import iplot, init_notebook_mode
import matplotlib.pyplot as plt
import plotly.io as pio




st.title("Preço de Commodities") 
st.header("Informações a Respeito do Fechamento e Volume das principais Commodities Brasileiras")

#BGI - Boi gordo
#ICF - cafe Arabico
#ETH - Etanol
#CCM - Milho
#SCJ - Soja
opcao = st.selectbox(
	'Escolha a Commodite',
	('BGI', 'ICF', 'ETH', 'CCM', 'SJC'))

if opcao == 'BGI':
  st.write('Você selecionou: Boi gordo')
elif opcao == 'ICF':
  st.write('Você selecionou: Cafe Arabico')
elif opcao == 'ETH':
  st.write('Você selecionou: Etanol')
elif opcao == 'CCM':
  st.write('Você selecionou: Milho')
elif opcao == 'SJC':
  st.write('Você selecionou: Soja')


if opcao:
 search_results = investpy.search_quotes(text = opcao, 
                                        products= ['commodities'], 
                                        countries= ['brazil'], 
                                        n_results = 50)
 for search_result in search_results:
  print(search_result)
 Df = search_result.retrieve_historical_data(from_date = '01/01/2019', to_date = '01/08/2022')

#Open	High	Low	Close	Volume	Change Pct

st.header("Gráfico de Fechamento")

st.line_chart(Df.Close)

st.header("Gráfico de Volume")

st.line_chart(Df.Volume)

fig = go.Figure(data=
    [go.Candlestick(x=Df.index,
                    open=Df["Open"],
                    high=Df["High"],
                    low=Df["Low"],
                    close=Df["Close"])]
)

fig.update_layout(
    title=f"{opcao}'  Candlestick - Preço da Commodity",
    yaxis_title="Price ($)"
)

st.plotly_chart(fig)
