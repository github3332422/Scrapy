import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
url = 'https://sou.zhaopin.com/?jl=489&sf=0&st=0&kw=Hadoop&kt=3'
driver.get(url)
button = driver.find_element_by_css_selector('body > div.a-modal.risk-warning > div > div > button')
button.click()
while True:
    time.sleep(2)
    next_bin = driver.find_element_by_css_selector('#pagination_content > div > button:nth-child(7)')
    if 'btn soupager__btn soupager__btn--disable' in next_bin.get_attribute('class'):
        print("亲，所有时间都获取完了哦")
        # self.write_csv()
        break
    else:
        next_bin.click()