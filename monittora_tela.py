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

    "VEICULOS EM VIAGEM CARREGADOS":
        "https://app.powerbi.com/groups/67ba6ab8-65f7-4eee-bccb-f1ad83efea92/reports/3b840a48-107c-456e-b836-e00f90d1693d/ReportSection?chromeless=True",
      
    "VEICULOS EM VIAGEM VAZIO":
        "https://app.powerbi.com/groups/67ba6ab8-65f7-4eee-bccb-f1ad83efea92/reports/0927ee70-4e1d-4ab8-aacd-4ca32792ced5/ReportSection?chromeless=True",
    
    "BASE 01":
        "https://app.powerbi.com/groups/67ba6ab8-65f7-4eee-bccb-f1ad83efea92/reports/b6c50271-3884-400e-a251-2d456b1c494a/ReportSection?chromeless=True",
  
    "BASE 02":
        "https://app.powerbi.com/groups/67ba6ab8-65f7-4eee-bccb-f1ad83efea92/reports/0b77fd45-b1cf-418b-a17f-9adba2dbda31/ReportSection?chromeless=True",
    
    "BASE CT":
        "https://app.powerbi.com/groups/67ba6ab8-65f7-4eee-bccb-f1ad83efea92/reports/be91a282-1e47-44d9-ba56-681e3769d2fb/ReportSection?chromeless=True",

    "BASE TRANSVALE":
        "https://app.powerbi.com/groups/67ba6ab8-65f7-4eee-bccb-f1ad83efea92/reports/0b7282a2-7362-47f6-aa77-b5b875e2b8d1/ReportSection?chromeless=True",
    
    "BASE INSERT":
        "https://app.powerbi.com/groups/67ba6ab8-65f7-4eee-bccb-f1ad83efea92/reports/d399cde9-2c32-44f5-a522-17ca563a7f86/ReportSection?chromeless=True",
  
    "BASE LEALES":
        "https://app.powerbi.com/groups/67ba6ab8-65f7-4eee-bccb-f1ad83efea92/reports/33e946c3-b560-4a71-ab3f-e1934aca9a6f/ReportSection?chromeless=True",

    "ALTO RISCO":
        "https://app.powerbi.com/groups/67ba6ab8-65f7-4eee-bccb-f1ad83efea92/reports/6da17e20-100d-4cf8-89cd-3b3d0044b238?chromeless=True",
        
    "MÉDIO RISCO":
        "https://app.powerbi.com/groups/67ba6ab8-65f7-4eee-bccb-f1ad83efea92/reports/b2d6efcb-87f8-4dfa-a6d7-0e5b693bd9a7/ReportSection?chromeless=True",

    "BAIXO RISCO":
        "https://app.powerbi.com/groups/67ba6ab8-65f7-4eee-bccb-f1ad83efea92/reports/51424b7a-ca8e-4b52-8ce3-aafce32558b8/ReportSection?chromeless=True"

    }

while True: 
    for key, value in url.items():
        driver.get(value)
        print(key)
        time.sleep(timer)