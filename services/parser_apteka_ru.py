from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys


def scrape_apteka_ru(search_query):
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Используем webdriver-manager, он сам скачает нужный chromedriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(f"https://apteka.ru/search/?q={search_query}")

        time.sleep(5)
        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.ESCAPE)

        time.sleep(10)

        product_names = driver.find_elements(By.CLASS_NAME, "catalog-card__name")
        product_prices = driver.find_elements(By.CLASS_NAME, "moneyprice__roubles")
        product_images = driver.find_elements(By.CSS_SELECTOR, ".CardPhotos img")
        product_url = driver.find_elements(By.CLASS_NAME, "catalog-card__link")

        # 5. Формирование данных в виде списка словарей
        products = []
        for name, price, image,url in zip(product_names, product_prices, product_images,product_url):
            product = {
                "name": name.text,
                "price": price.text,
                "image_url": image.get_attribute("src"),
                "url": url.get_attribute("href")
            }
            products.append(product)

        # 6. Преобразование в JSON
        return products
    finally:
        # Закрытие драйвера
        driver.quit()
