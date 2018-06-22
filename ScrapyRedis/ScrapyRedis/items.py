# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouItem(scrapy.Item):
    position_name = scrapy.Field()
    pay_min = scrapy.Field()
    pay_max = scrapy.Field()
    job_city = scrapy.Field()
    experience = scrapy.Field()
    education = scrapy.Field()
    properties = scrapy.Field()
    classification = scrapy.Field()
    create_time = scrapy.Field()
    advantage = scrapy.Field()
    content = scrapy.Field()
    company_add = scrapy.Field()
    company_url = scrapy.Field()
    lagou_id = scrapy.Field()

    def sql_insert_get(self):
        insert_sql = """
            INSERT IGNORE INTO lagou(
                position_name, pay_min, pay_max, job_city,experience, education, properties,
                classification, create_time, advantage,content, company_add, company_url, lagou_id
            )   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        classification = ".".join(self["classification"])
        lagou_id = int(self["lagou_id"])
        sql_data = (
            self["position_name"], self["pay_min"], self["pay_max"], self["job_city"],
            self["experience"], self["education"], self["properties"],
            classification, self["create_time"], self["advantage"],
            self["content"], self["company_add"], self["company_url"], lagou_id,
        )

        return insert_sql, sql_data
