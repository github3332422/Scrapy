# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MingspiderSpider(CrawlSpider):
    name = 'mingSpider'
    allowed_domains = ['mingchaonaxieshier.com']
    start_urls = ['http://www.mingchaonaxieshier.com/']

    rules = (
        Rule(LinkExtractor(allow=r'http://www.mingchaonaxieshier.com/.*?.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # url = response.url
        title = response.xpath("//div[@class='main']/h1//text()").extract()
        context = response.xpath("//div[@class='content']/p//text()").extract()[0:-6]
        item = {
            # 'url' : url,
            'title' : ''.join(title),
            'context' : ''.join(context)
        }
        print(title)
        return item


