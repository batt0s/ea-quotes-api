# ea-quotes-api

[Evrim Ağacı Sözler](https://evrimagaci.org/sozler) için resmi olmayan bir API.

Requests ve BeautifulSoup4 ile sözü alıp FastAPI ile size ulaştıran çok basit bir program.
[Render](https://render.com) üzerinde yayınlandı: https://ea-quotes-api.onrender.com
FastAPI tarafından oluşturulmuş dökümantasyona ulaşmak için : [Docs](https://ea-quotes-api.onrender.com/docs)

Rastgele bir söz almak için https://ea-quotes-api.onrender.com/ e GET request atmanız yeterli  
Belirli bir sözü almak için evrimagaci.org/alinti/{soz} gibi URL nin söz kısmını alıp sona eklemeniz lazım yani https://ea-quotes-api.onrender.com/{soz} e GET request atmanız yereli. (Örnek (httpie) : `http 'https://ea-quotes-api.onrender.com/insan-butun-kibriyle-ustun-bir-yaraticinin-mudahalesine-layik-olduguna-inanir-daha-alcakgonullu-ve8230-333'` )

Örnek response : 
```
{
    "quote":"Bir zamanlar çok bilge, az bilgiliydik. Şimdi devasa bilgiye sahibiz; ancak bunca bilgiyle baş edecek bilgeliğe sahip miyiz?",
    "author":"Jonas Salk",
    "link":"https://evrimagaci.org/alinti/bir-zamanlar-cok-bilge-az-bilgiliydik-simdi-devasa-bilgiye-sahibiz-ancak-bunca-bilgiyle-bas-edecek8230-342"
}
```
