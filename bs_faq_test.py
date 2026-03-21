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
    'name': 'FAQ Layout Test',
    'build': 'Phase 45 Hotfix'
}
options = webdriver.ChromeOptions()
for key, value in desired_cap.items():
    options.set_capability(key, value)
driver = webdriver.Remote(command_executor=URL, options=options)

try:
    print("Loading stretch-plus.co.jp/v2/ ...")
    driver.get("https://stretch-plus.co.jp/v2/")
    time.sleep(3)
    # scroll to FAQ section
    driver.execute_script("document.getElementById('faq').scrollIntoView();")
    time.sleep(2)
    # click the "予約" tab
    tabs = driver.find_elements_by_css_selector('.faq-tab')
    for tab in tabs:
        if "予約" in tab.text:
            tab.click()
            time.sleep(1)
            break
    # take screenshot
    driver.save_screenshot('bs_faq_layout_broken.png')
    print("Screenshot captured: bs_faq_layout_broken.png")
finally:
    driver.quit()
    print("Done")
