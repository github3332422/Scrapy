# -*- coding: utf-8 -*-
import scrapy

from zhilian.items import ZhilianItem


class ZhilianspiderSpider(scrapy.Spider):
    name = 'zhilianSpider'
    allowed_domains = ['zhaopin.com']
    start_urls = ['https://jobs.zhaopin.com/CC392160220J00057436115.htm']

    def parse(self, response):
        positionName = response.xpath("//h3[@class='summary-plane__title']//text()").extract()[0]
        salary = response.xpath("//span[@class='summary-plane__salary']//text()").extract()[0]
        city = response.xpath("//ul[@class='summary-plane__info']//li/a//text()").extract()[0]
        lis = response.xpath("//ul[@class='summary-plane__info']//li/text()").extract()
        expersise = lis[0]
        education = lis[1]
        fuli = response.xpath("//div[@class='highlights__content']/span//text()").extract()
        jineng = response.xpath("//div[@class='describtion__skills-content']/span//text()").extract()
        contexts = response.xpath("//div[@class='describtion__detail-content']/p//text()").extract()
        print(positionName,salary,city,expersise,education,fuli,jineng,contexts)