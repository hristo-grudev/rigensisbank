import re

import scrapy

from scrapy.loader import ItemLoader
from ..items import RigensisbankItem
from itemloaders.processors import TakeFirst


class RigensisbankSpider(scrapy.Spider):
	name = 'rigensisbank'
	start_urls = ['http://www.rigensisbank.com/lv/jaunumi/']

	def parse(self, response):
		pages_links = response.xpath('//div[@class="pagenav"]/ul/li/a/@href').getall()
		for link in pages_links:
			yield response.follow(link, self.parse_page)

	def parse_page(self, response):
		article_links = response.xpath('//div[@class="title"]/a/@href')
		yield from response.follow_all(article_links, self.parse_post)

	def parse_post(self, response):
		title = response.xpath('//h1/text()').get()
		description = response.xpath('//div[@class="info"]//text()').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()
		date = response.xpath('//div[@class="date"]/div/text()').getall()
		date = ' '.join(date).strip()

		item = ItemLoader(item=RigensisbankItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
