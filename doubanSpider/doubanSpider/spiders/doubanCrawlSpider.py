# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from doubanSpider.items import DoubanItem


class DoubancrawlspiderSpider(CrawlSpider):
    name = 'doubanCrawlSpider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250?start=0&filter=']

    rules = (
        Rule(LinkExtractor(allow="start=\d+&filter="), follow=True),
        Rule(LinkExtractor(allow="/subject/\d+/"), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        # print(response.url)
        # html = etree.HTML(response.text)
        item = DoubanItem()
        spans = response.xpath("//div[@id='info']/span")
        name = response.xpath("//div[@id='content']/h1//text()").extract()[1]
        score = response.xpath("//div[@class='rating_self clearfix']/strong//text()").extract()[0]
        director = spans[0].xpath("./span[@class='attrs']//text()").extract()
        screenwriter = spans[1].xpath("./span[@class='attrs']/a//text()").extract()
        starring = spans[2].xpath("./span[@class='attrs']/a//text()").extract()
        type = response.xpath("//span[@property='v:genre']//text()").extract()[1:]
        sytime = response.xpath("//span[@property='v:initialReleaseDate']//text()").extract()
        movieslength = response.xpath("//span[@property='v:runtime']//text()").extract()[0]
        IMDB = response.xpath("//div[@id='info']//a[@target='_blank']//@href").extract()[0]
        context = response.xpath("//span[@property='v:summary']//text()").extract()[0].strip()
        # print(name,score,director,screenwriter,starring,type,sytime,movieslength,IMDB)
        item = {
            'name' : name,
            'score' : score,
            'director' : director,
            'screenwriter' : screenwriter,
            'starring': starring,
            'type' : type,
            'sytime' : sytime,
            'movieslength' : movieslength,
            'IMDB' : IMDB,
            'context':context
        }
        return item
