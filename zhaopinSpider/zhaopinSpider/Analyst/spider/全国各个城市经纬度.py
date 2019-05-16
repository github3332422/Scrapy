import csv

import requests
import xlwt
from lxml import etree
url = 'https://blog.csdn.net/yang1994/article/details/6859935'

def get_html():
    response = requests.get(url)
    response = etree.HTML(response.text)
    print("数据获取完成")
    return response

def analy_html(response):
    trs = response.xpath("//div[@id='content_views']//tr")[1:]
    lis = []
    # for tr in trs[0:35]:
    #     data = tr.xpath('.//td[2]//text()')[0].split(':')
    #     # print(data,end=' ')
    #     city = data[0].split('经纬度')[0]
    #     du = data[1][1:-1].split(",")
    #     # print(city,du[0],du[1])
    #     # item = {
    #     #     'provience': city,
    #     #     'city':city,
    #     #     'thr':du[0],
    #     #     'dim':du[1]
    #     # }
    #     item = []
    #     item.append(city)
    #     item.append(city)
    #     item.append(du[1])
    #     item.append(du[0])
    #     lis.append(item)
    for tr in trs[37:]:
        data = tr.xpath('.//td[2]//text()')[0].split()
        # print(data)
        # item = {
        #     'provience':data[0],
        #     'city':data[1],
        #     'thr':data[2],
        #     'dim':data[3]
        # }
        item = []
        item.append(data[0])
        item.append(data[1])
        item.append(data[2][2:])
        item.append(data[3][2:])
        lis.append(item)
    print("数据解析完成")
    for li in lis:
        print(li)
    # write_csv(lis)
    write_xls(lis)

def write_csv(lis):
    headers = {'provience', 'city', 'thr','dim'}
    with open('../../tmp/全国城市经纬度表.csv', 'a+', encoding='utf-8', newline='')as fp:
        writer = csv.DictWriter(fp, headers)
        writer.writeheader()
        writer.writerows(lis)
    print("数据写入完成")

def write_xls(lis):
    f = xlwt.Workbook()
    sheet1 = f.add_sheet('city', cell_overwrite_ok=True)
    row = ['provience', 'city', 'thr', 'dim']
    for i in range(0, len(row)):
        sheet1.write(0, i, row[i])
    t = 1
    for li in lis:
        sheet1.write(t, 0, li[0])
        sheet1.write(t, 1, li[1])
        sheet1.write(t, 2, li[2])
        sheet1.write(t, 3, li[3])
        t += 1
    f.save('../../tmp/全国城市经纬度表.xls')
    print("写入数据完成")

def main():
    response = get_html()
    analy_html(response)


if __name__ == '__main__':
    main()
