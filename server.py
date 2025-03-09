import requests
from bs4 import BeautifulSoup
import json


def search_apteka_ru(drug_name):
    # URL для поиска на сайте apteka.ru
    url = f"https://apteka.ru/search/?q={drug_name}"

    # Заголовки для имитации запроса от браузера
    st_accept = "text/html"  # говорим веб-серверу,
    # что хотим получить html
    # имитируем подключение через браузер Mozilla на macOS
    st_useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"
    # формируем хеш заголовков
    headers = {
        "Accept": st_accept,
        "User-Agent": st_useragent
    }

    # Отправка GET-запроса
    response = requests.get(url, headers=headers)

    # Проверка статуса ответа
    if response.status_code != 200:
        return json.dumps({"error": "Не удалось получить данные с сайта"})

    # Парсинг HTML-страницы
    soup = BeautifulSoup(response.text, 'html.parser')

    # Поиск элементов с информацией о препарате
    # (этот код зависит от структуры сайта и может потребовать корректировки)
    items = soup.find_all('div', class_='product-item')
    results = []

    for item in items:
        name = item.find('div', class_='product-title').text.strip()
        price = item.find('div', class_='product-price').text.strip()
        active_substance = item.find('div', class_='product-substance').text.strip() if item.find('div',
                                                                                                  class_='product-substance') else "Не указано"
        image_url = item.find('img')['src'] if item.find('img') else "Нет изображения"

        results.append({
            "Имя": name,
            "Цена": price,
            "Действующее вещество": active_substance,
            "Ссылка на фото": image_url
        })

    # Возврат результатов в формате JSON
    return json.dumps(results, ensure_ascii=False, indent=4)


# Пример использования
drug_name = ("аспирин")
result = search_apteka_ru(drug_name)
print(result)