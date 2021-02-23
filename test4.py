# coding=utf-8
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("腾讯")
driver.find_element_by_id("su").click()
driver.quit()