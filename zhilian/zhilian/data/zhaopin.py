import csv

import time
from lxml import etree
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Spider(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
        self.positions = []

    def run(self):
        self.driver.get(self.url)
        count = 1
        while True:
            print('获取第', count, '页')
            source = self.driver.page_source
            self.parse_list_page(source)
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#s_position_list > div.item_con_pager > div > span.pager_next'))
            )
            next_bin = self.driver.find_element_by_css_selector('#s_position_list > div.item_con_pager > div > span.pager_next')
            if 'pager_next pager_next_disabled' in next_bin.get_attribute('class'):
                print("亲，所有时间都获取完了哦")
                self.write_csv()
                break
            else:
                count += 1
                next_bin.click()


    def parse_list_page(self,source):
        html = etree.HTML(source)
        links = html.xpath("//a[@class='position_link']/@href")
        # print(len(links))
        for link in links:
            self.request_detail_page(link)

    def request_detail_page(self,url):
        # self.driver.get(url)
        time.sleep(1)
        self.driver.execute_script("window.open('%s')"%url)
        self.driver.switch_to.window(self.driver.window_handles[1])
        source = self.driver.page_source
        #等待页面加载
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH,"//span[@class='name']"))
        )
        self.parse_detail_page(source)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def parse_detail_page(self,source):
		html = etree.HTML(source)
		position_name = html.xpath("//span[@class='name']/text()")[0]
		job_requests_spans = html.xpath("//dd[@class='job_request']//span")
		salary = job_requests_spans[0].xpath('.//text()')[0].strip()
		city = job_requests_spans[1].xpath('.//text()')[0].strip()
		city = re.sub(r"[\s/]", "", city)
		work_year = job_requests_spans[2].xpath('.//text()')[0].strip()
		work_year = re.sub(r"[\s/]", "", work_year)
		education = job_requests_spans[3].xpath('.//text()')[0].strip()
		education = re.sub(r"[\s/]", "", education)
		work_nature = job_requests_spans[4].xpath('.//text()')[0].strip()
		job_detail = "".join(html.xpath("//dd[@class='job-advantage']//text()")).strip()
		job_detail = job_detail.replace('\n', '')
		job_detail = job_detail.replace(' ', '')
		# pattern = re.compile('.*? class="b2" .*? alt="(.*?)">',re.S)
		# company = re.findall(pattern,html)[0]
		company = "".join(html.xpath("//h2[@class='fl']//text()"))
		company = company.replace('\n', '')
		company = company.replace(' ', '')[0:-6]
		# pattern = re.compile('[\u4E00-\u9FA5]+', re.S)
		# company = re.findall(pattern, company)[0]
		# print(position_name,salary,city,work_year,education)
		release_time = html.xpath("//p[@class='publish_time']//text()")

		zhiwei = str(html.xpath("//div[@class='job-detail']//text()"))
		zhiwei = zhiwei.replace('\\n', '')
		zhiwei = zhiwei.replace(' ', '')
		zhiwei = zhiwei.replace("'',", '')
		zhiwei = str(zhiwei)
		index = zhiwei.index("岗位要求：")
		duties = zhiwei[0:index]
		claim = zhiwei[index:-1]


		position = {
			'position_name':position_name,
			'company':company,
			'salary':salary,
			'city':city,
			'work_year':work_year,
			'education':education,
			'job_detail':job_detail[5:],
			'release_time':release_time[0:-6],
			'work_nature':work_nature,
			'duties':duties,
			'claim':claim
		}
        self.positions.append(position)

    def write_csv(self):
        headers = {'position_name', 'company', 'salary', 'city', 'work_year', 'education', 'job_detail'}
        with open('demo1.csv', 'w', encoding='utf-8', newline='')as fp:
            writer = csv.DictWriter(fp, headers)
            writer.writeheader()
            writer.writerows(self.positions)

if __name__ == '__main__':
    spider = Spider()
    spider.run()