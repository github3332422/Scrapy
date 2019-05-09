# -*- coding: utf-8 -*-
import scrapy

from ipSpider.items import IpspiderItem


class ProxySpider(scrapy.Spider):
    name = 'proxy'
    allowed_domains = ['xicidaili.com']
    start_urls = ['http://xicidaili.com/']

    def start_requests(self):
        res = []
        for i in range(2, 5):
            url = 'http://www.xicidaili.com/nn/%d' % i
            req = scrapy.Request(url)
            res.append(req)
        return res

    def parse(self, response):
        table = response.xpath('//table[@id="ip_list"]')[0]
        trs = table.xpath('//tr')[1:]  # 去掉标题行
        items = []
        for tr in trs:
            pre_item = IpspiderItem()
            pre_item['ip'] = tr.xpath('td[2]/text()').extract()[0]
            pre_item['port'] = tr.xpath('td[3]/text()').extract()[0]
            pre_item['position'] = tr.xpath('string(td[4])').extract()[0].strip()
            pre_item['type'] = tr.xpath('td[6]/text()').extract()[0]
            pre_item['speed'] = tr.xpath('td[7]/div/@title').re('\d+\.\d*')[0]
            pre_item['last_check_time'] = tr.xpath('td[10]/text()').extract()[0]
            items.append(pre_item)
        return items
