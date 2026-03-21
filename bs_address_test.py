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
    'name': 'Address Overflow Test on Info and Footer',
    'build': 'Phase 34 Mobile Adjustments'
}

print("Initialize BrowserStack connection...")
driver = webdriver.Remote(command_executor=URL, desired_capabilities=desired_cap)

try:
    print("Loading stretch-plus.co.jp/v2/ ...")
    driver.get("https://stretch-plus.co.jp/v2/")
    time.sleep(3) # Wait for initial rendering
    
    # 1. Scroll down to Info Section
    info_section = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "info"))
    )
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", info_section)
    time.sleep(2)
    driver.save_screenshot('bs_iphone_info_address.png')
    print("Screenshot captured: bs_iphone_info_address.png")
    
    # 2. Scroll to Footer
    footer_section = driver.find_element(By.ID, "footer")
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'end'});", footer_section)
    time.sleep(2)
    driver.save_screenshot('bs_iphone_footer_address.png')
    print("Screenshot captured: bs_iphone_footer_address.png")

finally:
    driver.quit()
    print("Done")
