# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


#item for the links in the issue
# define the fields for your item here like:
# name = scrapy.Field()
class ManongItem(scrapy.Item):
	title=scrapy.Field()
	desc=scrapy.Field()
	address=scrapy.Field()
    
	
