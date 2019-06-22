# -*- coding: utf-8 -*-

from scrapy import Request, Spider
from weiboComment.items import WordcommentItem


class WordcommentSpider(Spider):
    name = 'wordcomment'
    allowed_domains = ['weibo.cn']
    start_urls = ['https://weibo.cn/search/mblog']
    custom_settings = {
        'ITEM_PIPELINES': {
            'weiboComment.pipelines.CommentPipeline': 300
        }
    }

    word = ''
    host_url = 'https://weibo.cn'
    search_url = 'https://weibo.cn/search/mblog/?keyword={keyword}&filter=hasori&sort=hot'
    page = '&page=1'

    def start_requests(self):
        print("Input the search word in the web page, such as \"CongTsang\":")
        self.word = input("word: ")
        yield Request(self.search_url.format(keyword=self.word), self.parse_search)

    def parse_search(self, response):
        detail_url = response.css('.cc::attr(href)').extract_first()
        detail_url = detail_url[:-7] + self.page
        yield Request(detail_url, self.parse_comment)

    def parse_comment(self, response):
        comments = response.css('.ctt::text').extract()
        next = response.xpath('//a[text()="下页"]/@href').extract_first()
        if next:
            next = self.host_url + next
            item = WordcommentItem()
            for comment in comments:
                item['comment'] = comment

            yield item
            yield Request(next, self.parse_comment)
