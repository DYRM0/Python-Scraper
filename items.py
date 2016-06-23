# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DmozItem(scrapy.Item): #I added this dmoz item class from the scrapy tutorial
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()

class rateyourmusicalbum(scrapy.Item):
	title = scrapy.Field()
	date = scrapy.Field()
	rating = scrapy.Field()
	artist = scrapy.Field()
	
class rateyourmusicartist(scrapy.Item):
	artisttype = scrapy.Field()
	genre = scrapy.Field()
	dateofbirth = scrapy.Field()
	nationality = scrapy.Field()
	status = scrapy.Field()
	statusinfo = scrapy.Field()
	statusinfo2 = scrapy.Field()
	name = scrapy.Field()
	
	
class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
