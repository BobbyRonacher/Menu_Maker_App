# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import json
from datetime import datetime


class CheckItemPipeline:
    def process_item(self, recipe, spider):
        if not recipe['url']:
            raise DropItem('Missing url!')
        if not recipe['title']:
            raise DropItem('Missing Title!')
        if not recipe['rating']:
            raise DropItem('Missing rating!')
        if not recipe['nutrition']:
            raise DropItem('Missing nutrition!')
        if not recipe['category']:
            recipe['category'] = ''
        return recipe


class CheckReviewsAndRatings:
    def process_item(self, recipe, spider):
        if recipe['source'] != 'hellofresh':
            if recipe['rating'] < 5 and recipe['reviewCount'] < 10 \
                    or recipe['rating'] < 4.75 and recipe['reviewCount'] < 25 \
                    or recipe['rating'] < 4.5 and recipe['reviewCount'] < 40 \
                    or recipe['rating'] < 4 and recipe['reviewCount'] < 50:
                raise DropItem('High rating but not enough reviews')
            if recipe['rating'] < 3.5:
                raise DropItem('Rating too low')
        return recipe
    ### is rating saving as a string? Cast it as float during check item pipeline?


class ParseOutputPipeline:
    def process_item(self, recipe, spider):
        if recipe['source'] in ('delish'):
            recipe['calories'] = recipe['nutrition'][0].split(',')[0].split(':')[1].replace('calories', '').strip()
            recipe['protein'] = recipe['nutrition'][0].split(',')[1].replace('protein', '').replace('g', '').strip()
            recipe['carbs'] = recipe['nutrition'][0].split(',')[2].replace('carbohydrates', '').replace('g', '').strip()
            recipe['fat'] = recipe['nutrition'][0].split(',')[5].replace('fat', '').replace('g', '').strip()
        if recipe['source'] in ('hellofresh', 'allrecipes', 'foodnetwork', 'taste_of_home'):
            recipe['calories'] = recipe['nutrition']['calories'].strip().split(' ')[0]
            recipe['protein'] = recipe['nutrition']['proteinContent'].strip().split(' ')[0].replace('g', '').strip()
            recipe['carbs'] = recipe['nutrition']['carbohydrateContent'].strip().split(' ')[0].replace('g', '').strip()
            recipe['fat'] = recipe['nutrition']['fatContent'].strip().split(' ')[0].replace('g', '').strip()

        if recipe['calories'] == '' or recipe['protein'] == '' or recipe['carbs'] == '' or recipe['fat'] == '':
            raise DropItem('Blank nutrition!')

        return recipe