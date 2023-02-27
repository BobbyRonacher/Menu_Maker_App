import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from recipe_scraper.items import Recipe
import json

class FoodNetworkSpider(CrawlSpider):
    name = 'food_network'
    allowed_domains = ['foodnetwork.com']
    # start_urls = ['https://foodnetwork.com/recipes']
    start_urls = ['https://www.foodnetwork.com/recipes/food-network-kitchen/healthy-vegetable-and-couscous-stuffed-peppers-9541673']

    rules = [Rule(LinkExtractor(allow=r'food-network-kitchen'), callback='parse_info', follow=True)]

    def parse_info(self, response):
        recipe = Recipe()
        recipe['title'] = json.loads(response.xpath('//script[@type="application/ld+json"]//text()').extract_first())[0]['headline']
        recipe['url'] = response.url
        try:
            recipe['rating'] = float(json.loads(response.xpath('//script[@type="application/ld+json"]//text()').extract_first())[0]['aggregateRating']['ratingValue'])
            recipe['reviewCount'] = int(json.loads(response.xpath('//script[@type="application/ld+json"]//text()').extract_first())[0]['aggregateRating']['reviewCount'])
            # recipe['reviewCount'] = int(ratingdict['ratingCount'])
        except:
            recipe['rating'] = ''
            recipe['reviewCount'] = ''
        try:
            if 'nutrition' in json.loads(response.xpath('//script[@type="application/ld+json"]//text()').extract_first())[0].keys():
                recipe['nutrition'] = json.loads(response.xpath('//script[@type="application/ld+json"]//text()').extract_first())[0]['nutrition']
        except:
            recipe['nutrition'] = ''
        recipe['source'] = 'foodnetwork'
        recipe['category'] = json.loads(response.xpath('//script[@type="application/ld+json"]//text()').extract_first())[0]['recipeCategory']
        return recipe

