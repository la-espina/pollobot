import scrapy
from datetime import datetime
from ..helpers import Helpers
from foodwatch.keywords import wordpool,superfacil
from foodwatch.pollocubaBot import PolloBot

class SuperfacilSpider(scrapy.Spider):
    name = "superfacil"
    timeflag = False


    def start_requests(self):
        urls = []

      
        for tienda in superfacil.keys():
            for dep in superfacil[tienda]:
                url="https://www.superfacil.net/{}".format(tienda)
                urls.append(url)

        for url in urls:            
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        count = 0
        tienda=response.request.url.split("/")[3]
        
        bot=PolloBot()
        
        for product in response.css("figure.card-product "): 
            pname = product.css("figcaption.info-wrap h6::text").get()
            pprice = product.css("figcaption.info-wrap span.price-new::text").get()
            
            carrito = product.css("div.bottom-wrap button.btn i.fas").get()
            
            if pname is None or pprice is None or carrito is None: continue
            phash = Helpers.mkhash(pname, pprice)
         
            if Helpers.ispresent(phash) is False:
                count += 1
                msg="{}\n_{}_\n[{}]({})   ".format(pname,pprice,tienda,response.request.url)
                # bot.posttry(msg)
                # print(msg)
            yield {'place':tienda,'product': pname, 'price': pprice, 'chk': phash, 'url':response.request.url}
        # print('Count:',count)
        # if count > 0: Helpers.firetoast(0, count)
