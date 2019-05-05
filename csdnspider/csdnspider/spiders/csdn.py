# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CsdnSpider(CrawlSpider):
    name = 'csdn'
    allowed_domains = ['blog.csdn.net']
    start_urls = ['http://blog.csdn.net/hbblzjy']

    rules = (
        Rule(LinkExtractor(allow=r'blog.csdn.net/\w+$'), follow=True),
        Rule(LinkExtractor(allow=r'/\w+/article/details/\d+$'), callback="parse_item"),#跟的是具体文章
        # Rule(LinkExtractor(allow=r'channelid=\d+&page=\d+$'), follow=True),
        Rule(LinkExtractor(allow=r'/\w+/article/list/\d+$'), follow=True),#跟的是页数
    )
    all_item = []
    def parse_item(self, response):
        item = {}
        item["title"] = response.xpath("//h1/text()").extract_first()
        item['update_time'] = response.xpath("//span[@class='time']/text()").extract_first()
        item["tag"] = response.xpath("//ui[@class='htmledit_views']//text()").extract()
        yield item
