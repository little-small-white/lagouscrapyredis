# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class ScrapyredisSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ScrapyredisDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        request.cookies = {
            'JSESSIONID': 'ABAAABAAAGFABEF0848DC39785E5B13FF944B1215003C83',
            '_ga': 'GA1.2.1717565632.1529596658',
            '_gid': 'GA1.2.1106614961.1529596658',
            'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1529596658',
            'user_trace_token': '20180621235741-d3e31e97-756b-11e8-abdf-525400f775ce',
            'LGSID': '20180621235741-d3e3207e-756b-11e8-abdf-525400f775ce',
            'PRE_UTM': '',
            'PRE_HOST': '',
            'PRE_SITE': '',
            'PRE_LAND': 'https%3A%2F%2Fwww.lagou.com%2F',
            'LGUID': '20180621235741-d3e32211-756b-11e8-abdf-525400f775ce',
            'index_location_city': '%E5%85%A8%E5%9B%BD',
            'TG-TRACK-CODE': 'index_hotjob',
            'X_HTTP_TOKEN': '14a08ffd76d06247c3a92ae9e961c7fe',
            'LG_LOGIN_USER_ID': '3a432dc25843f9071037e1c5b39dc7c4d6f528e249f595104e37748674502780',
            '_putrc': 'B2551B7CF7C9B2F1123F89F2B170EADC',
            'login': 'true',
            'unick': '%E9%9F%A6%E4%B8%96%E5%8B%87',
            'showExpriedIndex': '1',
            'showExpriedCompanyHome': '1',
            'showExpriedMyPublish': '1',
            'hasDeliver': '1',
            'gate_login_token': '290dde76fa4e305afa8bd39d689607b745e287c6b6401739e9db721eb3e9a8e4',
            '_gat': '1',
            'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1529596803',
            'LGRID': '20180622000006-2a554df5-756c-11e8-abdf-525400f775ce',
        }
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
