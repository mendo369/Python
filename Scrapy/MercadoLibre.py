from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.loader import ItemLoader


class Article(Item):
    title = Field()
    description = Field()


class MercadoLibreCrawler(CrawlSpider):
    name = "mercadolibre"

    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "CLOSESPIDER_PAGECOUNT": 10 #Número de páginas
    }

    allowed_domains = ['listado.mercadolibre.com.co', 'articulo.mercadolibre.com.co']

    start_urls = ["https://listado.mercadolibre.com.co/celulares-smartphone"]

    download_delay = 1

    rules = (
        Rule(
            LinkExtractor(
                allow=r'/_Desde_\d+'
            ), follow=True
        ),
        Rule(
            LinkExtractor(
                allow=r'/'
            ), follow=True, callback='parse_items'
        )
    )

    @staticmethod
    def parse_items(response):
        item = ItemLoader(Article(), response)

        item.add_xpath('title', '//h1/text()')
        item.add_xpath('description', '//p[@class="ui-pdp-description__content"]/text()')

        yield item.load_item()
