import streamlit as st


main_page = st.Page("tools/main_page.py", title="Главная страница")
search_page = st.Page("tools/search_page.py", title="Поиск")
login_page = st.Page("tools/login_page.py",title="Аккаунт")
pg = st.navigation([main_page, search_page, login_page])
pg.run()