import json
baseUrl = 'https://fe-api.zhaopin.com/c/i/sou?start={0}&pageSize=90&cityId=489&kw={1}&kt=3'

offset = 0  # 偏移量
with open('keywords.json', 'r') as f:
    keywords_list = json.load(f)

start_urls = []

for item in keywords_list:
    for job_key in item['Job_keywords']:
        start_urls.append(baseUrl.format(str(offset), job_key))

for url in start_urls:
    print(url)