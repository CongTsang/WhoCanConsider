# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re

from scrapy.exceptions import DropItem

from weiboComment.items import WeibocommentItem
from weiboComment.items import WordcommentItem


class WeiboPipeline(object):

    def process_item(self, item, spider):
        if item.get('word'):
            return item
        else:
            raise DropItem("There is no words")


class CommentPipeline(object):

    def __init__(self):
        self.file = open("../data/comments.txt", 'wb')

    def process_item(self, item, spider):
        if isinstance(item, WordcommentItem):
            if item.get('comment'):
                comment = item.get('comment')
                if comment != '回复' and comment != '转发微博' and comment != ':' and comment:
                    if re.match(':.*?', comment):
                        item['comment'] = item['comment'].lstrip(':').strip()
                    else:
                        item['comment'] = item['comment'].strip()
                    self.file.write((item['comment'] + "\n").encode())
                    return item
                else:
                    raise DropItem("contain illegal str %s" % item)

    def close_spider(self, spider):
        self.file.close()
