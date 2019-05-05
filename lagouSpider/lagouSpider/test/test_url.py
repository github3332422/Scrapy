start_urls = ['https://www.lagou.com/zhaopin/shujuwajue/{}/?filterOption={}'.format(i,i) for i in range(1,31)]

for url in start_urls:
    print(url)