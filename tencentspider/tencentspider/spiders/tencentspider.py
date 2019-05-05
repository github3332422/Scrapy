import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from tencentspider.items import TencentspiderItem

'''
注意:
    1.方法不能是parse    如果是parse的话，只能爬取到第一页。
    2.rules只能是元组，不能是字典。     如果是字典的话，会匹配，但是不会获取到数据
'''
class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ["https://hr.tencent.com/position.php?&start=0"]
    # rules = (
    #     Rule(LinkExtractor(allow=("start=\d+")), callback="parseTencent", follow=True),
    # )
    rules = [Rule(LinkExtractor(allow=("start=\d+")), callback="parseTencent", follow=True)]

    def parseTencent(self, response):
        items = []
        trs = response.xpath("//table[@class='tablelist']//tr")[1:-1]
        for tr in trs:
            # print(tr)
            # positionName = tr.xpath("./td[1]/a/text()")[0].extract()
            # positionType = tr.xpath("./td[2]//text()")[0].extract()
            # positionNum = tr.xpath("./td[3]//text()")[0].extract()
            positionName = tr.xpath("./td[1]/a/text()").extract()
            if len(positionName) > 0:
                positionName = positionName[0]
            else:
                positionName = " "
            positionType = tr.xpath("./td[2]//text()").extract()
            if len(positionType) > 0:
                positionType = positionType[0]
            else:
                positionType = " "
            positionNum = tr.xpath("./td[3]//text()").extract()
            if len(positionNum) > 0:
                positionNum = positionNum[0]
            else:
                positionNum = " "
            # print(positionName,positionType,positionNum)
            item = TencentspiderItem()
            item['name']= positionName
            item['type'] = positionType
            item['number'] = positionNum
            items.append(item)
        return items


