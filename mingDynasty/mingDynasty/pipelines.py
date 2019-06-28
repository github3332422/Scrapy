# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import CsvItemExporter


class MingdynastyPipeline(object):
    def process_item(self, item, spider):
        return item

class txtPipeline(object):
    def open_spider(self, spider):
        self.file = open("明朝那些事.txt", 'w+')

    def process_item(self, item, spider):
        self.file.write(item['context'] + '\n')
        self.file.write('\n')

        return item

    def close_spider(self, spider):
        self.file.close()

class CsvPipeline(object):
    def __init__(self):
        self.file = open("Demo.csv", 'wb')
        self.exporter = CsvItemExporter(self.file, encoding="utf-8")
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item