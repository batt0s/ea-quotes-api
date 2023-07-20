# ea-quotes-api

[Evrim Ağacı Sözler](https://evrimagaci.org/sozler) için resmi olmayan bir API.

Requests ve BeautifulSoup4 ile sözü alıp FastAPI ile size ulaştıran çok basit bir program.

[Deta](https://deta.sh) üzerinde yayınlandı: https://eaquotesapi-1-y2922670.deta.app/
FastAPI tarafından oluşturulmuş dökümantasyona ulaşmak için : [Docs](https://eaquotesapi-1-y2922670.deta.app/docs)

Rastgele bir söz almak için https://eaquotesapi-1-y2922670.deta.app/ e GET request atmanız yeterli  
Belirli bir sözü almak için evrimagaci.org/alinti/{soz} gibi URL nin söz kısmını alıp sona eklemeniz lazım yani https://eaquotesapi-1-y2922670.deta.app/{soz} e GET request atmanız yereli. (Örnek (httpie) : `http 'https://https://eaquotesapi-1-y2922670.deta.app/insan-butun-kibriyle-ustun-bir-yaraticinin-mudahalesine-layik-olduguna-inanir-daha-alcakgonullu-ve8230-333'` )

Örnek response : 
```
{
    "quote":"Bir zamanlar çok bilge, az bilgiliydik. Şimdi devasa bilgiye sahibiz; ancak bunca bilgiyle baş edecek bilgeliğe sahip miyiz?",
    "author":"Jonas Salk",
    "link":"https://evrimagaci.org/alinti/bir-zamanlar-cok-bilge-az-bilgiliydik-simdi-devasa-bilgiye-sahibiz-ancak-bunca-bilgiyle-bas-edecek8230-342"
}
```
