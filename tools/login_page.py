import streamlit as st
import sqlite3 as sql
from hashlib import sha256

class RegAuth():
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def register_user(self):
        # Хешируем пароль
        password_hash = sha256(self.password.encode()).hexdigest()
        
        conn = sql.connect('./MedFinder/tools/auth.db')
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
            INSERT INTO users (login, password_hash)
            VALUES (?, ?)
            ''', (self.login, password_hash))
            
            conn.commit()
            return True
        except sql.IntegrityError:
            return False
        finally:
            conn.close()

    def authenticate_user(self):
        # Хешируем введенный пароль для сравнения
        password_hash = sha256(self.password.encode()).hexdigest()
        
        conn = sql.connect('./MedFinder/tools/auth.db')
        cursor = conn.cursor()
        
        cursor.execute('''
        SELECT id, login FROM users 
        WHERE login = ? AND password_hash = ?
        ''', (self.login, password_hash))
        
        user = cursor.fetchone()
        conn.close()
        
        if user:
            return True
        else:
            return False

# Инициализация состояния
if "page" not in st.session_state:
    st.session_state.page = "reg"

# Функции для смены страниц
def go_to_reg():
    st.session_state.page = "reg"

def go_to_auth():
    st.session_state.page = "auth"

# Отображение текущей "страницы"
if st.session_state.page == "reg":
    st.title("Регистрация")
    reg = st.form('reg_form')

    login = reg.text_input('Логин:')
    password = reg.text_input('Пароль:')

    submit = reg.form_submit_button(f'Подтвердить')
    auth = reg.form_submit_button("Авторизация", on_click=go_to_auth)

    if login != '' and password != '':
        proc = RegAuth(login, password)
        if proc.register_user() and submit:
            st.success("Пользователь успешно зарегистрирован")
        elif not(proc.register_user()) and submit:
            st.error("Ошибка: пользователь с таким логином уже существует")
    

elif st.session_state.page == "auth":
    st.title("Авторизация")
    auth = st.form('auth_form')

    login = auth.text_input('Логин:')
    password = auth.text_input('Пароль:')

    submit = auth.form_submit_button(f'Подтвердить')
    reg = auth.form_submit_button("Регистрация", on_click=go_to_reg)

    if login != '' and password != '':
        proc = RegAuth(login, password)
        if proc.authenticate_user() and submit:
            st.switch_page("tools/main_page.py")
        elif not(proc.authenticate_user()) and submit:
            st.error("Ошибка аутентификации: неверный логин или пароль")