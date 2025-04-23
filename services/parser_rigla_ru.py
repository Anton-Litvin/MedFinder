from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import os
import time
import json

def scrape_rigla_ru(search_query):
    """
    Парсит данные с сайта Rigla.ru по заданному запросу.

    :param search_query: Поисковый запрос (например, "аспирин")
    :return: Данные в формате JSON
    """
    # Указываем путь к chromedriver
    chromedriver_path = os.path.join(os.getcwd(),"services", "chromedriver")

    # Создаем объект Service
    service = Service(executable_path=chromedriver_path)

    # Инициализация драйвера с использованием Service
    driver = webdriver.Chrome(service=service)

    try:
        # 1. Переход на страницу
        driver.get(f"https://www.rigla.ru/search?q={search_query}")

        # 2. Ожидание появления окна выбора города и его закрытие
        time.sleep(5)
        ad_body = driver.find_element(By.CLASS_NAME, "popup-metadata-type-slider-close__btn")
        ad_body.click()

        # 3. Ожидание 10 секунд (дополнительное время для загрузки страницы)
        time.sleep(10)

        # 4. Извлечение текста из всех доступных блоков
        product_names = driver.find_elements(By.CLASS_NAME, "product__title")
        product_prices = driver.find_elements(By.CLASS_NAME, "product__active-price-number")
        product_images = driver.find_elements(By.CLASS_NAME, "product__img")
        product_url = driver.find_elements(By.CLASS_NAME, "product__title")

        # 5. Формирование данных в виде списка словарей
        products = []
        for name, price, image,url in zip(product_names, product_prices, product_images,product_url):
            product = {
                "name": name.get_attribute("title"),
                "price": price.text,
                "image_url": image.get_attribute("src"),
                "url": ("https://www.rigla.ru"+url.get_attribute("href"))
            }
            products.append(product)

        # 6. Преобразование в JSON
        return products
    finally:
        # Закрытие драйвера
        driver.quit()

