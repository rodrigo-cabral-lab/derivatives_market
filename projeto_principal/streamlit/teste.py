import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# escrevendo um título na página
st.title('Minha primeira aplicação :sunglasses:')

st.title('Lula 2022!!!')

st.title('Fora Bozo!!!')

# filtros para a tabela
checkbox_mostrar_tabela = st.sidebar.checkbox('Mostrar tabela')
if checkbox_mostrar_tabela:

    st.sidebar.markdown('## Filtro para a tabela')

    categorias = list(dados['Categoria'].unique())
    categorias.append('Todas')

    categoria = st.sidebar.selectbox('Selecione a categoria para apresentar na tabela', options = categorias)

    if categoria != 'Todas':
            df_categoria = dados.query('Categoria == @categoria')
            mostra_qntd_linhas(df_categoria)      
    else:
            mostra_qntd_linhas(dados)