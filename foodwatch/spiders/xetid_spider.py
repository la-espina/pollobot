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
                self.tienda=tienda
                yield scrapy.Request(url=url, callback=self.parse)
                

    def parse(self, response):
        count = 0

        for product in response.css("ul#listado-prod div.product-container"):
            pname = product.css("div.product-image-container a.product_img_link").xpath('@title').get()
            pprice = product.css("div.right-block div.content_price span.price::text").get()

            if pname is None or pprice is None: continue

            phash = Helpers.mkhash(pname, pprice)


            if Helpers.ispresent(phash) is False:
                count += 1
                yield {'place':self.tienda,'product': pname, 'price': pprice, 'chk': phash}

        # if count > 0: Helpers.firetoast(2, count)
