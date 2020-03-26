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
    print("LOAD START")
    cases = []
    totalNumber = 0
    totalDeaths = 0
    totalCured = 0
    driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=chrome_options)
    wait = WebDriverWait(driver, 100)
    driver.get("https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6")
    confirmed_result = wait.until(presence_of_element_located((By.XPATH,
                                                           '//*[@id="ember41"]/div[2]/nav')))
    contents = confirmed_result.get_attribute("textContent")

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
            confirmedNumber = int(contents[n-1].strip()[:-10])
            t = {}
            deathn = deaths(place)
            curen = cured(place)
            t["place"] = place
            t["number"] = confirmedNumber
            t["deaths"] = deathn
            t["cured"] = curen
            time.sleep(2)
            totalNumber = totalNumber + confirmedNumber
            totalDeaths = totalDeaths + deathn
            totalCured = totalCured + curen
            cases.append(t)
    t = {}
    t["place"] = "Total Number"
    t["number"] = totalNumber
    t["deaths"] = totalDeaths
    t["cured"] = totalCured
    cases.insert(0, t)
    driver.quit()
    os.system('pkill "chrome"')
    print("DONE!")
    return cases


def deaths(place):
    deathNumber = 0
    driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=chrome_options)
    wait = WebDriverWait(driver, 100)
    driver.get("https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6")
    deaths_result = wait.until(presence_of_element_located((By.XPATH,
                                                           '//*[@id="ember91"]/div/nav')))
    time.sleep(2)
    contents = deaths_result.get_attribute("textContent")

    contents = contents.split('\n')
    while "" in contents:
        contents.remove("")
    while "        " in contents:
        contents.remove("        ")
    while "        " in contents:
        contents.remove("        ")
    while '  ' in contents:
        contents.remove('  ')
    while '                            ' in contents:
        contents.remove('                            ')
    while '  ' in contents:
        contents.remove('  ')
    while '    ' in contents:
        contents.remove('    ')
    
    for n in range(0, len(contents)):
        res = any(place in contents[n] for ele in contents)
        print(place + " in " + str(n) + " " + str(contents[n].strip().replace(u'\xa0', u' ')) + " " + str(place in contents[n].strip().replace(u'\xa0', u' ')))
        if res:
            deathNumber = int(contents[n-1].strip().replace(u'\xa0', u' ')[:-6])
    os.system('pkill "chrome"')
    return deathNumber

def cured(place):
    cureNumber = "No Data"
    driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=chrome_options)
    wait = WebDriverWait(driver, 100)
    driver.get("https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6")
    cured_result = wait.until(presence_of_element_located((By.XPATH,
                                                           '//*[@id="ember105"]/div/nav')))
    time.sleep(2)
    contents = cured_result.get_attribute("textContent")
    
    contents = contents.split('\n')

    while "" in contents:
        contents.remove("")

    while "        " in contents:
        contents.remove("        ")

    while "        " in contents:
        contents.remove("        ")

    while '  ' in contents:
        contents.remove('  ')

    while '                            ' in contents:
        contents.remove('                            ')

    while '  ' in contents:
        contents.remove('  ')

    while '    ' in contents:
        contents.remove('    ')
    for n in range(0, len(contents)):
        print(place + " in " + str(n) + " " + str(contents[n].strip().replace(u'\xa0', u' ')) + " " + str(place in contents[n].strip().replace(u'\xa0', u' ')))
        if place in contents[n].strip().replace(u'\xa0', u' '):
            cureNumber = 0
            cureNumber = int(contents[n-1].strip().replace(u'\xa0', u' ')[:-10])
    os.system('pkill "chrome"')
    return cureNumber
    
