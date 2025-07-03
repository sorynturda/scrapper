# main.py

from fastapi import FastAPI
from dtos import Linkk
from scrap.scraper import get_html

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/link/")
def post_link(
    link: Linkk
):
    html_text = get_html(link.url)
    return {"res": html_text}