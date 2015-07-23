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
		count =0;
		for sel in response.xpath("//body[@class='issue']"):
			print sel.extract()
			item=ManongItem()
			item['desc']=sel.xpath("/p").extract()
			item['address']=sel.xpath("/h4/a/@href").extract()
			item['title']=sel.xpath("/h4/a/text()").extract()
			yield item
			count=count+1
			if(count>2):
				print("parse_issue twice *******************************")
				break