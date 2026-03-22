import os
from selenium import webdriver
import time

USER = "chance.ai1234@gmail.com"
KEY = "b3FH73CfMgAazQnPrT14"
URL = f"https://{USER}:{KEY}@hub-cloud.browserstack.com/wd/hub"

desired_cap = {
    'browserName': 'iPhone',
    'device': 'iPhone 15 Pro',
    'realMobile': 'true',
    'os_version': '17',
    'name': 'Production Live Test',
    'build': 'Phase 48 Release'
}
options = webdriver.ChromeOptions()
for key, value in desired_cap.items():
    options.set_capability(key, value)
driver = webdriver.Remote(command_executor=URL, options=options)

try:
    print("Loading production root https://stretch-plus.co.jp/ ...")
    driver.get("https://stretch-plus.co.jp/")
    time.sleep(4)
    driver.save_screenshot('bs_live_production.png')
    print("Screenshot captured: bs_live_production.png")
finally:
    driver.quit()
    print("Done")
