import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from recipe_scraper.items import Recipe
import json


class bbcgoodfoodSpider(CrawlSpider):
    name = 'bbcgoodfood'
    allowed_domains = ['bbcgoodfood.com']
    start_urls = ['https://www.bbcgoodfood.com/recipes/']

    rules = [Rule(LinkExtractor(allow=r'recipes\/'), callback='parse_info', follow=True)]

    def parse_info(self, response):
        recipe = Recipe()
        recipe['url'] = response.url
        try:
            recipe['title'] = json.loads(response.xpath('//script[@type="application/ld+json"]//text()').extract_first())['name']
        except:
            recipe['title'] = ''
        recipe['rating'] = .10
        recipe['reviewCount'] = .10
        try:
            recipe['nutrition'] = json.loads(response.xpath('//script[@type="application/ld+json"]//text()').extract_first())['nutrition']
        except:
            recipe['nutrition'] = ''
        try:
            recipe['category'] = json.loads(response.xpath('//script[@type="application/ld+json"]//text()').extract_first())['recipeCategory']
        except:
            recipe['category'] = ''
        recipe['source'] = 'bbcgoodfood'

        return recipe

