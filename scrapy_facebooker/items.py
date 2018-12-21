# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class FacebookEvent(scrapy.Item):
    date = scrapy.Field()
    summary_date = scrapy.Field()
    summary_place = scrapy.Field()
    title = scrapy.Field()
    username = scrapy.Field()
    url = scrapy.Field()