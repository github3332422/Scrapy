# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MingdynastyItem(scrapy.Item):
    '''
    设置要获取的题目和内容
    '''
    title = scrapy.Field()
    # url = scrapy.Field()
    context = scrapy.Field()
