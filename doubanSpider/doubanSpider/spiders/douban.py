# -*- coding: utf-8 -*-
import scrapy

from doubanSpider.items import DoubanspiderItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250/']

    headler = {
        'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=self.headler)

    def parse(self, response):
        lis = response.xpath('//ol[@class="grid_view"]/li')
        items = []
        for li in lis:
            item = DoubanspiderItem()
            lis = li.xpath('.//span[@class="title"]//text()')
            if len(lis) > 0 :
                name = lis.extract()[0]
            else:
                name = ""
            item['name'] = name
            lis = li.xpath('.//span[@class="rating_num"]//text()')
            if len(lis) > 0 :
                score = lis.extract()[0]
            else:
                score = ""
            item['score'] = score
            lis = li.xpath('.//span[@class="inq"]//text()')
            if len(lis) > 0:
                context = lis.extract()[0]
            else:
                context = ""
            item['context'] = context
            yield item
        next_url = response.xpath('//span[@class="next"]/a/@href').extract()

        # 判断是否还有下一页数据，如果有就继续爬，直到爬取完最后一页
        if next_url:
            next_url = "https://movie.douban.com/top250" + next_url[0]
            print(next_url)
            yield scrapy.Request(next_url, headers=self.headler,callback=self.parse)
