# -*- coding: utf-8 -*-
"""
Uwsing M_edge
Version 91.0.864.67 (Version officielle) (64 bits)
"""
import os ,time
from msedge.selenium_tools import Edge, EdgeOptions
from dotenv import load_dotenv

load_dotenv()

url = os.getenv('URL')
print(url)

# christophe utilise chrome:
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
# # driver.maximize_window()
# driver.get(url+'/book.php?id=3')


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


def scrap_one(id:int, sleep=True):
    print(f'\n --- Scraping book with id = {id} ---')
    driver.get(url + f'/book.php?id={id}')
    target = driver.find_element_by_css_selector('a[download=""]')
    target.click()
    if sleep:
        time.sleep(3)



#stoped at i = 614 server crash or it belives it's a dos attack rerun with range(614,1165)

for i in range(1165):
    print("---- lala ----", "\n Work in progress...")
    scrap_one(i+1,sleep=True)

# time.sleep(600)
# driver.close()

