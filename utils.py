import requests
from bs4 import BeautifulSoup
baseUrl = "https://evrimagaci.org/sozler/"
headers = {
    'User-Agent': 'ea-quote',
}
def getQuote(url: str = "rastgele"):
    try:
        req = requests.get(baseUrl+url, headers=headers)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        blockquote = soup.find("blockquote", class_="quote")
        quote = blockquote.contents[0].strip('\n')
        link = req.url
        authorDiv = soup.find("div", class_="quote-author")
        author = authorDiv.contents[0]
        return quote, author, link
    except:
        return None, None, None
