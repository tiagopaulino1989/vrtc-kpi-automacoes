from lib2to3.pgen2 import driver
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time
import os

#SETTING UP THE ENV CONFIG FOR DRIVERS
local = "C:\BrowserDrivers\geckodriver.exe"

# OPENING SESSION IN CHROME OR FIREFOX
# driver = webdriver.Chrome(executable_path=executable_path=local+r"\chromedriver.exe") #CHROME

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.cache.disk.enable", False)
profile.set_preference("browser.cache.memory.enable", False)
profile.set_preference("browser.cache.offline.enable", False)
profile.set_preference("network.http.use-cache", False) 

driver = webdriver.Firefox(executable_path=local, firefox_profile=profile) #FIREFOX

# SETTING DEFAULT TIME CONFIG
timer = 45

# URLS CONFIG FOR ROTATE TABS
url = {
    
    "PreViagem":
        "https://app.powerbi.com/groups/67ba6ab8-65f7-4eee-bccb-f1ad83efea92/reports/c2d8e9e2-33b7-4915-a99d-2680a4ca8910?chromeless=True",

    "GestaoChecklist":
        "https://app.powerbi.com/groups/67ba6ab8-65f7-4eee-bccb-f1ad83efea92/reports/8a54e054-d7a7-4f98-b8a9-8172adbf923c?chromeless=True" ,
        
    "GridChecklist":
        "https://app.powerbi.com/groups/67ba6ab8-65f7-4eee-bccb-f1ad83efea92/reports/ea79cd38-a833-4713-a9a2-c2e0368387ca?chromeless=True"
    }


while True: 
    for key, value in url.items():
        driver.get(value)
        print(key)
        time.sleep(timer)