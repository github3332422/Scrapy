# -*- coding: utf-8 -*-
import json
import os
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import time
import re

class LagoucrawlSpider(CrawlSpider):
    name = 'lagouCrawl'
    allowed_domains = ['lagou.com']
    start_urls = ['https://www.lagou.com/zhaopin/shujuwajue/1/']

    rules = (
        Rule(LinkExtractor(allow=r'shujuwajue/\d+/'), follow=True),
        Rule(LinkExtractor(allow=r'jobs/\d+.html'), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=r'shujuwajue/\d+/'), follow=True),
    )

    # def start_requests(self):
    #     # 读取cookies.json文件
    #     with open(os.path.join(os.path.dirname(__file__, ), "cookies.json"), "r", encoding='utf-8') as f:
    #         self.cookies = json.loads(f.read())
    #
    #     self.myheaders = {
    #         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'zh-CN,zh;q=0.9',
    #         'Connection': 'keep-alive',
    #         'Host': 'www.lagou.com',
    #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    #     }
    #     yield scrapy.Request(url=self.start_urls[0], cookies=self.cookies, headers=self.myheaders, callback=self.parse_item,
    #                          dont_filter=True)

    def parse_item(self, response):
        # 工作名字
        name = response.xpath("//dd[@class='job_request']//span//text()").extract()

        # 工资,工作城市,经验,教育,工作性质
        # job_requests_spans = response.xpath("//dd[@class='job_request']//span//text()").extract()
        #
        # '''
        # 昨天在这里出现了问题，在获取job_requests_spans的值的时候出现了问题
        # '''
        #
        # salary = job_requests_spans[0].strip()
        # city = job_requests_spans[1].strip()
        # # city = re.sub(r"[\s/]", "", city)
        # work_year = job_requests_spans[2].strip()
        # # work_year = re.sub(r"[\s/]", "", work_year)
        # education = job_requests_spans[3].strip()
        # # education = re.sub(r"[\s/]", "", education)
        # work_nature = job_requests_spans[4].strip()

        # 职位诱惑
        job_detail = "".join(response.xpath("//dd[@class='job-advantage']//text()").extract()).strip()
        job_detail = job_detail.replace('\n', '')
        job_detail = job_detail.replace(' ', '')

        # 公司名字
        company = "".join(response.xpath("//h2[@class='fl']//text()").extract())
        company = company.replace('\n', '')
        company = company.replace(' ', '')[0:-6]

        # 发表时间
        release_time = response.xpath("//p[@class='publish_time']//text()").extract()

        # 职位要求
        zhiwei = str(response.xpath("//div[@class='job-detail']//text()").extract())
        zhiwei = zhiwei.replace('\\n', '')
        zhiwei = zhiwei.replace(' ', '')
        zhiwei = zhiwei.replace("'',", '')
        zhiwei = str(zhiwei)
        print("*"*50)
        print(name,job_detail,company,release_time,zhiwei)
        print("*"*50)
