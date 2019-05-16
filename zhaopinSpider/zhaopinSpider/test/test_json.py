import json
with open('F:\Python\Scrapy\zhaopinSpider\keywords.json', 'r') as f:
    keywords_list = json.load(f)
baseUrl = 'https://fe-api.zhaopin.com/c/i/sou?start={0}&pageSize=90&cityId=489&kw={1}&kt=3'

offset = 0
start_urls = []
for job_key in start_urls['Job_keywords']:
    start_urls.append(baseUrl.format(str(offset), job_key))
print(keywords_list['Job_keywords'])