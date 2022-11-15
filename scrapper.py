from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd 
import streamlit as st

@st.cache(persist=True)
def df_builder(): 
    url = "https://www.linkedin.com/jobs/search?keywords=Desenvolvedor%20J%C3%BAnior&location=Brazil&locationId=&geoId=106057199&f_TPR=r2592000&f_WT=2&f_E=1%2C2&position=1&pageNum=0"


    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    wd = webdriver.Chrome(executable_path='./chromedriver.exe', options=op)


    wd.get(url)


    number_of_jobs = int(wd.find_element(By.CLASS_NAME, "results-context-header__job-count").text)

    i = 2
    while i <= int(number_of_jobs/25)+1:
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        i = i +1
        try:
            wd.find_element(By.XPATH, '//*[@id="main-content"]/section[2]/button').click()
            time.sleep(3)
        except:
            pass
            time.sleep(3)



    jobs_list = wd.find_element(By.CLASS_NAME, "jobs-search__results-list")
    jobs = jobs_list.find_elements(By.TAG_NAME, "li")


    
    jobs_title= []
    empresa = []
    localizacao = []
    data = []
    link = []


    
    for job in jobs:   
            
        job_title0 = job.find_element(By.TAG_NAME, "h3").text
        jobs_title.append(job_title0)

        empresa0 = job.find_element(By.TAG_NAME, "h4").text
        empresa.append(empresa0)
            
        localizacao0 = job.find_element(By.CLASS_NAME, "job-search-card__location").text
        localizacao.append(localizacao0)

        
        data0 = job.find_element(By.TAG_NAME, 'time').get_attribute("datetime")
        data.append(data0)
            
        link0 = job.find_element(By.TAG_NAME, "a").get_attribute("href")
        link.append(link0)

    



    df_jobs = pd.DataFrame({"Vaga": jobs_title, "Empresa": empresa, "Localização": localizacao, "Data Postada": data, "Link": link})   
    return df_jobs