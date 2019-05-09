import requests
from lxml import etree
headers = {
        'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}

# response = requests.get('https://movie.douban.com/top250?start=225&filter=',headers = headers)
# html = etree.HTML(response.text)
#
# lis = html.xpath('//ol[@class="grid_view"]/li')
# for li in lis:
#     lis = li.xpath('.//span[@class="title"]//text()')
#     if len(lis) > 0 :
#         name = lis[0]
#     else:
#         name = ""
#
#     lis = li.xpath('.//span[@class="rating_num"]//text()')
#     if len(lis) > 0 :
#         score = lis[0]
#     else:
#         score = ""
#
#     lis = li.xpath('.//span[@class="inq"]//text()')
#     if len(lis) > 0:
#         context = lis[0]
#     else:
#         context = ""
#     print(name,score,context)
# # next_url = html.xpath('//span[@class="next"]/a/@href')
# # print(next_url)
# # print(response.text)
response = requests.get('https://movie.douban.com/subject/1295644/',headers = headers)
html = etree.HTML(response.text)
# spans = html.xpath("//div[@id='info']/span")
# name = html.xpath("//div[@id='content']/h1//text()")[1]
# print(name)
# score = html.xpath("//div[@class='rating_self clearfix']/strong//text()")[0]
# print(score)
# director = spans[0].xpath("./span[@class='attrs']//text()")
# print(director)
# screenwriter = spans[1].xpath("./span[@class='attrs']/a//text()")
# print(screenwriter)
# starring = spans[2].xpath("./span[@class='attrs']/a//text()")
# print(starring)
# type = html.xpath("//span[@property='v:genre']//text()")[1:]
# print(type)
# sytime = html.xpath("//span[@property='v:initialReleaseDate']//text()")
# print(sytime)
# movieslength = html.xpath("//span[@property='v:runtime']//text()")[0]
# print(movieslength)
# IMDB = html.xpath("//div[@id='info']//a[@target='_blank']//@href")[0]
# print(IMDB)
context = html.xpath("//span[@property='v:summary']//text()")[0].strip()
print(context.strip())

