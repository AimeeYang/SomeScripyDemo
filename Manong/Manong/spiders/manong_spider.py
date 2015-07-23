# -*- coding: utf-8 -*-
#from scrapy.Spider import Spider #wrong path
import scrapy
from Manong.items import ManongItem


class MaNongSpider(scrapy.spiders.Spider):
	name="Manong"
	start_urls=['http://weekly.manong.io/issues/']
	
	#default callback function
	def parse(self,response):
		for href in response.xpath("//div[@class='issue']/h4/a/@href"):
			full_url=response.urljoin(href.extract())
			yield scrapy.Request(full_url,callback=self.parse_issue)
			#print sel.xpath('/@href').extract()

	def parse_issue(self,response):
		print('parse_issue in ==============================')
		for sel in response.xpath("//body[@class='issue']/h4"):
			print sel.extract().encode('utf-8').decode('utf-8')
			item=ManongItem()
			item['desc']=sel.xpath("//..").xpath("//p/text()").extract().encode('utf-8').decode('urf-8')
			item['address']=sel.xpath("//a/@href").extract()
			item['title']=sel.xpath("//a/text()").extract().encode('utf-8').decode('utf-8')
			yield item