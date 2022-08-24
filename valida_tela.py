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
    
    "GestaoCadadastroConsulta":
        "https://app.powerbi.com/groups/fe29f95a-80e2-431d-8054-bb8febce5298/reports/661af3a0-4f81-4334-93c5-5d1e65f7d089/ReportSection46ac17ba842ce96ffa8c?chromeless=True" ,
    
    "OperacionalValida":
        "https://app.powerbi.com/groups/35336e6c-ae7b-456f-b382-d557def8fa6e/reports/5d5f1cef-915a-4c16-8113-8ae2fb2a0daf/ReportSection0190d74fa1e41ab7098b?chromeless=True",
    
    "ValidaSLA":
        "https://portal.vertticegr.com.br/dashboard/sla/valida"
    
    }


while True: 
    for key, value in url.items():
        driver.get(value)
        print(key)
        time.sleep(timer)