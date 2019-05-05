# -*- coding:utf-8 -*-
__author__ = 'GaoShuai'

from selenium import webdriver
from scrapy.selector import Selector
import time
import json


def login_lagou():
    browser = webdriver.Chrome()
    browser.get("https://passport.lagou.com/login/login.html")
    # 填充账号密码
    browser.find_element_by_css_selector(
        "body > section > div.left_area.fl > div.form-content > div:nth-child(2) > form > div:nth-child(1) > input") \
        .send_keys("18814664090")
    browser \
        .find_element_by_css_selector(
        "body > section > div.left_area.fl > div.form-content > div:nth-child(2) > form > div:nth-child(2) > input") \
        .send_keys("zhangqing")

    # 点击登陆按钮
    browser \
        .find_element_by_css_selector(
        "body > section > div.left_area.fl > div.form-content > div:nth-child(2) > form > div.input_item.btn_group.clearfix.sense_login_password > input") \
        .click()
    cookie_dict = {}
    time.sleep(10)
    Cookies = browser.get_cookies()
    for cookie in Cookies:
        cookie_dict[cookie['name']] = cookie['value']
    # browser.quit()

    data =  cookie_dict
    jsObj = json.dumps(data)

    fileObject = open('cookies.json', 'w')
    fileObject.write(jsObj)
    fileObject.close()


def login_zhihu():
    browser = webdriver.Chrome()
    browser.get("https://www.zhihu.com/signup?next=%2F")
    # 填充账号密码
    browser \
        .find_element_by_css_selector(
        ".SignFlow-accountInput.Input-wrapper input") \
        .send_keys("18814664090")
    browser \
        .find_element_by_css_selector(
        ".SignFlow-passwordInput.Input-wrapper input") \
        .send_keys("zhangqing")

    # 点击登陆按钮
    browser.find_element_by_css_selector(
        "#root > div > main > div > div > div > div.SignContainer-inner > div.Login-content > form > button") \
        .click()
    cookie_dict = {}
    time.sleep(3)
    Cookies = browser.get_cookies()
    for cookie in Cookies:
        cookie_dict[cookie['name']] = cookie['value']
    # browser.quit()

    return cookie_dict


if __name__ == "__main__":
    login_lagou()
    print('获取cookies成功')
    # print(login_zhihu())