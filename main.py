import pandas as pd 
import streamlit as st
from scrapper import df_builder
from estagioscrapper import df_builder_estagios

st.title('Remoto para Juninho')

dev_jr, estagio = st.tabs(["Desenvolvedor Júnior", "Estágio Remoto"])

with dev_jr:
    df_jobs = df_builder()
    df_jobs = df_jobs.sort_values(by=['Data Postada'], ascending=False)
    st.dataframe(data=df_jobs, width=2000)

with estagio:
    df_estagio = df_builder_estagios()
    df_estagio = df_estagio.sort_values(by=['Data Postada'], ascending=False)
    st.dataframe(df_estagio)

