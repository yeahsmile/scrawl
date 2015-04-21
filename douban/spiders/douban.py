# -*- coding:utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from douban.items import DoubanItem
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

class DoubanSpider(CrawlSpider) :

    name = "douban" 
    allowed_domains = ["movie.douban.com"]
    start_urls = ["http://movie.douban.com/top250"]
    rules = (
        Rule(SgmlLinkExtractor(allow = (r'http://movie\.douban\.com/top250\?start=\d+&filter=&type=',))),
        Rule(SgmlLinkExtractor(allow = (r'http://movie\.douban\.com/subject/\d+', )), callback = 'parse_page', follow = True),
        )

    def parse_page(self, response) :
        sel = Selector(response)
        item = DoubanItem()
        item['name'] = sel.xpath('//h1/span[@property="v:itemreviewed"]/text()').extract()
        item['description'] = sel.xpath('//div/span[@property="v:summary"]/text()').extract()
        item['url'] = response.url
        return item
