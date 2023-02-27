import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from recipe_scraper.items import Recipe
import json


class HelloFreshSpider(CrawlSpider):
    name = 'hellofresh'
    allowed_domains = ['hellofresh.com']
    start_urls = ['https://www.hellofresh.com/recipes']

    rules = [Rule(LinkExtractor(allow=r'recipes\/.*[\d]'), callback='parse_info', follow=True)]


    def parse_info(self, response):
        recipe = Recipe()
        recipe['url'] = response.url
        recipe['title'] = json.loads(response.xpath('//script[@type="application/ld+json"]//text()').extract_first())['name']
        recipe['rating'] = .10
        recipe['reviewCount'] = .10
        recipe['nutrition'] = json.loads(response.xpath('//script[@type="application/ld+json"]//text()').extract_first())['nutrition']
        recipe['category'] = json.loads(response.xpath('//script[@type="application/ld+json"]//text()').extract_first())['recipeCategory']
        recipe['source'] = 'hellofresh'

        return recipe

