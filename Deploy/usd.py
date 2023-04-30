#importar dados de usd
#Conversor de Moedas: O Conversor de Moedas realiza o Web Scrapping do sistema de mesmo nome do Banco Central. Permite que seja importado as #cotações diárias de diversas moedas diante do real. Para saber as moedas que são possíveis de importar, e consequentemente seus respectivos #símbolos, utiliza-se a função currency.get_currency_list().
from bcb import currency
from bcb import sgs
import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import altair as alt
import plotly.figure_factory as ff


lista_moeda = currency.get_currency_list()

#criando um dataframe com dados diários do dolar
usd = currency.get(['USD'], start='2019-01-01', end='2022-07-14')

#criando dataframe com dados mensais de ipca 
ipca = sgs.get({'IPCA':433}, start='2019-01-01', end='2022-07-01')
#adicionando uma coluna do acumulado do ipca
ipca['ipca_acumulado'] = ipca['IPCA'].cumsum()


st.header("Gráfico do USD")

st.line_chart(usd)

st.header("Gráfico do IPCA e IPCA acumulado")

st.line_chart(ipca)