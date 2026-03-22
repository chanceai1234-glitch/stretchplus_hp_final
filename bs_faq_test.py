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
    'name': 'FAQ Layout Test 2',
    'build': 'Phase 46 Hotfix'
}
options = webdriver.ChromeOptions()
for key, value in desired_cap.items():
    options.set_capability(key, value)
driver = webdriver.Remote(command_executor=URL, options=options)

from selenium.webdriver.common.by import By

try:
    print("Loading stretch-plus.co.jp/v2/ ...")
    driver.get("https://stretch-plus.co.jp/v2/")
    time.sleep(3)
    driver.execute_script("document.getElementById('faq').scrollIntoView();")
    time.sleep(2)
    # click the "予約" tab
    tabs = driver.find_elements(By.CSS_SELECTOR, '.faq-tab')
    for tab in tabs:
        if "予約" in tab.text:
            tab.click()
            time.sleep(1)
            break
    driver.save_screenshot('bs_faq_layout_fixed.png')
    print("Screenshot captured: bs_faq_layout_fixed.png")
finally:
    driver.quit()
    print("Done")
