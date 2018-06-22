# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouItem(scrapy.Item):
    position_name = scrapy.Field()
    wages = scrapy.Field()
    job_city = scrapy.Field()
    experience = scrapy.Field()
    education = scrapy.Field()
    property = scrapy.Field()
    classification = scrapy.Field()
    create_time = scrapy.Field()
    advantage = scrapy.Field()
    content = scrapy.Field()
    company_url = scrapy.Field()
    lagou_id = scrapy.Field()

    def sql_insert_get(self):
        insert_sql = """
            INSERT IGNORE INTO lagou(
                position_name, wages, job_city,experience, education, property,
                classification, create_time, advantage,content, company_url, lagou_id
            )   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        classification = ".".join(self["classification"])
        lagou_id = int(self["lagou_id"])
        sql_data = (
            self["position_name"], self["wages"], self["job_city"],
            self["experience"], self["education"], self["property"],
            classification, self["create_time"], self["advantage"],
            self["content"], self["company_url"], lagou_id,
        )

        return insert_sql, sql_data
