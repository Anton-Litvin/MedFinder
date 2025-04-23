import streamlit as st

# Заголовок страницы
st.set_page_config(page_icon="",layout="centered")
st.title("Вход в аккаунт")
# Функция для проверки логина и пароля
def authenticate(username, password):
    # Заглушка для проверки данных
    # В реальном приложении здесь можно подключить базу данных или API
    if username == "user" and password == "password":
        return True
    return False


# Создаём форму для входа
with st.form("login_form"):
    st.write("Пожалуйста, введите ваши данные для входа:")

    # Поле для ввода логина
    username = st.text_input("Логин")

    # Поле для ввода пароля
    password = st.text_input("Пароль", type="password")

    # Кнопка "Войти"
    submitted = st.form_submit_button("Войти")

    # Если форма отправлена
    if submitted:
        if authenticate(username, password):
            st.success("Вход выполнен успешно!")
            st.write("Перенаправление на главную страницу...")
            # Здесь можно добавить перенаправление на другую страницу
            # Например, с помощью st.experimental_set_query_params или st.session_state
        else:
            st.error("Неверный логин или пароль. Попробуйте снова.")

# Ссылка на регистрацию (опционально)
st.write("Ещё нет аккаунта? [Зарегистрируйтесь](#)")