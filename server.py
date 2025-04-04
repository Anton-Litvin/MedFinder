from parser_apteka_ru import scrape_apteka_ru
from fastapi import FastAPI
from parser_stolichki_ru import scrape_stolichki_ru
from parser_rigla_ru import  scrape_rigla_ru
app = FastAPI()

@app.get("/")
def root():
    return "Hello"
@app.post("/pars")
async def parse(pharm_name):
    apteka1 = scrape_apteka_ru(pharm_name)
    apteka2 = scrape_stolichki_ru(pharm_name)
    apteka3 = scrape_rigla_ru(pharm_name)
    return {"apteka_ru_data":apteka1,
            "stolichki_ru_data" : apteka2,
            "rigla_ru_data": apteka3}