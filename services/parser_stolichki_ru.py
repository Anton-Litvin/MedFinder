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
    chromedriver_path = os.path.join(os.getcwd(),"services", "chromedriver")

    service = Service(executable_path=chromedriver_path)

    driver = webdriver.Chrome(service=service)

    try:
        driver.get(f"https://stolichki.ru/search?name={search_query}")
        time.sleep(2)
        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.ESCAPE)
        time.sleep(10)

        product_names = driver.find_elements(By.CLASS_NAME, "product-card__link")
        product_prices = driver.find_elements(By.CLASS_NAME, "product-card__price")
        product_images = driver.find_elements(By.CLASS_NAME, "lozad")
        product_url = driver.find_elements(By.CLASS_NAME, "product-card__link")


        products = []
        for name, price, image,url in zip(product_names, product_prices, product_images,product_url):
            product = {
                "name": name.get_attribute("title"),
                "price": price.text,
                "image_url": image.get_attribute("data-src"),
                "url": url.get_attribute("href")
            }
            products.append(product)

        return products

    finally:
        driver.quit()
