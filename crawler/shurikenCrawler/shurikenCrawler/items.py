# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UrlKnef(scrapy.Item):
	Id = scrapy.Field()
	url = scrapy.Field()
	time = scrapy.Field()
	urlComes = scrapy.Field()

class VulnWeb(scrapy.Item):
	url = scrapy.Field()
	ip = scrapy.Field()
	port = scrapy.Field()
	time = scrapy.Field()
	server = scrapy.Field()
	XSS_Protection = scrapy.Field()	
