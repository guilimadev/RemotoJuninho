from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager





import time
import pandas as pd 
import streamlit as st

from datetime import datetime



def df_builder(): 
    url = "https://www.linkedin.com/jobs/search?keywords=Desenvolvedor%20J%C3%BAnior&location=Brazil&locationId=&geoId=106057199&f_TPR=r2592000&f_WT=2&f_E=1%2C2&position=1&pageNum=0"


    options = Options()
    options.add_argument("--headless") 
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-features=NetworkService")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--disable-features=VizDisplayCompositor")    
    wd = webdriver.Chrome(ChromeDriverManager().install(), options=options)


    wd.get(url)


    number_of_jobs = int(wd.find_element(By.CLASS_NAME, "results-context-header__job-count").text)

    
    
    i = 1
    scrap_text = st.empty()
    scrap_text.write("Scrapping Linkedin Jobs Page")

    bar = st.empty()
    bar.progress(0)
    while i <= int(number_of_jobs/25)+1:
        
        progress_bar = round((i* (100/ (number_of_jobs/25))))
        if progress_bar > 100:
            progress_bar = 100
        bar.progress(progress_bar)

        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        i = i +1
        try:
            wd.find_element(By.XPATH, '//*[@id="main-content"]/section[2]/button').click()
            time.sleep(2)
        except:
            pass
            time.sleep(2)


    bar.empty()
    scrap_text.empty()

    jobs_list = wd.find_element(By.CLASS_NAME, "jobs-search__results-list")
    jobs = jobs_list.find_elements(By.TAG_NAME, "li")


    
    jobs_title= []
    empresa = []   
    data = []
    link = []

    
    j = 1
    prep_test = st.empty()
    prep_test.write("Preparing Data Frame")
    bar2 = st.empty()
    bar2.progress(0)
    for job in jobs: 
           
        bar_progress = round((j * (100/len(jobs))))
        bar2.progress(bar_progress)
        job_title0 = job.find_element(By.TAG_NAME, "h3").text
        jobs_title.append(job_title0)

        empresa0 = job.find_element(By.TAG_NAME, "h4").text
        empresa.append(empresa0)          
           
        data1 = job.find_element(By.TAG_NAME, 'time').get_attribute("datetime")
        data.append(data1)
            
        link0 = job.find_element(By.TAG_NAME, "a").get_attribute("href")
        link.append(link0)
        j += 1
    

    bar2.empty()
    prep_test.empty()

    

    now = datetime.now()
    current_time = now.strftime("%d/%m/%Y - %H:%M:%S")
    st.write("Last Update: ", current_time)

    df_jobs = pd.DataFrame({"Vaga": jobs_title, "Empresa": empresa, "Data": data, "Link": link})   
    return df_jobs
    

