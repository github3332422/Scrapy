import requests
cookies = {
            'X_MIDDLE_TOKEN': '42daf4b72327b2813110076551bf5e71415983ed09',
            'JSESSIONID': 'ABAAABAAAFCAAEGBF8CF664800052ACD736EF5CE24E3052',
            '_ga': 'GA1.2.1912257997.1548059451',
            '_gat': '1',
            'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1548059451',
            'user_trace_token': '20190501164153-ae06a11a-62f0-4f21-b76a-4fc8b7e96e09',
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
            'SEARCH_ID': '78af44107149423086b7600d96d8c36c'
        }
headers = {
    'Origin': 'https://www.lagou.com',
    'X-Anit-Forge-Code': '0',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Referer': 'https://www.lagou.com/jobs/list_java?px=new&city=%E4%B8%8A%E6%B5%B7',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'X-Anit-Forge-Token': 'None',
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
