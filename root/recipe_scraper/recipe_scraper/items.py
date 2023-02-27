# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Recipe(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    rating = scrapy.Field()
    reviewCount = scrapy.Field()
    nutrition = scrapy.Field()
    source = scrapy.Field()
    calories = scrapy.Field()
    protein = scrapy.Field()
    carbs = scrapy.Field()
    fat = scrapy.Field()
    category = scrapy.Field()
