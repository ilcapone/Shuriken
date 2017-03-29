# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv

class ShurikencrawlerPipeline(object):

    def process_item(self, item, spider):
        return item

class CsvShurikenPipeline(object):
	def __init__(self):
		self.csvwriter = csv.writer(open('links_crawler.csv', 'wb'))

	def process_item(self, item, Knef):
		row = item['url']
        row = item['time']
        row = item['urlComes']
        self.csvwriter.writerow(row)
        return item