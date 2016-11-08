# -*- coding: utf-8 -*-
# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Compose
from scrapy.contrib.loader.processor import MapCompose
from scrapy.contrib.loader.processor import TakeFirst
from scrapy.contrib.spiders import CrawlSpider
from scrapy.contrib.spiders import Rule
from scrapy.selector import HtmlXPathSelector
from items import AliItem

class AliSpider(CrawlSpider):

    name = "ali"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/"
    ]
#    rules = (
#             Rule(SgmlLinkExtractor(allow=('item')), callback='parse_item'),
#             )
    def parse(self, response):

        for sel in response.xpath('//div[@class="site-item "]'):
            item=AliItem()
            item['name'] = sel.xpath('div[@class="title-and-desc"]/div/text()').extract()

            yield item






        