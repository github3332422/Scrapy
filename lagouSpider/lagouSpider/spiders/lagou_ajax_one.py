import requests
'''
说明：拉勾网直接请求数据
参考链接:https://blog.csdn.net/qq_37462361/article/details/87856659
'''
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
}
response = requests.get('https://www.lagou.com/',headers=headers)  # 请求原网页
r = requests.utils.dict_from_cookiejar(response.cookies)  # 获取cookies
print(r)
# r["user_trace_token"] = r["LGRID"]
# r["LGSID"] = r["LGRID"]
# r["LGUID"] = r["LGRID"]  # 构造cookies的参数
cookies = {
    # 'X_MIDDLE_TOKEN': r['X_HTTP_TOKEN'],
    # 'JSESSIONID': r['JSESSIONID'],
    '_ga': 'GA1.2.1912257997.1548059451',
    '_gat': '1',
    'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1548059451',
    # 'user_trace_token': r['user_trace_token'],
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
    'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1548059503'
    # 'SEARCH_ID': r['SEARCH_ID']
}
cookies.update(r)  # 更新接口的cookies
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
    'Referer': 'https://www.lagou.com/jobs/list_%E5%A4%A7%E6%95%B0%E6%8D%AE?labelWords=&fromSearch=true&suginput='
}

params = (
    ('px', 'new'),
    ('city', '\u4E0A\u6D77'),
    ('needAddtionalResult', 'false'),
)

data = {'first': True,
        'kd': 'java',
        'pn': 1}
response = requests.post('https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false', headers=headers, params=params,
                         cookies=cookies, data=data)  # 请求接口
print(response.json())

