import scrapy
from datetime import datetime
from ..helpers import Helpers
from foodwatch.keywords import wordpool,departments
from foodwatch.pollocubaBot import PolloBot

class TuEnvioSpider(scrapy.Spider):
    name = "tuenvio"
    timeflag = False


    def start_requests(self):
        urls = []

        # for keyword in wordpool:
        #     urls.append("https://www.tuenvio.cu/4caminos/Search.aspx?keywords=%22" + keyword + "%22")
        for tienda in departments.keys():
            for dep in departments[tienda]:
                url="https://www.tuenvio.cu/{}/Products?depPid={}".format(tienda,dep)
                urls.append(url)

        for url in urls:            
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        count = 0
        tienda=response.request.url.split("/")[3]
        
        bot=PolloBot()
        
        for product in response.css("div.thumbSetting"):
            pname = product.css("div.thumbTitle>a::text").get()
            pprice = product.xpath("div[2]/span/text()").get()

            if pname is None or pprice is None: continue
            phash = Helpers.mkhash(pname, pprice)
         
            if Helpers.ispresent(phash) is False:
                count += 1
                msg="{}\n_{}_\n[{}]({})   ".format(pname,pprice,tienda,response.request.url)
                bot.posttry(msg)
            yield {'place':tienda,'product': pname, 'price': pprice, 'chk': phash, 'url':response.request.url}
        # print('Count:',count)
        # if count > 0: Helpers.firetoast(0, count)
