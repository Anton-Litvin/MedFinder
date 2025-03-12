from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import os
import time

# Указываем путь к chromedriver
chromedriver_path = os.path.join(os.getcwd(), "chromedriver")

# Создаем объект Service
service = Service(executable_path=chromedriver_path)

# Инициализация драйвера с использованием Service
driver = webdriver.Chrome(service=service)

try:
    # 1. Переход на страницу
    driver.get("https://apteka.ru")

    # 2. Устанавливаем cookie или локальное хранилище для выбранного города
    # Пример для cookies (замените на актуальные данные для вашего сайта)
    driver.add_cookie({
        "name": "city_id",  # Имя cookie, которое хранит ID города
        "value": "Moscow",       # Значение (ID города, например, 1 для Москвы)
        "domain": "apteka.ru"
    })

    # 3. Переход на страницу поиска
    driver.get("https://apteka.ru/search/?q=аспирин")

    # 4. Ожидание 10 секунд (дополнительное время для загрузки страницы)
    time.sleep(10)

    # 5. Извлечение текста из всех доступных блоков
    product_names = driver.find_elements(By.CLASS_NAME, "catalog-car__name")
    product_prices = driver.find_elements(By.CLASS_NAME, "moneyprice__roubles")
    product_images = driver.find_elements(By.XPATH, "//img[contains(@src, '.png')]")

    # 6. Вывод результата в терминал
    for name in product_names:
        print("Название товара:", name.text)

    for price in product_prices:
        print("Цена товара:", price.text)

    for image in product_images:
        print("Ссылка на изображение:", image.get_attribute("src"))

finally:
    # Закрытие драйвера
    driver.quit()