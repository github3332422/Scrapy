# -*- coding: utf-8 -*-
import scrapy
from emojispider.items import EmojispiderItem

class EmoSpider(scrapy.Spider):
    name = 'emo'
    allowed_domains = ['webfx.com/tools/emoji-cheat-sheet/']
    start_urls = ['http://webfx.com/tools/emoji-cheat-sheet/']

    def parse(self, response):
        headers = response.xpath("//h2")
        lists = response.xpath("//ul")
        all_items = []
        for header,list in zip(headers,lists):
            section = header.xpath("text()").extract()[0]
            for li in list.xpath("li"):
                item = EmojispiderItem()
                item['section'] = section
                spans = li.xpath("div/span")
                if len(spans):
                    link = spans[0].xpath("@data-src").extract()
                    if link:
                        item['emoji_link'] = response.url + link[0]
                    handle_code = spans[1].xpath('text()').extract()
                else:
                    handle_code = li.xpath("div/text()").extract()
                if handle_code:
                    item['emoji_handle'] = handle_code[0]
                print(item)
                yield item
            all_items.append(item)
            # yield all_items
# if __name__ == '__main__':
