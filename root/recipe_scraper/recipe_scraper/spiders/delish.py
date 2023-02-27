import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from recipe_scraper.items import Recipe
import json


class SimplyRecipesSpider(CrawlSpider):
    name = 'delish'
    allowed_domains = ['delish.com']
    start_urls = ['https://www.delish.com/cooking/recipe-ideas']

    rules = [Rule(LinkExtractor(allow=r'recipe-ideas\/[:alphanum:]'), callback='parse_info', follow=True)]


    def parse_info(self, response):
        recipe = Recipe()
        recipe['url'] = response.url
        try:
            recipe['title'] = json.loads(response.xpath('//script[@type="application/ld+json"]//text()').extract_first())['headline']
        except:
            recipe['title'] = json.loads(response.xpath('//script[@type="application/ld+json"]//text()').extract_first())[0]['headline']
        recipe['nutrition'] = ''
        recipe['rating'] = ''
        recipe['reviewCount'] = ''
        if 'aggregateRating' in json.loads(response.xpath('//script[@type="application/ld+json"]//text()').extract_first()).keys():
            ratingDict = json.loads(response.xpath('//script[@type="application/ld+json"]//text()').extract_first())['aggregateRating']
            recipe['rating'] = float(ratingDict['ratingValue'])
            recipe['reviewCount'] = ratingDict['reviewCount']
        if len(response.xpath('//em//text()').extract()) > 0:
           if 'Nutrition' in response.xpath('//em//text()').extract()[0]:
               recipe['nutrition'] = response.xpath('//em//text()').extract()
        recipe['category'] = json.loads(response.xpath('//script[@type="application/ld+json"]//text()').extract_first())['recipeCategory']
        recipe['source'] = 'delish'


        return recipe

