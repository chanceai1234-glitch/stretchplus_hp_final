import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# BrowserStack configuration
USER = "chance.ai1234@gmail.com"
KEY = "b3FH73CfMgAazQnPrT14"
URL = f"https://{USER}:{KEY}@hub-cloud.browserstack.com/wd/hub"

desired_cap = {
    'browserName': 'iPhone',
    'device': 'iPhone 15 Pro',
    'realMobile': 'true',
    'os_version': '17',
    'name': 'Anchor Offset Test',
    'build': 'STRETCH+ Benchmarks'
}

options = Options()
for key, value in desired_cap.items():
    options.set_capability(key, value)

driver = webdriver.Remote(command_executor=URL, options=options)

try:
    print("Loading stretch-plus.co.jp/v2/ ...")
    driver.get("https://stretch-plus.co.jp/v2/")
    time.sleep(3)
    
    # Click Hamburger Menu
    print("Clicking hamburger menu...")
    hamburger = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".hamburger-btn"))
    )
    hamburger.click()
    time.sleep(1.5)
    
    # Click 'ご利用の流れ' link
    print("Clicking anchor link for #flow...")
    flow_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#header-nav a[href='#flow']"))
    )
    flow_link.click()
    
    # Wait for scroll to stop
    print("Waiting for smooth scroll...")
    time.sleep(3)
    
    # Capture Screenshot
    screenshot_path = '/Users/ai_stretch/.gemini/antigravity/brain/5b227e4a-2e93-4b73-b436-af64a60dd58c/bs_iphone_anchor_offset.png'
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved to {screenshot_path}")

finally:
    driver.quit()
