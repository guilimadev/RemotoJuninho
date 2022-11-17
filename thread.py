import streamlit as st
from threading import Thread
from streamlit.runtime.scriptrunner import add_script_run_ctx

def target():
    st.text("thread")

t = Thread(target=target)
add_script_run_ctx(t)