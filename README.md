# ea-quotes-api

[Evrim Ağacı Sözler](evrimagaci.org/sozler) için resmi olmayan bir API.

Requests ve BeautifulSoup4 ile sözü alıp FastAPI ile size ulaştıran çok basit bir program.

[Deta](deta.sh) üzerinde yayınlandı: [ea-quotes.deta.dev](https://ea-quotes.deta.dev)  
FastAPI tarafından oluşturulmuş dökümantasyona ulaşmak için : [Docs](https://ea-quotes.deta.dev/docs)

Rastgele bir söz almak için https://ea-quotes.deta.dev e GET request atmanız yeterli  
Belirli bir sözü almak için evrimagaci.org/sozler/{soz} gibi URL nin söz kısmını alıp sona eklemeniz lazım yani https://ea-quotes.deta.dev/{soz} e GET request atmanız yereli. (Örnek (httpie) : `http 'https://ea-quotes.deta.dev/bernard-m-baruch-48'` )

Örnek response : 
```
{
    "link": "https://evrimagaci.org/sozler/bernard-m-baruch-48",
    "quote": "Herkes kendi fikrine sahip olmakta özgürdür; ancak kimse gerçekler konusunda hatalı olma hakkına sahip değildir. ",
    "saidBy": "Bernard M. Baruch"
}
```
