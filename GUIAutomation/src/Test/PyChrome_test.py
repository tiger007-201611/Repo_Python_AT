'''
Created on Sep 22, 2018

@author: admin
'''
import selenium
import time
from selenium import webdriver

def test_CHBrowser():
    
    browser = webdriver.Chrome('/Users/admin/Automation/GitHub/Repo_Python_AT/GUIAutomation/webdriver/Chrome/chromedriver_mac64_v2.41_CH67-69')
    time.sleep(10)
    browser.get('http://www.baidu.com')
    time.sleep(10)
    browser.get('http://www.sohu.com')
    time.sleep(10)
    browser.close()
    
#test_CHBrowser()