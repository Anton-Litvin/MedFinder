import streamlit as st
import requests
st.title("Поиск")
phram_searh = st.text_input("Введите имя препарата, которое хотите найти")
pharms = requests.post("http://127.0.0.1/pars",data={"pharm_name":phram_searh})