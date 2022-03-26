from fastapi import FastAPI
from utils import getQuote

app = FastAPI()

@app.get("/")
def random():
    quote, saidBy, link = getQuote()
    data = {
        "quote": quote,
        "saidBy": saidBy,
        "link": link
    }
    return data

@app.get("/{url}")
def custom(url):
    quote, saidBy, link = getQuote(url)
    data = {
        "quote": quote,
        "saidBy": saidBy,
        "link": link
    }
    return data
