import streamlit as st
import requests
import json
st.set_page_config(layout="wide")
st.title("Поиск")

if st.sidebar.button("Main"):
    st.switch_page("tools/main_page.py")
if st.sidebar.button("Search"):
    st.switch_page("tools/search_page.py")
if st.sidebar.button("Exit"):
    st.switch_page("tools/login_page.py")

phram_searh = st.text_input("Введите имя препарата, которое хотите найти")
if st.button("Поиск"):
    try:
        pharms = requests.post("http://127.0.0.1:8000/pars", params={"pharm_name": phram_searh})
        pharms_data = pharms.json()
        col1,col2 ,col3 =st.columns(3)
        with col1:
            st.header(f"{phram_searh} в Apteka.ru")
            for i in range (len(pharms_data["apteka_ru_data"])):
                tile = col1.container(height=400)
                tile.write(f'[{pharms_data["apteka_ru_data"][i]["name"]}]({pharms_data["apteka_ru_data"][i]["url"]})')
                tile.image(pharms_data["apteka_ru_data"][i]["image_url"])
                tile.write(pharms_data["apteka_ru_data"][i]["price"]+' рублей')
        with col2:
            st.header(f"{phram_searh} в Stolichki.ru")
            for j in range (0,len(pharms_data["stolichki_ru_data"]),2):
                tile = col2.container(height=400)
                tile.write(f'[{pharms_data["stolichki_ru_data"][j]["name"]}]({pharms_data["stolichki_ru_data"][j]["url"]})')
                tile.image(pharms_data["stolichki_ru_data"][j//2]["image_url"])
                tile.write(pharms_data["stolichki_ru_data"][j//2]["price"]+' рублей')
        with col3:
            st.header(f"{phram_searh} в Rigla.ru")
            for k in range (len(pharms_data["rigla_ru_data"])):
                tile = col3.container(height=400)
                tile.write(f'[{pharms_data["rigla_ru_data"][k]["name"]}]({pharms_data["rigla_ru_data"][k]["url"]})')
                tile.image(pharms_data["rigla_ru_data"][k]["image_url"])
                tile.write(pharms_data["rigla_ru_data"][k]["price"]+' рублей')
    except requests.exceptions.JSONDecodeError :
        st.error("Ничего не найдено")