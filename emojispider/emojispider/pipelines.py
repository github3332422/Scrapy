# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonLinesItemExporter, CsvItemExporter
import os
import csv
import codecs
import json
from openpyxl import Workbook
import pymongo
import pymysql
from twisted.enterprise import adbapi

from emojispider import settings


class jsonPipeline1(object):
    def __init__(self):
        self.file = codecs.open("job1.json", "wb",encoding="utf-8")

    def process_item(self,item,spider):
        lines = json.dumps(dict(item), ensure_ascii=False);
        self.file.write(lines);
        # self.file.write(',\n');
        return item

    def close_spider(self,spider):
        self.file.close()


class jsonPipeline(object):
    def __init__(self):
        self.fp = open("jsonPipeline.json", "wb")
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False)

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.fp.close()


class xlsxPipeline(object):
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['emoji_handle', 'emoji_link', 'section'])

    def process_item(self, item, spider):
        line = [item['emoji_handle'], item['emoji_link'], item['section']]
        self.ws.append(line)
        self.wb.save('job.xlsx')
        return item

class csvPipeline1(object):
    def __init__(self):
        self.csvwriter = csv.writer(open('items.csv', 'wb'), delimiter=',')
        self.csvwriter.writerow(list['emoji_handle', 'emoji_link', 'section'])

    def process_item(self,item,spider):
        rows = zip(item['emoji_handle'], item['emoji_link'], item['section'])
        for row in rows:
            self.csvwriter.writerow(row)
        return item
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

class xmlPipeline(object):
    def __init__(self):
        self.file = codecs.open(filename="demo.xml",mode='w+',encoding='utf-8');

    def process_item(self,item,spider):
        res = dict(item)
        str = json.dumps(res,ensure_ascii=False);
        self.file.write(str);
        self.file.write(',\n');
        return item

    def close_spider(self,spider):
        self.file.close();

class txtPipeline(object):
    def open_spider(self, spider):
        self.file = open('Demo.txt', 'w')

    def process_item(self, item, spider):
        self.file.write(item['section'] + '\t')
        self.file.write(item['emoji_handle']+ '\t')
        self.file.write(item['emoji_link']+ '\t')
        self.file.write('\n')

        return item

    def close_spider(self, spider):
        self.file.close()


class MongoPipeline(object):

    collection_name = 'scrapy_emo'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(dict(item))
        return item


class MySqlPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='admin',
                                    db='db_scrapy', charset='utf8')
        self.cursor = self.conn.cursor()
        self.cursor.execute('truncate table emo')
        self.conn.commit()

    def process_item(self, item, spider):
        try:
            self.cursor.execute("insert into emo (section,emoji_handle,emoji_link) VALUES (%s,%s,%s)", (item['section'], item['emoji_handle'], item['emoji_link']))
            self.conn.commit()
        except pymysql.Error:
            print("插入失败")
        return item

    def close_spider(self, spider):
        self.conn.close()

class DemoPipeline(object):
    @classmethod
    def from_settings(cls,settings):
        adbparams = dict(
            host = settings['MYSQL_HOST'],
            user = settings['MYSQL_USER'],
            password = settings['MYSQL_PASSWORD'],
            db = settings['MYSQL_DB'],
            cursorclass = pymysql.cursors.DictCursor,
        )
        dbpool = adbapi.ConnectionPool('pymysql',**adbparams)
        return cls(dbpool)

    def __init__(self,dbpool):
        self.dbpool = dbpool

    def process_item(self,item,spider):
        query = self.dbpool.runInteraction(self.do_insert,item)
        query.addErrback(self.handle_error)
        return item

    def handle_error(self,failure):
        print('failure')

    def do_insert(self,cursor,item):
        sql = "insert into emo(section,emoji_handle,emoji_link) values(%s,%s,%s);"
        cursor.execute(sql,(item['section'],item['emoji_handle'],item['emoji_link']))