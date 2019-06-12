# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TencentspiderSpider(CrawlSpider):
    name = 'tencentSpider'
    allowed_domains = ['www.tencent.com']
    start_urls = ['https://careers.tencent.com/search.html/']

    rules = (
        Rule(LinkExtractor(allow=r'index=\d+'), callback='parse_item',follow=True),
        # Rule(LinkExtractor(allow=r'?postId==\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response.url)
        print("*"*50)
        # item = {}
        # #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # #item['name'] = response.xpath('//div[@id="name"]').get()
        # #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
