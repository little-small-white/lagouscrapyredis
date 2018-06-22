# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class ScrapyredisPipeline(object):
    def process_item(self, item, spider):
        self.sql_execute(item)
        return item

    def open_spider(self, spider):
        self.conn = pymysql.connect(host="localhost", user="root", password="root", database="wei", charset="utf8")
        self.cursor = self.conn.cursor()

    def sql_execute(self, item):
        sql, values = item.sql_insert_get()
        self.cursor.execute(sql, values)
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.conn.close()
