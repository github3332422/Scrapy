# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouspiderItem(scrapy.Item):
    positionName = scrapy.Field()
    positionUrl = scrapy.Field()
    positionPlace = scrapy.Field()
    positionSalary = scrapy.Field() 
    positionExper = scrapy.Field()
    positionEdu = scrapy.Field()
    companyName = scrapy.Field()
    companyNature = scrapy.Field()
    companyScale = scrapy.Field()
    positionClaim = scrapy.Field()
    positionAttract = scrapy.Field()

class positionItem(scrapy.Item):
    companyFullName = scrapy.Field()
    industryField = scrapy.Field()
    education = scrapy.Field()
    workYear = scrapy.Field()
    city = scrapy.Field()
