import streamlit as st
import sqlite3 as sql

def create_database():
    # Подключаемся к базе данных (или создаем новую)
    conn = sql.connect('./MedFinder/tools/auth.db')
    cursor = conn.cursor()
    
    # Создаем таблицу пользователей
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL)
                   ''')
    
    conn.commit()
    conn.close()

create_database()

main_page = st.Page("tools/main_page.py", title="Главная страница")
search_page = st.Page("tools/search_page.py", title="Поиск")
login_page = st.Page("tools/login_page.py",title="Аккаунт")
pg = st.navigation([login_page, main_page, search_page], position="hidden")
pg.run()