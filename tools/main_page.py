import streamlit as st

st.set_page_config(page_icon="👋",layout="centered")
st.title("Добро пожаловать на MedFinder!👋")

if st.sidebar.button("Main"):
    st.switch_page("tools/main_page.py")
if st.sidebar.button("Search"):
    st.switch_page("tools/search_page.py")
if st.sidebar.button("Exit"):
    st.switch_page("tools/login_page.py")

st.markdown(
    """
## Раз уж вы сюда попали значит вам нужно найти необходимый медицинский препарат
- Для поиска перейдите в раздел "Поиск" 
- Для регистрации прейдите в раздел "Профиль"

![Логотип проекта](https://i.redd.it/odp5mi64gyy21.png)  
"""
)
