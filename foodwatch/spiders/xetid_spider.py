import scrapy
from datetime import datetime
from ..helpers import Helpers
from foodwatch.keywords import wordpool,xetidep


class XetidSpider(scrapy.Spider):
    name = "xetid"
    timeflag = False

    def start_requests(self):
        urls = []

        # for keyword in wordpool:
        #     urls.append("https://5tay42.xetid.cu/module/categorysearch/catesearch?search_query="+keyword)
        for tienda in xetidep.keys():
            for dep in xetidep[tienda]:
                url="https://{}.xetid.cu/{}".format(tienda,dep)
                # self.tienda=tienda
                self.url=url
                yield scrapy.Request(url=url, callback=self.parse)
                

    def parse(self, response):
        count = 0
        tienda=response.request.url.split("/")[2].split(".")[0]
        bot=PolloBot()
        for product in response.css("ul#listado-prod div.product-container"):
            pname = product.css("div.product-image-container a.product_img_link").xpath('@title').get()
            pprice = product.css("div.right-block div.content_price span.price::text").get()

            if pname is None or pprice is None: continue

            phash = Helpers.mkhash(pname, pprice)


            if Helpers.ispresent(phash) is False:
                count += 1
                msg="{}\n_{}_\n[{}]({})   ".format(pname,pprice,tienda,response.request.url)
                bot.posttry(msg)
                yield {'place':tienda,'product': pname, 'price': pprice, 'chk': phash,'url':response.request.url }

        # if count > 0: Helpers.firetoast(2, count)
