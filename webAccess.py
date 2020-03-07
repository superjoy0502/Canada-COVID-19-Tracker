# -*- coding:utf-8 -*-
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.options import Options  
# path = "/operadriver_linux64/operadriver"
chrome_options = Options()  
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("disable-infobars") 
chrome_options.add_argument("--disable-extensions") 
chrome_options.add_argument("--disable-gpu") 
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")  
chrome_options.binary_location = "/usr/bin/google-chrome"




def load():
    cases = []
    driver = webdriver.Chrome(executable_path="/chromedriver", options=chrome_options)
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6")
    first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR,
                                                           '#ember41 > div.widget-body.flex-fluid.full-width.flex-vertical.overflow-y-auto.overflow-x-hidden > nav')))
    contents = first_result.get_attribute("textContent")

    contents = contents.split('\n')
    while "" in contents:
        contents.remove("")
    while "        " in contents:
        contents.remove("        ")
    while '  ' in contents:
        contents.remove('  ')

    for n in range(0, len(contents)):
        res = any("Canada" in contents[n] for ele in contents)
        if res:
            place = contents[n].strip().replace(u'\xa0', u' ')[:-7]
            number = int(contents[n-1].strip()[:-10])
            t = {}
            t["place"] = place
            t["number"] = number
            cases.append(t)

    driver.quit()
    os.system('pkill "chrome"')
    return cases
