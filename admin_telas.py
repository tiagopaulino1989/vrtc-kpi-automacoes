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
timer = 50

# URLS CONFIG FOR ROTATE TABS
url = {
    
    "Comparativo de Uso - Monittora": 
    "https://app.powerbi.com/groups/35336e6c-ae7b-456f-b382-d557def8fa6e/reports/29a6a265-0368-4bdb-ae9e-e86af3da47cb?chromeless=True",

    "Comparativo de Uso - Valida": 
    "https://app.powerbi.com/groups/35336e6c-ae7b-456f-b382-d557def8fa6e/reports/29a6a265-0368-4bdb-ae9e-e86af3da47cb/ReportSectionbf046b7d50740a01b3d6?chromeless=True",

    "Comparativo de Uso - Novos Clientes":
    "https://app.powerbi.com/groups/35336e6c-ae7b-456f-b382-d557def8fa6e/reports/29a6a265-0368-4bdb-ae9e-e86af3da47cb/ReportSectionb0cfdc025e90ed8f547b?chromeless=True"

    }


while True: 
    for key, value in url.items():
        driver.get(value)
        print(key)
        time.sleep(timer)
    time.sleep(5)
