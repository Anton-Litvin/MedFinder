from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys  # Импортируем Keys для работы с клавишами
import os
import time

# start web browser
# Указываем путь к chromedriver
chromedriver_path = os.path.join(os.getcwd(), "chromedriver")

# Создаем объект Service
service = Service(executable_path=chromedriver_path)

# Инициализация драйвера с использованием Service
driver = webdriver.Chrome(service=service)

# get source code
driver.get("https://apteka.ru/search/?q=аспирин")
time.sleep(2)
html = driver.page_source
body = driver.find_element(By.TAG_NAME, "body")  # Находим элемент body
body.send_keys(Keys.ESCAPE)  # Отправляем клавишу "Esc"
f = open("index.html","w")
f.write(html)

# close web browser
driver.close()