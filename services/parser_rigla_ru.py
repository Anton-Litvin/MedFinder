from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_rigla_ru(search_query):
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Используем webdriver-manager, он сам скачает нужный chromedriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(f"https://www.rigla.ru/search?q={search_query}")
        time.sleep(5)

        try:
            ad_body = driver.find_element(By.CLASS_NAME, "popup-metadata-type-slider-close__btn")
            ad_body.click()
        except:
            pass

        time.sleep(10)

        product_names = driver.find_elements(By.CLASS_NAME, "product__title")
        product_prices = driver.find_elements(By.CLASS_NAME, "product__active-price-number")
        product_images = driver.find_elements(By.CLASS_NAME, "product__img")

        products = []
        for name, price, image in zip(product_names, product_prices, product_images):
            product = {
                "name": name.get_attribute("title"),
                "price": price.text,
                "image_url": image.get_attribute("src"),
                "url": "https://www.rigla.ru" + name.get_attribute("href"),
            }
            products.append(product)

        return products
    finally:
        driver.quit()

#print(scrape_rigla_ru("валидол"))