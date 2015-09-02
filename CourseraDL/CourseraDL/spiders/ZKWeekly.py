# download weekly material from zk
from os import path
import scrapy
import os

results=[]
#basePath="D:/Weekly_Logic/"
basePath="D:/Weekly_Eng/"
#basePath="D:/Weekly_Math/"
#baseTitle="Logic"
baseTitle="Eng"
#baseTitle="Math"
baseUrl="http://bbs.zhongkaiedu.com/"
def getHrefs(txt):
	sel =scrapy.selector.Selector(text=txt)
	num =0
	for op in sel.xpath("//ignore_js_op"):
		num=num+1
	
	print 'table ignore_js_op', num

class ZKWeekly(scrapy.spiders.Spider):
	name="ZKWeekly"
	#start_urls=["http://bbs.zhongkaiedu.com/thread-183011-1-1.html"]
	start_urls=["http://bbs.zhongkaiedu.com/thread-183044-1-1.html"]
	#start_urls=["http://bbs.zhongkaiedu.com/thread-183010-1-1.html"]
	
	def parse(self,response):
		
		for temp in response.xpath('//div[@class="pcb"]/div[@class="t_fsz"]/table'):
			sel=scrapy.selector.Selector(text=temp.extract())
			if(len(sel.xpath("//ignore_js_op"))<=0):
				continue
			else:
				num =0
				for op in sel.xpath("//ignore_js_op"):
					num=num+1
					sel2=scrapy.selector.Selector(text=op.extract())
					title=baseTitle+sel2.xpath("//span/a/text()").extract()[0]
					print "title: ",title
					href=baseUrl+sel2.xpath("//span/a/@href").extract()[0]
					yield scrapy.Request(href,meta={'localfilename':title},callback=self.saveFile)
				print "ignore_js_op count",num
				
	def saveFile(self,response):
		fileFullName=path.join(basePath,response.meta['localfilename'])
		if path.exists(fileFullName):
			return
		else:
			with open(fileFullName,"wb") as f:
				f.write(response.body)
	