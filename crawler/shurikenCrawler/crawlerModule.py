#!/usr/bin/python
# -*- coding: utf-8 -*-

# crawler init

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from shurikenCrawler.items import UrlKnef
from datetime import datetime


class Knef(CrawlSpider):
    name = 'knef'
    allowed_domains = []

    def __init__(self, startUrl=None, *args, **kwargs):
        super(Knef, self).__init__(*args, **kwargs)
        print "[$ crawler $] start URL : " + startUrl
        self.start_urls = [startUrl]
        
    rules = (Rule(LinkExtractor(allow=()), callback='parse_item', follow=True),)

    def parse_item(self, response):

        for link in LinkExtractor(allow=(),deny = self.allowed_domains).extract_links(response):
            item = UrlKnef()
            item['url'] =  link.url
            item['time'] = str(datetime.now())
            item['urlComes'] = response.url
            self.logger.info('Link url search: %s', link.url)
            return item

def start_Crawler():
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    starturl = raw_input('[$ crawler $] Insert url which the crawler start > ')


    process.crawl(Knef, startUrl = starturl)
    process.start()

#if __name__ == "__main__":
 #   process = CrawlerProcess({
  #      'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
   # })

    #starturl = raw_input('[$ crawler $] Insert url which the crawler start > ')


    #process.crawl(Knef, startUrl = starturl)
    #process.start()