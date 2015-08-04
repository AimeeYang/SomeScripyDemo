# Download courese material from Coursera
from os import path
import scrapy
import os

#keywords=[u'PDF',u'Subtitles (srt)',u'Video (MP4)']
keywords=[{'key':u'PDF','suffix':'.pdf'},{'key':u'Subtitles (srt)','suffix':'.srt'},{'key':u'Video (MP4)','suffix':'.mp4'}]
specialSymbols=['?',':']
results=[]
basePath="D:/CD/"

def varifyFileName(fname):
	for symbol in specialSymbols:
		fname=fname.replace(symbol,'')
	return fname
def getHrefs(htmltxt):
	sel=scrapy.selector.Selector(text=htmltxt)
	for keyword in keywords:
		if str(htmltxt).find(keyword['key']) != -1:
			addressPath="//a[@title='"+keyword['key']+"']/@href"
			address=sel.xpath(addressPath).extract()[0]
			filenamePath="//a[@title='"+keyword['key']+"']/div/text()"
			filename=sel.xpath(filenamePath).extract()[0]+keyword['suffix']
			filename=varifyFileName(filename)
			result={'address':address,'filename':filename}
			results.append(result)	
	
	
class CourseraDL(scrapy.spiders.Spider):
	name='courseraDL'
	start_urls=['https://class.coursera.org/ml-003/lecture']
	#start_urls=['https://d396qusza40orc.cloudfront.net/ml/docs/slides/Lecture1.pdf']
	
	def parse2(self,response):
		print 'type', type(response)
		
	def parse(self,response):
		count=0
		for resource in response.xpath('//div[@class="course-lecture-item-resource"]'):
			getHrefs(resource.extract())
			count=count+1;
			if count>2:
				break
		for result in results:
			#print 'result.address', result['address'], type(result['address'])
			yield scrapy.Request(result['address'],meta={'localfilename':result['filename']},callback=self.saveFile)
	
	def saveFile(self,response):
		fileFullName=path.join(basePath,response.meta['localfilename'])
		if path.exists(fileFullName):
			return
		else:
			with open(fileFullName,"wb") as f:
				f.write(response.body)