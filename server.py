from parser_apteka_ru import scrape_apteka_ru
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return "Hello"
@app.post("/pars")
async def parse(pharm_name):
    return scrape_apteka_ru(pharm_name)