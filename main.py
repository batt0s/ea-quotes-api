from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from utils import getQuote

app = FastAPI()

@app.get("/")
def random():
    quote, author, link = getQuote()
    if quote == None:
        data = {
            "error": "An error occurred."
        }
        return JSONResponse(content=data, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    data = {
        "quote": quote,
        "author": author,
        "link": link
    }
    return JSONResponse(content=data, status_code=status.HTTP_200_OK)

@app.get("/{url}")
def custom(url):
    quote, author, link = getQuote(url)
    if quote == None:
        data = {
            "error": "An error occurred."
        }
        return JSONResponse(content=data, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    data = {
        "quote": quote,
        "author": author,
        "link": link
    }
    return JSONResponse(content=data, status_code=status.HTTP_200_OK)
