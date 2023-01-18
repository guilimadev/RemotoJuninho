import pandas as pd
import streamlit as st
import numpy as np


from estagioscrapper import df_builder_estagios
from scrapper import df_builder
from custom import df_builder_custom




from PIL import Image

st.set_page_config(layout="wide", page_title="Juninho From Home", page_icon=":house:")
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False









dev_jr, estagio, custom = st.tabs(["Junior Developer", "Remote Intern", "Custom Search"])


with st.sidebar:    
    st.title("Juninho From Home")
    image = Image.open('perfil2.jpg')
    st.image(image)
    st.write("Hello (world!), I'm Guilherme, IT Student at the UFRN and I developed this app as I was studying some python, web scraping and streamlit. Still need a lot of improvements but I'm work on it!")
    st.write("Feel free to use!")


with dev_jr:
    
    df_jobs = df_builder()    

    df_jobs = df_jobs.sort_values(by=['Data'], ascending=False)
    
    
    st.write('Number of jobs found: ' + str(len(df_jobs.index)))

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
            st.dataframe(df_jobs, 2000)
        else:
            st.dataframe(df_jobs[df_jobs['Vaga'] == job_selected], 2000) 
    else:
        if job_selected == "All":
            st.dataframe(df_jobs[df_jobs['Empresa'] == company_selected], 2000) 
        else:
            st.dataframe(df_jobs[(df_jobs['Empresa'] == company_selected) & (df_jobs['Vaga'] == job_selected)], 2000)

with estagio:  
    
    df_estagio = df_builder_estagios()    
    df_estagio = df_estagio.sort_values(by=['Data'], ascending=False)
    
    
    st.write('Number of jobs found: ' + str(len(df_estagio.index)))

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
            st.dataframe(df_estagio, 2000)
        else:
            st.dataframe(df_estagio[df_estagio['Vaga'] == job_selected], 2000) 
    else:
        if job_selected == "All":
            st.dataframe(df_estagio[df_estagio['Empresa'] == company_selected], 2000) 
        else:
            st.dataframe(df_estagio[(df_estagio['Empresa'] == company_selected) & (df_estagio['Vaga'] == job_selected)], 2000)
    

with custom:
    coltext = st.columns(1)
    with coltext:
        params = st.text_input("Type your search and press enter", '')   
    if params != '':   
        
        
        df_estagio = df_builder_custom(params)    
        df_estagio = df_estagio.sort_values(by=['Date'], ascending=False)
        
        
        st.write('Number of jobs founded: ' + str(len(df_estagio.index)))

        listof_companys = np.empty(1)
        listof_companys = np.append(listof_companys, "All")
        listof_companys = np.delete(listof_companys, 0)
        listof_companys = np.append(listof_companys, df_estagio.Company.unique()) 

        
        

        
        col1, col2 = st.columns(2)
        with col1:
            company_selected = st.selectbox(options=listof_companys, label="Select Company", key=4)
        with col2:
            listof_jobs = np.empty(1)
            listof_jobs  = np.append(listof_jobs, "All")
            listof_jobs  = np.delete(listof_jobs, 0)
            listof_jobs  = np.append(listof_jobs, df_estagio[df_estagio['Company'] == company_selected].Job.unique())    
            if company_selected != "All":       
                job_selected = st.selectbox(options=listof_jobs, label="Select Job", key=5)
            
            else:
                job_selected = st.selectbox(options=listof_jobs, label="Select Job", disabled=True, key=5)
            


        if company_selected == "All":
            if job_selected == "All":
                st.dataframe(df_estagio, 2000)
            else:
                st.dataframe(df_estagio[df_estagio['Job'] == job_selected], 2000) 
        else:
            if job_selected == "All":
                st.dataframe(df_estagio[df_estagio['Company'] == company_selected], 2000)
            else:
                st.dataframe(df_estagio[(df_estagio['Company'] == company_selected) & (df_estagio['Job'] == job_selected)], 2000)

