from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import os
import time
import json

def scrape_stolichki_ru(search_query):
    """
    Парсит данные с сайта Stolichki.ru по заданному запросу.

    :param search_query: Поисковый запрос (например, "аспирин")
    :return: Данные в формате JSON
    """
    # Указываем путь к chromedriver
    chromedriver_path = os.path.join(os.getcwd(), "chromedriver")

    # Создаем объект Service
    service = Service(executable_path=chromedriver_path)

    # Инициализация драйвера с использованием Service
    driver = webdriver.Chrome(service=service)

    try:
        # 1. Переход на страницу
        driver.get(f"https://stolichki.ru/search?name={search_query}")
        time.sleep(2)
        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.ESCAPE)
        # 3. Ожидание 10 секунд (дополнительное время для загрузки страницы)
        time.sleep(10)

        # 4. Извлечение текста из всех доступных блоков
        product_names = driver.find_elements(By.CLASS_NAME, "product-card__link")
        product_prices = driver.find_elements(By.CLASS_NAME, "product-card__price")
        product_images = driver.find_elements(By.CLASS_NAME, "lozad")

        # 5. Формирование данных в виде списка словарей
        products = []
        for name, price, image in zip(product_names, product_prices, product_images):
            product = {
                "name": name.get_attribute("title"),
                "price": price.text,
                "image_url": image.get_attribute("data-src")
            }
            products.append(product)

        # 6. Преобразование в JSON
        return json.dumps(products, ensure_ascii=False, indent=4)

    finally:
        # Закрытие драйвера
        driver.quit()


# Пример использования
search_query = "аспирин"
result = scrape_stolichki_ru(search_query)
print(result)
