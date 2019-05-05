from lxml import etree
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

positions = []
driver = webdriver.Chrome()
def get_company_message(url):
    driver.get(url)
    response = etree.HTML(driver.page_source)
    positionName = response.xpath("//h3[@class='summary-plane__title']//text()")[0]
    salary = response.xpath("//span[@class='summary-plane__salary']//text()")[0]
    city = response.xpath("//ul[@class='summary-plane__info']//li/a//text()")[0]
    lis = response.xpath("//ul[@class='summary-plane__info']//li/text()")
    expersise = lis[0]
    education = lis[1]
    fuli = response.xpath("//div[@class='highlights__content']/span//text()")
    jineng = response.xpath("//div[@class='describtion__skills-content']/span//text()")
    contexts = response.xpath("//div[@class='describtion__detail-content']/p//text()")
    print(positionName, salary, city, expersise, education, fuli, jineng, contexts)

def get_position_link(url):
    print("程序开始执行")
    driver.get(url)
    html = etree.HTML(driver.page_source)
    print(driver.page_source)
    urls = html.xpath("//a[@class='contentpile__content__wrapper__item__info']/@href")
    print(urls)
    for url in urls:
        print(url)
        # get_company_message(url)

def get_url():
    base_url = 'https://sou.zhaopin.com/?p={}&jl=489&sf=0&st=0&kw=Hadoop&kt=3'
    for i in range(1,3):
        url = base_url.format(i)
        print(url)
        get_position_link(url)
        time.sleep(2)

def write_csv():
    pass

def main():
    get_url()

if __name__ == '__main__':
    main()