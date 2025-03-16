import streamlit as st
import requests
st.title("Поиск")
phram_searh = st.text_input("Введите имя препарата, которое хотите найти")
if st.button("Поиск"):
    pharms = requests.post("http://127.0.0.1:8000/pars", params={"pharm_name": phram_searh})
    st.write(pharms.request.body)