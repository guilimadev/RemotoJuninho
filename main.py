import pandas as pd
import streamlit as st
import numpy as np

from estagioscrapper import df_builder_estagios
from scrapper import df_builder
from custom import df_builder_custom

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False


st.set_page_config(layout="wide", page_title="Juninho From Home", page_icon=":house:")
 
dev_jr, estagio, custom = st.tabs(["Desenvolvedor Júnior", "Estágio Remoto", "Custom Search"])

with dev_jr:   
   
    df_jobs = df_builder()    
    df_jobs = df_jobs.sort_values(by=['Data'], ascending=False)
    
    
    st.write('Number of jobs founded: ' + str(len(df_jobs.index)))

    listof_companys = np.empty(1)
    listof_companys = np.append(listof_companys, "All")
    listof_companys = np.delete(listof_companys, 0)
    listof_companys = np.append(listof_companys, df_jobs.Empresa.unique()) 

    
    

    
    col1, col2 = st.columns(2)
    with col1:
        company_selected = st.selectbox(options=listof_companys, label="Select Company")
    with col2:
        listof_jobs = np.empty(1)
        listof_jobs  = np.append(listof_jobs, "All")
        listof_jobs  = np.delete(listof_jobs, 0)
        listof_jobs  = np.append(listof_jobs, df_jobs[df_jobs['Empresa'] == company_selected].Vaga.unique()) 

        if company_selected != "All":       
            job_selected = st.selectbox(options=listof_jobs, label="Select Job")
    
        else:
            job_selected = st.selectbox(options=listof_jobs, label="Select Job", disabled=True)
    


    if company_selected == "All":
        if job_selected == "All":
            st.dataframe(df_jobs)
        else:
            st.dataframe(df_jobs[df_jobs['Vaga'] == job_selected]) 
    else:
        if job_selected == "All":
            st.dataframe(df_jobs[df_jobs['Empresa'] == company_selected]) 
        else:
            st.dataframe(df_jobs[(df_jobs['Empresa'] == company_selected) & (df_jobs['Vaga'] == job_selected)])

with estagio:  
    
    df_estagio = df_builder_estagios()    
    df_estagio = df_estagio.sort_values(by=['Data'], ascending=False)
    
    
    st.write('Number of jobs founded: ' + str(len(df_estagio.index)))

    listof_companys = np.empty(1)
    listof_companys = np.append(listof_companys, "All")
    listof_companys = np.delete(listof_companys, 0)
    listof_companys = np.append(listof_companys, df_estagio.Empresa.unique()) 

    
    

    
    col1, col2 = st.columns(2)
    with col1:
        company_selected = st.selectbox(options=listof_companys, label="Select Company", key=3)
    with col2:
        listof_jobs = np.empty(1)
        listof_jobs  = np.append(listof_jobs, "All")
        listof_jobs  = np.delete(listof_jobs, 0)
        listof_jobs  = np.append(listof_jobs, df_estagio[df_estagio['Empresa'] == company_selected].Vaga.unique())    
        if company_selected != "All":       
            job_selected = st.selectbox(options=listof_jobs, label="Select Job", key=2)
        
        else:
            job_selected = st.selectbox(options=listof_jobs, label="Select Job", disabled=True, key=2)
        


    if company_selected == "All":
        if job_selected == "All":
            st.dataframe(df_estagio)
        else:
            st.dataframe(df_estagio[df_estagio['Vaga'] == job_selected]) 
    else:
        if job_selected == "All":
            st.dataframe(df_estagio[df_estagio['Empresa'] == company_selected]) 
        else:
            st.dataframe(df_estagio[(df_estagio['Empresa'] == company_selected) & (df_estagio['Vaga'] == job_selected)])
    

with custom:
    params = st.text_input("Pesquisa", '')
    if params != '':
        df_estagio = df_builder_custom(params)    
        df_estagio = df_estagio.sort_values(by=['Data'], ascending=False)
        
        
        st.write('Number of jobs founded: ' + str(len(df_estagio.index)))

        listof_companys = np.empty(1)
        listof_companys = np.append(listof_companys, "All")
        listof_companys = np.delete(listof_companys, 0)
        listof_companys = np.append(listof_companys, df_estagio.Empresa.unique()) 

        
        

        
        col1, col2 = st.columns(2)
        with col1:
            company_selected = st.selectbox(options=listof_companys, label="Select Company", key=4)
        with col2:
            listof_jobs = np.empty(1)
            listof_jobs  = np.append(listof_jobs, "All")
            listof_jobs  = np.delete(listof_jobs, 0)
            listof_jobs  = np.append(listof_jobs, df_estagio[df_estagio['Empresa'] == company_selected].Vaga.unique())    
            if company_selected != "All":       
                job_selected = st.selectbox(options=listof_jobs, label="Select Job", key=5)
            
            else:
                job_selected = st.selectbox(options=listof_jobs, label="Select Job", disabled=True, key=5)
            


        if company_selected == "All":
            if job_selected == "All":
                st.dataframe(df_estagio)
            else:
                st.dataframe(df_estagio[df_estagio['Vaga'] == job_selected]) 
        else:
            if job_selected == "All":
                st.dataframe(df_estagio[df_estagio['Empresa'] == company_selected]) 
            else:
                st.dataframe(df_estagio[(df_estagio['Empresa'] == company_selected) & (df_estagio['Vaga'] == job_selected)])

