# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ipproxy.items import IpproxyItem


class ProxySpider(CrawlSpider):
    name = 'proxy'
    allowed_domains = ['xicidaili.com']
    start_urls = ['https://www.xicidaili.com/nn']

    rules = (
        # Rule(LinkExtractor(allow=r'Items/'), follow=True),
        Rule(LinkExtractor(allow='/nn/\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        items = []
        trs = response.xpath("//tr[@class='odd']")
        for tr in trs:
            item = IpproxyItem()
            tds = tr.xpath('.//td//text()').extract()
            for td in tds:
                if td.strip() == '':
                    tds.remove(td)
            if tds[4].strip() != '':
                # print(tds[0], tds[1], tds[4])
                ip = tds[0] + ':' + tds[1]
                type = tds[4]
            else:
                # print(tds[0],tds[1],tds[3])
                ip = tds[0] + ':' + tds[1]
                type = tds[3]
            item['ip'] = ip
            # item['type'] = type
            items.append(item)
        return items
