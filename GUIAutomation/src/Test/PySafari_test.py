'''
Created on Sep 22, 2018

@author: admin
'''
import selenium
import time
from selenium import webdriver

def test_SABrowser():
    
    browser = webdriver.Safari()
    time.sleep(10)
    browser.get('http://www.baidu.com')
    time.sleep(10)
    browser.get('http://www.sohu.com')
    time.sleep(10)
    browser.get('http://192.168.1.11:8686/view/PythonAT/job/MyFirstPyProject/ws/tiger/log.html')
    time.sleep(10)
    browser.close()
#test_SABrowser()