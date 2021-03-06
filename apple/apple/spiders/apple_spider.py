# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider 
from scrapy.selector import HtmlXPathSelector 
from apple.items import AppleItem


class AppleSpider(BaseSpider):
	name = "apple"
	allowed_domains = ["apple.com"]
	start_urls = ['http://www.apple.com/itunes/charts/free-apps/']

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		apps = hxs.select('//section/div/ul/li')
		items = []
	
		for app in apps:
			item = AppleItem()
			item['app_name'] = app.select('.//h3/a/text()').extract()
			item['appstore_link']= app.select('.//h3/a/@href').extract()
			item['category']= app.select('.//h4/a/text()').extract()
			item['img_src']= app.select('.//a/img/@src').extract()

			items.append(item)
			

		return items 	
