# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
from scrapy_redis.spiders import RedisSpider
import re
from ScrapyRedis.items import LagouItem


class LagouSpider(RedisSpider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    redis_key = 'lagou:start_urls'

    # rules = (
    #     Rule(LinkExtractor(allow=r'.*jobs/\d+.html'), callback='parse_data'),
    #     Rule(LinkExtractor(allow=r'.*zhaopin/\w+/($|/\d+)'), callback='parse_item'),
    # )

    def parse(self, response):
        all_urls = response.css("a::attr(href)").extract()
        all_urls = [parse.urljoin(response.url, x) for x in all_urls if x.startswith("https")]
        for url in all_urls:
            a = re.match(r'.*jobs/\d+.html', url)
            b = re.match(r'.*zhaopin/\w+/($|/\d+)', url)
            if a:
                yield scrapy.Request(url, callback=self.parse_data)
            if b:
                yield scrapy.Request(url, callback=self.parse)

    def parse_data(self, response):
        lagou_item = LagouItem()
        re_match = re.match('^https://www.lagou.com/jobs/(\d+).html$', response.url)
        lagou_id = re_match.group(1) if re_match else 0
        lagou_item["position_name"] = response.css(".job-name span::text").extract_first("")
        lagou_item["wages"] = response.css(".job_request .salary::text").extract_first("")
        lagou_item["job_city"] = response.xpath('//*[@class="job_request"]/p/span[2]/text()').extract_first("").replace(
            "/", "").strip()
        lagou_item["experience"] = response.xpath('//*[@class="job_request"]/p/span[3]/text()').extract_first(
            "").replace("/", "").strip()
        lagou_item["education"] = response.xpath('//*[@class="job_request"]/p/span[4]/text()').extract_first(
            "").replace("/", "").strip()
        lagou_item["property"] = response.xpath('//*[@class="job_request"]/p/span[5]/text()').extract_first("")
        lagou_item["classification"] = response.css(".position-label li::text").extract()
        lagou_item["create_time"] = response.css(".publish_time::text").extract_first("")
        lagou_item["advantage"] = response.css(".job-advantage p::text").extract_first("")
        lagou_item["content"] = response.css(".job_bt div").extract_first("")
        lagou_item["company_url"] = response.css(".c_feature a::attr(href)").extract_first("")
        lagou_item["lagou_id"] = lagou_id

        yield lagou_item
