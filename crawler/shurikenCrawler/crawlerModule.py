#!/usr/bin/python
# -*- coding: utf-8 -*-

# crawler init

import sys
import csv
import scrapy
import os
import time
from scrapy.exceptions import CloseSpider
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy import signals
from shurikenCrawler.items import UrlKnef
from shurikenCrawler.middlewares import ProxyMiddleware
from datetime import datetime

class Knef(CrawlSpider):
    name = 'knef'
    allowed_domains = []
    DEPTH_LIMIT = 3

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(Knef, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    def spider_closed(self, spider):
        spider.logger.info('Spider closed: %s', spider.name)

    def __init__(self, startUrl=None, scanTime=None, *args, **kwargs):
        super(Knef, self).__init__(*args, **kwargs)
        print "[$ crawler $] Start URL : " + startUrl
        self.start_urls = [startUrl]
        self.scan_time = scanTime
        self.i=0
        self.init_time = time.time()

    rules = (Rule(LinkExtractor(allow=(), deny_domains=(
        'google.es',
        'movistar.es',
        'linkedin.com',
        'apple.com',
        'instagram.com',
        'tuenti.com',
        'facebook.com',
        'youtube.com',
        'twitter.com',
        'microsoft.com',
        'wikipedia.org',
        'smugmug.com',
        'google.com',
        'mozilla.org')), callback='parse_item', follow=True),)

    def parse_item(self, response):
        self.current_time = time.time() - self.init_time
        self.logger.info('[$ crawler $] Current time ------------------ > %s secods', self.current_time )
        if str(self.current_time) > str(self.scan_time):
                self.finish_timeCrawler()
        else:
            for link in LinkExtractor(allow=(),deny = self.allowed_domains, deny_domains=(
                'google.es',
                'movistar.es',
                'linkedin.com',
                'apple.com',
                'instagram.com',
                'tuenti.com',
                'facebook.com',
                'youtube.com', 'twitter.com',
                'microsoft.com','wikipedia.org',
                'smugmug.com',
                'google.com',
                'mozilla.org')).extract_links(response):
                self.item = UrlKnef()
                self.item['Id'] =  self.i
                self.i = self.i + 1
                self.item['url'] =  link.url
                self.item['time'] = str(datetime.now())
                self.item['urlComes'] = response.url
                self.logger.info('[$ crawler $] Link url search: %s', link.url)
                global urls_Extractor
                urls_Extractor.append(self.item)
                return self.item

    def finish_timeCrawler(self):
        raise CloseSpider('End Knef crawler')


def start_Crawler():
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    print "[$ crawler $] To stop crawler press Ctrl-C"
    starturl = raw_input('[$ crawler $] Insert url which the crawler start > ')
    scanTime = raw_input('[$ crawler $] Insert the duration of the link extractor > ')
    global urls_Extractor
    urls_Extractor = []

    process.crawl(Knef, startUrl = starturl, scanTime = scanTime)
    process.start()
    first = True
    data_crawler = os.getcwd() + "/data/crawler_data/crawler_links.csv"
    if os.path.exists(data_crawler):
        os.remove(data_crawler)
    with open(data_crawler, 'a') as f:
        for url in urls_Extractor:
            if first:
                w = csv.DictWriter(f, fieldnames = ['Id','url', 'urlComes', 'time'])
                w.writeheader()
                w.writerow(url)
                first = False
            else:
                if url is not None:
                    if '' in url['url'] and len(url['url']) == 0:
                        print "[$ crawler $] Problem with some url"
                    else:
                        print url
                        w.writerow(url)
