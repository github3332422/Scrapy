# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import redis


class IpproxyPipeline(object):
    def process_item(self, item, spider):
        return item

class MongoPipeline(object):

    collection_name = 'ip'

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

class RedisPipeline(object):

    # 打开数据库
    def open_spider(self, spider):
        db_host = spider.settings.get('REDIS_HOST')
        db_port = spider.settings.get('REDIS_PORT')
        db_index = spider.settings.get('REDIS_DB_INDEX')
        self.db_conn = redis.StrictRedis(host=db_host, port=db_port, db=db_index)
        # self.connection_client = redis.Redis(connection_pool=self.db_conn)

    # 关闭数据库
    def close_spider(self, spider):
        self.db_conn.connection_pool.disconnect()

    # 处理数据
    def process_item(self, item, spider):
        # self.insert_db(item)
        self.db_conn.rpush('ip',item['ip'])
        # return item

    # 插入数据
    # def insert_db(self, item):
    #     print('item:',item)
    #     for li in item:
    #         print('li:',li)
    #         self.db_conn.rpush('ip', li)
    #     self.db_conn.rpush('ip',item)
    #     for it in item:
    #         print(it)
    #         self.db_conn.rpush(it,'ip')
    #     print(item)