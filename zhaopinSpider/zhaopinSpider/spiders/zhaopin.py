# -*- coding: utf-8 -*-
import json
import re
import scrapy
from zhaopinSpider.items import ZhaopingItem


class ZhaopinSpider(scrapy.Spider):
    name = 'zhaopin'
    allowed_domains = ['zhaopin.com']
    start_urls = ['http://zhaopin.com/']
    baseUrl = 'https://fe-api.zhaopin.com/c/i/sou?start={0}&pageSize=90&cityId=489&kw={1}&kt=3'
    offset = 0  # 偏移量

    def start_requests(self):
        start_urls = ['https://fe-api.zhaopin.com/c/i/sou?start=0&pageSize=90&cityId=489&kw=深度学习&kt=3',
                      'https://fe-api.zhaopin.com/c/i/sou?start=0&pageSize=90&cityId=489&kw=算法工程师&kt=3',
                      'https://fe-api.zhaopin.com/c/i/sou?start=0&pageSize=90&cityId=489&kw=Hadoop&kt=3',
                      'https://fe-api.zhaopin.com/c/i/sou?start=0&pageSize=90&cityId=489&kw=数据开发&kt=3',
                      'https://fe-api.zhaopin.com/c/i/sou?start=0&pageSize=90&cityId=489&kw=数据分析师&kt=3',
                      'https://fe-api.zhaopin.com/c/i/sou?start=0&pageSize=90&cityId=489&kw=数据架构&kt=3',
                      'https://fe-api.zhaopin.com/c/i/sou?start=0&pageSize=90&cityId=489&kw=人工智能&kt=3',
                      'https://fe-api.zhaopin.com/c/i/sou?start=0&pageSize=90&cityId=489&kw=区块链&kt=3'
                      ]
        for url in start_urls:
            print("start_url:", url)
            yield scrapy.Request(url=url, callback=self.parse, meta={'start_url': url})

    def parse(self, response):
        data_list = json.loads(response.body)['data']['results']
        if len(data_list) == 0:
            return
        for data in data_list:
            item = ZhaopingItem()
            item['jobType'] = data['jobType']['display']  # 职位所属种类
            item['jobName'] = data['jobName']  # 职位名称
            item['emplType'] = data['emplType']  # 工作类型(兼职、全职)
            item['eduLevel'] = data['eduLevel']['name']  # 学历要求
            item['companyName'] = data['company']['name']  # 公司名称
            item['salary'] = data['salary']  # 薪资
            item['welfare'] = data['welfare']  # 员工福利
            item['city'] = data['city']['display']  # 工作城市
            item['workingExp'] = data['workingExp']['name']  # 工作经验
            item['infoComLink'] = data['company']['url']  # 公司详情连接
            item['positionUrl'] = data['positionURL']  # 职位详情链接

            yield item
        init_url = response.meta['start_url']
        self.offset += 90
        str_offset = str(self.offset)
        pattern = 'start=(.*?)&'
        replace_str = 'start=' + str_offset + '&'
        url = re.sub(pattern=pattern, repl=replace_str, string=init_url)

        yield scrapy.Request(url=url, callback=self.parse, meta={'start_url': url})
