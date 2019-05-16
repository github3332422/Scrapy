import xlwt
from lxml import etree

def write_xls(dict):
    f = xlwt.Workbook()
    sheet1 = f.add_sheet('city', cell_overwrite_ok=True)
    row = ['provience', 'city']
    for i in range(0, len(row)):
        sheet1.write(0, i, row[i])
    t = 1
    for d in dict:
        sheet1.write(t, 0, d['provience'])
        sheet1.write(t, 1, d['citys'])
        t += 1
    f.save('../../tmp/allcity.xls')
    print("写入数据完成")

def get_provience(response):
    provience = response.xpath("//div[@class='mw-parser-output']/h3//span[@class='mw-headline']//text()")
    return provience

def get_citys(response):
    citys = response.xpath("//div[@class='mw-parser-output']/ul")[2:-1]
    return citys

def get_message():
    f = open('../../data/all.txt',encoding='UTF-8').read()
    response = etree.HTML(f)
    return response

def main():
    response = get_message()
    citys = get_citys(response)
    provience = get_provience(response)
    dict = []
    for p,c in zip(provience,citys):
        item = {
            'provience': p,
            'citys': c.xpath("./li//a//text()")
        }
        dict.append(item)
    item = {
        'provience': "北京市",
        'citys': "北京"
    }
    dict.append(item)
    item = {
        'provience': "天津市",
        'citys': "天津"
    }
    dict.append(item)
    item = {
        'provience': "上海市",
        'citys': "上海"
    }
    dict.append(item)
    item = {
        'provience': "重庆市",
        'citys': "重庆"
    }
    dict.append(item)
    for d in dict:
        print(d)
    # write_xls(dict)
    # #测试能否查找成功
    s = "山"
    for d in dict:
        for x in d['citys']:
            if s in x:
                print(x,d['provience'])
                # break

if __name__ == '__main__':
    main()