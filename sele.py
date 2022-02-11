# -*- coding: utf-8 -*-
"""
Uwsing M_edge
Version 91.0.864.67 (Version officielle) (64 bits)
"""
#christophe utilise chrome:
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
# # driver.maximize_window()
# driver.get('http://51.195.220.149/book.php?id=3')

import os ,time
from re import T
from msedge.selenium_tools import Edge, EdgeOptions

options = EdgeOptions()
options.use_chromium = True

data_path = os.path.join(os.getcwd(),'books_folder')
prefs = {"download.default_directory" :data_path}
options.add_experimental_option("prefs",prefs)

driver  = Edge(options = options)

def test_sele():
    driver.get('https://www.browserstack.com/test-on-the-right-mobile-devices');
    downloadcsv= driver.find_element_by_css_selector('.icon-csv');
    gotit= driver.find_element_by_id('accept-cookie-notification');
    gotit.click();    
    downloadcsv.click();
    time.sleep(5)
    driver.close()

# driver.get('http://51.195.220.149/book.php?id=3')

# print("---- lala ----", "\n Work in progress...")
# target = driver.find_element_by_css_selector('a[download=""]')
# target.click()

def scrap_one(id:int, sleep=True):
    print(f'\n --- Scraping book with id = {id} ---')
    driver.get(f'http://51.195.220.149/book.php?id={id}')
    target = driver.find_element_by_css_selector('a[download=""]')
    target.click()
    if sleep:
        time.sleep(5)


for i in range(5):
    print("---- lala ----", "\n Work in progress...")
    scrap_one(i+1,sleep=True )

driver.close()





# for i in range(1165):
#     print("---- lala ----", "\n Work in progress...")

