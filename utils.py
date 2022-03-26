import requests
from bs4 import BeautifulSoup
baseUrl = "https://evrimagaci.org/sozler/"
headers = {
    'User-Agent': 'ea-quote',
}
def getQuote(url = "rastgele"):
    req = requests.get(baseUrl+url, headers=headers)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find("a", class_="quote")
    quote = a.contents[0].strip('\n')
    link = a['href']
    saidByDiv = soup.find("div", class_="title")
    saidBy = saidByDiv.contents[0]
    return quote, saidBy, link
