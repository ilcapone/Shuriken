import scrapy
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