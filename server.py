from database.database import CacheManager
from services.parser_apteka_ru import scrape_apteka_ru
from fastapi import FastAPI
from services.parser_stolichki_ru import scrape_stolichki_ru
from services.parser_rigla_ru import  scrape_rigla_ru
app = FastAPI()
cache_manager = CacheManager()
FUNCTIONS = {
    "apteka_ru_data": scrape_apteka_ru,
    "stolichki_ru_data": scrape_stolichki_ru,
    "rigla_ru_data": scrape_rigla_ru
}

@app.get("/")
def root():
    return "Hello"
@app.post("/pars")
async def parse(pharm_name):
    """Обработка значения через три функции с кэшированием"""
    results = {}

    for func_name, func in FUNCTIONS.items():
        # Пытаемся получить результат из кэша
        cached_result = cache_manager.get_cached(func_name, pharm_name)
        if cached_result is not None:
            results[func_name] = cached_result

        else:
            # Если нет в кэше - выполняем функцию
            result = func(pharm_name)
            # Сохраняем результат в кэш
            cache_manager.save_to_cache(func_name, pharm_name, result)

            results[func_name] = result


    return results
