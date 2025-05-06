import asyncio
from concurrent.futures import ThreadPoolExecutor
from fastapi import FastAPI

from database.database import CacheManager
from services.parser_apteka_ru import scrape_apteka_ru
from services.parser_stolichki_ru import scrape_stolichki_ru
from services.parser_rigla_ru import scrape_rigla_ru

app = FastAPI()
cache_manager = CacheManager(ttl_seconds=3600)
executor = ThreadPoolExecutor()

FUNCTIONS = {
    "apteka_ru_data": scrape_apteka_ru,
    "stolichki_ru_data": scrape_stolichki_ru,
    "rigla_ru_data": scrape_rigla_ru
}

async def run_parser_with_cache(func_name: str, func, pharm_name: str):
    """Выполняет функцию с кэшированием и запуском в потоке"""
    loop = asyncio.get_event_loop()

    # Проверка кэша
    cached_result = cache_manager.get_cached(func_name, pharm_name)
    if cached_result is not None:
        return func_name, cached_result

    # Выполнение синхронной функции в потоке
    result = await loop.run_in_executor(executor, func, pharm_name)

    # Сохраняем результат в кэш
    cache_manager.save_to_cache(func_name, pharm_name, result)

    return func_name, result

@app.post("/pars")
async def parse(pharm_name: str):
    """Обработка значения через три функции с многопоточностью и кэшированием"""
    tasks = [
        run_parser_with_cache(func_name, func, pharm_name)
        for func_name, func in FUNCTIONS.items()
    ]

    results = {}
    for func_name, result in await asyncio.gather(*tasks):
        results[func_name] = result
    print(result)
    return results
