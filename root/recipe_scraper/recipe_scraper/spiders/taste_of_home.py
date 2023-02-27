import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from recipe_scraper.items import Recipe
import json


class TasteOfHomeSpider(CrawlSpider):
    name = 'taste_of_home'
    allowed_domains = ['www.tasteofhome.com']
    start_urls = ['https://www.tasteofhome.com/recipes/harvesttime-chicken-with-couscous/']

    rules = [Rule(LinkExtractor(allow=r'/recipes/'), callback='parse_info', follow=True)]


    def parse_info(self, response):
        recipe = Recipe()
        recipe['url'] = response.url
        try:
            recipe['title'] = json.loads(response.xpath('//script[@type="application/ld+json"]//text()').extract_first())['name']
        except:
            recipe['title'] = ''
        try:
            recipe['rating'] = json.loads(response.xpath('//script[@type="application/ld+json"]//text()').extract_first())['aggregateRating']['ratingValue']
        except:
            recipe['rating'] = ''
        try:
            recipe['reviewCount'] = json.loads(response.xpath('//script[@type="application/ld+json"]//text()').extract_first())['aggregateRating']['reviewCount']
        except:
            recipe['reviewCount'] = ''
        try:
            recipe['nutrition'] = json.loads(response.xpath('//script[@type="application/ld+json"]//text()').extract_first())['nutrition']
        except:
            recipe['nutrition'] = ''
        try:
            recipe['category'] = json.loads(response.xpath('//script[@type="application/ld+json"]//text()').extract_first())['recipeCategory']
        except:
            recipe['category'] = ''
        recipe['source'] = 'taste_of_home'


        return recipe

