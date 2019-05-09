# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IpspiderItem(scrapy.Item):
    ip = scrapy.Field()
    port = scrapy.Field()
    position = scrapy.Field()
    type = scrapy.Field()
    speed = scrapy.Field()
    last_check_time = scrapy.Field()
