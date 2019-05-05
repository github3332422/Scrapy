import random
import re

import requests
import time
from lxml import etree

from lagouSpider.items import positionItem

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}


def request_list_page(i):
    url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
    response = requests.get(
        'https://www.lagou.com/jobs/list_%E5%A4%A7%E6%95%B0%E6%8D%AE?labelWords=&fromSearch=true&suginput=',
        headers=headers)  # 请求原网页
    r = requests.utils.dict_from_cookiejar(response.cookies)  # 获取cookies
    print(r)
    cookies = {
        'X_MIDDLE_TOKEN': '42daf4b72327b2810380076551bf5e71415983ed09',
        'JSESSIONID': 'ABAAABAAAGGABCB6F2700E7C8843B391A605A792F2C6FC5',
        '_ga': 'GA1.2.1912257997.1548059451',
        '_gat': '1',
        'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1548059451',
        'user_trace_token': '20190501165350-0542640b-1bac-46a0-9656-facb67d3e855',
        'LGSID': '20190121163050-dbd72f67-1d56-11e9-8927-525400f775ce',
        'PRE_UTM': '',
        'PRE_HOST': '',
        'PRE_SITE': '',
        'PRE_LAND': 'https%3A%2F%2Fwww.lagou.com%2F%3F_from_mid%3D1',
        'LGUID': '20190121163050-dbd73128-1d56-11e9-8927-525400f775ce',
        '_gid': 'GA1.2.1194828713.1548059451',
        'index_location_city': '%E5%85%A8%E5%9B%BD',
        'TG-TRACK-CODE': 'index_hotjob',
        'LGRID': '20190121163142-fb0cc9c0-1d56-11e9-8928-525400f775ce',
        'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1548059503',
        'SEARCH_ID': '9d3ad2aadaa14904beb81d25f5898605'
    }
    cookies.update(r)  # 更新接口的cookies
    data_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
        'Referer': 'https://www.lagou.com/jobs/list_%E5%A4%A7%E6%95%B0%E6%8D%AE?labelWords=&fromSearch=true&suginput='
    }
    data = {
        'first': 'false',
        'pn': 1,
        'kd': '大数据'
    }
    data['pn'] = i
    response = requests.post(url, headers=data_headers, data=data, cookies=cookies)
    result = response.json()
    positions = result['content']['positionResult']['result']
    # print(type(positions))
    # print("*" * 50)
    for position in positions:
        # print(position,type(position))
        print("*"*50)
        parse_position_detail(position)
    time.sleep(random.randint(5, 20))


def parse_position_detail(position):
    item = positionItem()
    companyFullName = position['companyFullName']
    item['companyFullName'] = companyFullName
    industryField = position['industryField']
    item['industryField'] = industryField
    education = position['education']
    item['education'] = education
    workYear = position['workYear']
    item['workYear'] = workYear
    city = position['city']
    item['city'] = city
    print(item)
    # return item
    # positionAdvantage = position['positionAdvantage']
    # item.append(positionAdvantage)
    # salary = position['salary']
    # item.append(salary)
    # positionName = position['positionName']
    # item.append(positionName)
    # companySize = position['companySize']
    # item.append(companySize)
    # companyLabelList = position['companyLabelList']
    # item.append(companyLabelList)
    # positionLables = position['positionLables']
    # item.append(positionLables)
    # industryLables = position['industryLables']
    # item.append(industryLables)
    # print(item)

def main():
    for i in range(1,2):
        request_list_page(i)


if __name__ == '__main__':
    main()