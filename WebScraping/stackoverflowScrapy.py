# scrapy runspider stackoverflowScrapy.py -O result.json -t json

from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup


class Question(Item):
    question = Field()
    description = Field()


class StackOverflowSpider(Spider):
    name = "MyFirstSpider"

    custom_settings = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0"
    }

    start_url = ["https://stackoverflow.com/questions"]

    def parser(self, response):
        sel = Selector(response)
        questions = sel.xpath('//div[@id="questions"]//div[@class="s-post-summary"]')
        for question in questions:
            item = ItemLoader(Question(), question)
            item.add_xpath("question", ".//h3/a/text()")
            item.add_xpath(
                "description", ".//div[@class='s-post-summary--content-excerpt']/text()"
            )

            yield item.load_item()
