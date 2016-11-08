# -*- coding: utf-8 -*-
import scrapy
from items import IpiItem
import random
from scrapy.exceptions import NotConfigured, NotSupported


class IpiSpider(scrapy.Spider):
    name = "ipi"
    allowed_domains = ["ipify.org"]
    start_urls = (
        'https://api.ipify.org', #for i in range(2)
    )
    g_i = 0

    def parse(self, response):

        pub_ip = response.xpath('//body')
        item=IpiItem()
        item['name'] = response.xpath('//body/p/text()').extract()

        yield item
        
        IpiSpider.g_i += 1
        if IpiSpider.g_i > 5:
            return

        yield scrapy.Request('https://api.ipify.org/?fake={}'.format(IpiSpider.g_i))









