from parser_apteka_ru import scrape_apteka_ru
from fastapi import FastAPI
from parser_stolichki_ru import scrape_stolichki_ru

app = FastAPI()

@app.get("/")
def root():
    return "Hello"
@app.post("/pars")
async def parse(pharm_name):
    apteka1 = scrape_apteka_ru(pharm_name)
    apteka2 = scrape_stolichki_ru(pharm_name)
    return {"apteka_ru_data":apteka1,
            "stolichki_ru_data" : apteka2}