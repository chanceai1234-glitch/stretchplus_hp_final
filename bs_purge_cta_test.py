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
    'name': 'Purge CTA Banners Test',
    'build': 'Phase 37 Hotfix'
}
options = webdriver.ChromeOptions()
for key, value in desired_cap.items():
    options.set_capability(key, value)
driver = webdriver.Remote(command_executor=URL, options=options)

try:
    print("Loading stretch-plus.co.jp/v2/ ...")
    driver.get("https://stretch-plus.co.jp/v2/")
    time.sleep(4)
    
    # Scroll to Worries section to see the transition
    worries = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "worries"))
    )
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'end'});", worries)
    time.sleep(2)
    driver.save_screenshot('bs_purged_cta_worries_to_reviews.png')
    
    # Scroll to Menu section to see the transition
    menu = driver.find_element(By.ID, "menu")
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'end'});", menu)
    time.sleep(2)
    driver.save_screenshot('bs_purged_cta_menu_to_flow.png')
    
    print("Screenshots captured.")
finally:
    driver.quit()
    print("Done")
