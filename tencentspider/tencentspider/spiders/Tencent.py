import requests
import time
from lxml import etree
from selenium import webdriver
import csv

# item = []

driver = webdriver.Chrome()
def get_message(url):
    driver.get(url)
    html = etree.HTML(driver.page_source)
    # print(driver.page_source)
    # items = []
    trs = html.xpath("//table[@class='tablelist']//tr")[1:-1]
    for tr in trs:
        # print(tr)
        positionName = tr.xpath("./td[1]/a/text()")
        if len(positionName) > 0:
            positionName = positionName[0]
        else:
            positionName = " "
        positionType = tr.xpath("./td[2]//text()")
        if len(positionType) > 0:
            positionType = positionType[0]
        else:
            positionType = " "
        positionNum = tr.xpath("./td[3]//text()")
        if len(positionNum) > 0:
            positionNum = positionNum[0]
        else:
            positionNum = " "
        print(positionName,positionType,positionNum)
        # item = TencentspiderItem()
        # item = {
        #     'name':positionName,
        #     'type':positionType,
        #     'number':positionNum
        # }
        item = []
        item.append(positionName)
        item.append(positionType)
        item.append(positionNum)
        write_csv(item)
    # return items

def write_csv(message):
    # headers = {'name', 'type','number'}
    with open('tencent1.csv', 'a+', encoding='UTF-8', newline='')as fp:
        writer = csv.writer(fp)
        writer.writerow(message)

def main():
    for i in range(0,313):#313
        url = 'https://hr.tencent.com/position.php?&start={}'.format(i*10)
        print(url)
        get_message(url)
        time.sleep(1.5)

if __name__ == '__main__':
    main()
