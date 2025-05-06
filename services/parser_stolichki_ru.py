from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_stolichki_ru(search_query):
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Используем webdriver-manager, он сам скачает нужный chromedriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(f"https://stolichki.ru/search?name={search_query}")
        time.sleep(5)
        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.ESCAPE)
        WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "product-card__link"))
        )

        # Прокрутка страницы для загрузки всех изображений
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Ожидание загрузки контента

        product_names = driver.find_elements(By.CLASS_NAME, "product-card__link")
        product_prices = driver.find_elements(By.CLASS_NAME, "product-card__price")
        product_images = driver.find_elements(By.CLASS_NAME, "product-card__pic")
        product_url = driver.find_elements(By.CLASS_NAME, "product-card__link")
        print(product_images[0].get_attribute("data-src"))

        products = []
        for name, price, image,url in zip(product_names, product_prices, product_images,product_url):
            product = {
                "name": name.get_attribute("title"),
                "price": price.text,
                "image_url": image.find_element(By.CLASS_NAME,"lozad").get_attribute("data-src"),
                "url": url.get_attribute("href")
            }
            products.append(product)

        return products

    finally:
        driver.quit()

#print(scrape_stolichki_ru("валидол"))