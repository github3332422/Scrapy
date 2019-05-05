# -*- coding: utf-8 -*-
import scrapy
from lagouSpider.items import LagouspiderItem


class LagouSpider(scrapy.Spider):
    name = 'lagou'
    allowed_domains = ['lagou.com']
    start_urls = ['https://www.lagou.com/zhaopin/shujuwajue/{}/'.format(i) for i in range(1,31)]

    def parse(self, response):
        lis = response.xpath("//li[@class='con_list_item default_list']")
        items = []
        for li in lis:
            item = LagouspiderItem()
            positionName = li.xpath(".//a[@class='position_link']//h3//text()").extract()[0].strip()
            item['positionName'] = positionName
            positionUrl = li.xpath(".//a[@class='position_link']/@href").extract()[0].strip()
            item['positionUrl'] = positionUrl
            positionPlace = li.xpath(".//span[@class='add']/em//text()").extract()[0].strip()
            item['positionPlace'] = positionPlace
            positionSalary = li.xpath(".//span[@class='money']//text()").extract()[0].strip()
            item['positionSalary'] = positionSalary
            #经验和学历
            positionll = str(li.xpath(".//div[@class='li_b_l']/text()").extract()[2]).strip()
            ll = positionll.split('/')
            positionExper = ll[0]
            item['positionExper'] = positionExper
            positionEdu = ll[1]
            item['positionEdu'] = positionEdu
            # positionll = re.sub(r"[\s/ ]", "", positionll)

            companyName = li.xpath(".//div[@class='company_name']/a/text()").extract()[0].strip()
            item['companyName'] = companyName
            #公司介绍
            positiondata = str(li.xpath(".//div[@class='industry']/text()").extract()).strip().split('/')
            companyNature = positiondata[0].strip()
            companyNature = companyNature.replace(" ","")[4:-1]
            item['companyNature'] = companyNature
            companyScale = positiondata[-1].strip()
            companyScale = companyScale.replace(" ", "")[0:-4]
            item['companyScale'] = companyScale
            # positiondata = re.sub(r"[\s/ ]", "", positiondata)
            positionClaim = li.xpath(".//div[@class='li_b_l']/span/text()").extract()#福利
            item['positionClaim'] = positionClaim
            positionAttract = li.xpath(".//div[@class='li_b_r']//text()").extract()[0].strip()
            item['positionAttract'] = positionAttract
            # print(positionName,positionUrl,positionPlace,positionSalary,positionExper,positionEdu,companyName,companyNature,companyScale,positionClaim,positionAttract)
            # print("*"*10)
            # return item
            print(item)
            print("*"*50)
            items.append(item)
        return items
