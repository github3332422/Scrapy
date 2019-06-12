# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request
from urllib import  parse
class PccnblogSpider(scrapy.Spider):
    name = 'pcallblog'
    allowed_domains = ["blog.jobbole.com"]
    start_urls = ["http://blog.jobbole.com/all-posts/"]
    def parse(self, response):
        post_urls = response.css("#archive .floated-thumb .post-thumb a::attr(href)").extract()
        for post_url in post_urls:
            yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse_detail)

        next_url = response.css(".next.page-numbers::attr(href)").extract_first("")
        if next_url:
            yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse)
    def parse_detail(self,response):
        title = response.css(".entry-header h1::text").extract()[0]
        date = response.css("p.entry-meta-hide-on-mobile::text").extract()[0].strip().replace("¡¤","").strip()
        praise_nums = response.css(".vote-post-up h10::text").extract()[0]
        fav_nums = response.css(".bookmark-btn::text").extract()[0]
        match_re = re.match(".*(\d+).*",fav_nums)
        if match_re:
            fav_nums = match_re.group(1)
        else:
            fav_nums = 0
        comment_nums = response.css("a[href='#article-comment'] span::text").extract()[0]
        match_re = re.match(".*(\d+).*",comment_nums)
        if match_re:
            comment_nums = match_re.group(1)
        else:
            comment_nums = 0
        content = response.css("div.entry").extract()[0]
        tag_list = response.css("p.entry-meta-hide-on-mobile a::text").extract()
        tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        tags = ",".join(tag_list)
        print("tags:",tags)
        print("title:",title)
        print("date:",date)
        print("praise_nums:",praise_nums)
        print("fav_nums:",fav_nums)
        print("comment_nums:",comment_nums)
        print("content:",content)
        pass
