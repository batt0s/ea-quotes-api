from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from utils import getQuote

app = FastAPI()

@app.get("/")
def random():
    quote, saidBy, link = getQuote()
    if quote == '':
        data = {
            "error": "An error occurred."
        }
        return JSONResponse(content=data, status_code=status.HTTP_400_BAD_REQUEST)
    data = {
        "quote": quote,
        "saidBy": saidBy,
        "link": link
    }
    return JSONResponse(content=data, status_code=status.HTTP_200_OK)

@app.get("/{url}")
def custom(url):
    quote, saidBy, link = getQuote(url)
    if quote == '':
        data = {
            "error": "An error occurred."
        }
        return JSONResponse(content=data, status_code=status.HTTP_400_BAD_REQUEST)
    data = {
        "quote": quote,
        "saidBy": saidBy,
        "link": link
    }
    return JSONResponse(content=data, status_code=status.HTTP_200_OK)
