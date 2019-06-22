# -*- coding: utf-8 -*-

from scrapy import Request, Spider
import re
from weiboComment.items import WeibocommentItem


class WeiboSpider(Spider):
    name = 'weibo'
    allowed_domains = ['weibo.cn']
    start_urls = ['http://weibo.cn/']
    custom_settings = {
        'ITEM_PIPELINES': {
            'weiboComment.pipelines.WeiboPipeline': 300
        }
    }

    hot_rank = 'https://s.weibo.com/top/summary?cate=realtimehot'

    def start_requests(self):
        yield Request(self.hot_rank, self.parse_words)

    def parse_words(self, response):
        results = response.css('tr')
        pattern = re.compile('<a.*?href.*?="(.*?)".*?>(.*?)</a>.*?<span>(.*?)</span>', re.S)

        for result in results:
            str = result.css('.td-02').extract_first()
            if str:
                lists = re.findall(pattern, str)
                item = WeibocommentItem()
                for list in lists:
                    item['word'] = list[1]
                    item['hot'] = list[2]
                yield item
