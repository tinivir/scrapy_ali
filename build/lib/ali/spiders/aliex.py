# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from items import AliexItem


class AliexSpider(CrawlSpider):
    name = "aliex"
    allowed_domains = ["aliexpress.com"]
    start_urls = (
        'https://ru.aliexpress.com/af/category/202001195.html?d=n&isViewCP=y&CatId=202001195&catName=mobile-phones&spm=2114.21020108.1.38.indkuZ&origin=n',
    )

    rules = (

        Rule(LinkExtractor(allow=('/mobile-phones/', ))),     
        Rule(LinkExtractor(allow=('/item/', )),callback='parse_item',follow=False),
    )

    # def start_requests(self):
    #     yield scrapy.Request('https://ru.aliexpress.com/af/category/202001195.html?d=n&isViewCP=y&CatId=202001195&catName=mobile-phones&spm=2114.21020108.1.38.indkuZ&origin=n',
    #               meta = {
    #                   # 'dont_redirect': True,
    #                   # 'handle_httpstatus_list': [302]
    #               },
    #               callback= self.parse)

    def parse_item(self, response):
        item=AliexItem()
        item['name'] = response.xpath('//div/div/h1[@class="product-name"]/text()').extract()
        price = response.xpath('//div[@class="p-price-content"]/span[@class="p-price"]/text()').extract()
        if not price:
          price = response.xpath('//div[@class="p-price-content notranslate"]/span[@class="p-price"]/span[@itemprop="lowPrice"]/text()').extract()
        item['price'] = price
        yield item

