# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import json

class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open("URLs_from_IndeedSpider.json", 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
	
	def from_crawler(cls, crawler):
		settings = crawler.settings
		self.filename = settings.get("FEED_URI")
		return cls(my_setting)