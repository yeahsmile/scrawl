from scrapy.spider import BaseSpider
class DouBanImage(BaseSpider):
    name = "douban"
    allowed_domains = ["douban.com"]
    filename = 'douban.txt'
    f = open(filename,'wb')

    for i in range(0,1560,40):
        start_urls = [
        "http://movie.douban.com/subject/10581289/photos?type=S"]



    def parse(self,response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//ul/li/div/a/img/@src').extract()
        items = []

        for site in sites:
        	site = site.replace('thumb','raw')
        	self.f.write(site)
        	self.f.write('\r\n')
        	item = DoubanimageItem()
        	item['ImageAddress'] = site
        	items.append(item)
        return items
        