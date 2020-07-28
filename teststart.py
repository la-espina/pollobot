from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from foodwatch.spiders.superfacil_spyder import SuperfacilSpider

settings = get_project_settings()
process = CrawlerProcess(settings)


print('Initializing crawlers')
process.crawl(SuperfacilSpider)

process.start()