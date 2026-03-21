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
    'name': 'Hero Typography Test',
    'build': 'Phase 39 Hotfix'
}
options = webdriver.ChromeOptions()
for key, value in desired_cap.items():
    options.set_capability(key, value)
driver = webdriver.Remote(command_executor=URL, options=options)

try:
    print("Loading stretch-plus.co.jp/v2/ ...")
    driver.get("https://stretch-plus.co.jp/v2/")
    time.sleep(5)
    driver.save_screenshot('bs_hero_typo_final.png')
    print("Screenshot captured: bs_hero_typo_final.png")
finally:
    driver.quit()
    print("Done")
