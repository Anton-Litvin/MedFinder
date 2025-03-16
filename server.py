from parser_apteka_ru import scrape_apteka_ru
from parser_stolichki_ru import scrape_stolichki_ru
from fastapi import FastAPI

app = FastAPI()

@app.post("/pars")
def parse(pharm_name):
    return [scrape_apteka_ru(pharm_name)]