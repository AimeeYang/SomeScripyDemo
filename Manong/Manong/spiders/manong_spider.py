# -*- coding: utf-8 -*-
#from scrapy.Spider import Spider #wrong path
import scrapy
from Manong.items import ManongItem


class MaNongSpider(scrapy.spiders.Spider):
	name="Manong"
	start_urls=['http://weekly.manong.io/issues/']
	
	#default callback function
	def parse(self,response):
		count = 1
		for href in response.xpath("//div[@class='issue']/h4/a/@href"):
			if(count<2):
				full_url=response.urljoin(href.extract())
				yield scrapy.Request(full_url,callback=self.parse_issue)
				#print sel.xpath('/@href').extract()
				count=count+1
			else:
				return
			
			
	def parse_issue(self,response):
		print('parse_issue in ==============================')
		for sel in response.xpath("//body[@class='issue']/h4"):
			#print sel.extract().encode('utf-8','ignore').decode('utf-8','ignore')
			#print sel.extract().decode('utf-8','ignore').encode('GB18030')
			#print sel.extract().decode('unicode','ignore').encode('GB18030')
			#below is check sel coding type, result is unicode
			#if isinstance(sel.extract(),str):
			#	print 'sel is str type'
			#elif isinstance(sel.extract(),unicode):
			#	print 'sel is unicode'
			#else:
			#	print 'sel is neigher str nor unicode'
			print sel.extract().encode('GB18030')
			item=ManongItem()
			item['address']=sel.xpath('//a/@href').extract()
			#item['desc']=unicode(sel.xpath("//..").xpath("//p/text()").extract()[0],errors='ignore').encode('GB18030')
			#item['address']=sel.xpath("//a/@href").extract()
			#item['title']=unicode(sel.xpath("//a/text()").extract()[0],errors='ignore').encode('GBK','ignore')
			#item['desc']=sel.xpath("//..").xpath("//p/text()").extract()[0].decode('unicode','ignore').encode('GB18030')
			#item['address']=sel.xpath("//a/@href").extract()
			#item['title']=sel.xpath("//a/text()").extract()[0].decode('unicode','ignore').encode('GBK','ignore')
			#item['desc']=sel.xpath("//..").xpath("//p/text()").extract()[0].decode('utf-8','ignore').encode('GB18030')
			#item['address']=sel.xpath("//a/@href").extract()
			#item['title']=sel.xpath("//a/text()").extract()[0].decode('utf-8','ignore').encode('GBK','ignore')
			#item['desc']=sel.xpath("//..").xpath("//p/text()").extract().encode('utf-8','ignore').decode('urf-8',ignore)
			#item['address']=sel.xpath("//a/@href").extract()
			#item['title']=sel.xpath("//a/text()").extract().encode('utf-8','ignore').decode('utf-8',ignore)			
			yield item
	
	