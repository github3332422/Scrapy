# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re

from scrapy.exporters import JsonLinesItemExporter


class CsdnPipeline(object):
	def process_item(self, item, spider):
		item["tag"] = [re.sub(r"\s+|/","",i,re.S) for i in item["tag"]]
		item["tag"] =[i for i in item["tag"] if len(i)>0 and i!='标签：']
		print(item)

class CsdnspiderPipeline(object):
    def process_item(self, item, spider):
        return item

class jsonPipeline(object):
    def __init__(self):
        self.fp = open("jsonPipeline.json", "wb")
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False)

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.fp.close()
