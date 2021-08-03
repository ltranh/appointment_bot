# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BurgerbotItem(scrapy.Item):
    # define the fields for your item here like:
    date = scrapy.Field()
    time = scrapy.Field()
    clas = scrapy.Field()
    month= scrapy.Field()
     
