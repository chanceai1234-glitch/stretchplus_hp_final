import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

USER = "chance.ai1234@gmail.com"
KEY = "b3FH73CfMgAazQnPrT14"
URL = f"https://{USER}:{KEY}@hub-cloud.browserstack.com/wd/hub"

desired_cap = {
    'browserName': 'iPhone',
    'device': 'iPhone 15 Pro',
    'realMobile': 'true',
    'os_version': '17',
    'name': 'Hamburger Menu Restoration Test',
    'build': 'Phase 35 Hotfix'
}

print("Initialize BrowserStack connection...")
options = webdriver.ChromeOptions()
for key, value in desired_cap.items():
    options.set_capability(key, value)
driver = webdriver.Remote(command_executor=URL, options=options)

try:
    print("Loading stretch-plus.co.jp/v2/ ...")
    driver.get("https://stretch-plus.co.jp/v2/")
    time.sleep(4) # Wait for initial rendering
    
    # Take screenshot before click
    driver.save_screenshot('bs_hamburger_closed.png')
    print("Screenshot captured: bs_hamburger_closed.png")
    
    # 1. Click Hamburger
    hamburger = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "hamburger-btn"))
    )
    hamburger.click()
    print("Clicked hamburger.")
    
    time.sleep(2) # wait for CSS transition (0.4s)
    
    driver.save_screenshot('bs_hamburger_open.png')
    print("Screenshot captured: bs_hamburger_open.png")

finally:
    driver.quit()
    print("Done")
