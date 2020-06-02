from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from foodwatch.spiders.caminos_spider import CaminosSpider
from foodwatch.spiders.carlos3_spider import Carlos3Spider
# from foodwatch.spiders.quinta_spider import QuintaSpider
from foodwatch.spiders.quintaalt_spider import QuintaaltSpider
from foodwatch.spiders.tuenvio_spider import TuEnvioSpider
from foodwatch.spiders.xetid_spider import XetidSpider
settings = get_project_settings()
process = CrawlerProcess(settings)
# process = CrawlerProcess()

# process.crawl(Carlos3Spider)
# process.crawl(CaminosSpider)
# process.crawl(QuintaSpider)
# process.crawl(QuintaaltSpider)

process.crawl(TuEnvioSpider)
process.crawl(XetidSpider)


while True:
    print('foodwatch [CRAWLING ...]')
    process.start()     # the script will block here until all crawling jobs are finished
    print('foodwatch [DONE]')
