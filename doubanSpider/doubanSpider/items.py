# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanspiderItem(scrapy.Item):
    name = scrapy.Field()
    score = scrapy.Field()
    context = scrapy.Field()

class DoubanItem(scrapy.Item):
    # name = scrapy.Field()
    name = scrapy.Field()
    score = scrapy.Field()
    director = scrapy.Field()
    screenwriter = scrapy.Field()
    starring = scrapy.Field()
    type = scrapy.Field()
    sytime = scrapy.Field()
    movieslength = scrapy.Field()
    IMDB = scrapy.Field()
    context = scrapy.Field()
