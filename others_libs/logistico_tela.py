from importlib.resources import path
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
    
     "GESTÃO DE COLETAS E ENTREGAS":
        "https://app.powerbi.com/groups/fe29f95a-80e2-431d-8054-bb8febce5298/reports/78541a58-9172-4834-bd3c-680677b31fb4/ReportSection?chromeless=True",
    
    "GESTÃO DE FROTA":
        "https://app.powerbi.com/groups/fe29f95a-80e2-431d-8054-bb8febce5298/reports/9af87f9b-efeb-4313-9374-473049fb2a3d/ReportSection?chromeless=True",
    
    "GESTÃO DE LEADTIME":
        "https://app.powerbi.com/groups/fe29f95a-80e2-431d-8054-bb8febce5298/reports/3d96ac3f-6ec9-4db7-9194-91083cdee1b5/ReportSection?chromeless=True",
     
    "GESTÃO DE PARADAS":
        "https://app.powerbi.com/groups/fe29f95a-80e2-431d-8054-bb8febce5298/reports/f70c3114-b75c-4f55-8bc2-6a902b0ead21/ReportSection?chromeless=True",
    
    "GESTÃO DE RASTREADORES":
        "https://app.powerbi.com/groups/fe29f95a-80e2-431d-8054-bb8febce5298/reports/fc145d66-a4fd-442b-b0cd-789fd8df3056?chromeless=True"

    }


while True: 
    for key, value in url.items():
        driver.get(value)
        print(key)
        time.sleep(timer)
        print(local)