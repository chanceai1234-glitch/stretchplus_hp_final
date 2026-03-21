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
    'name': 'Address Line Breaks Test',
    'build': 'Phase 38 Hotfix'
}
options = webdriver.ChromeOptions()
for key, value in desired_cap.items():
    options.set_capability(key, value)
driver = webdriver.Remote(command_executor=URL, options=options)

try:
    print("Loading stretch-plus.co.jp/v2/ ...")
    driver.get("https://stretch-plus.co.jp/v2/")
    time.sleep(4)
    
    # Scroll to Info section
    info = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "info"))
    )
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'start'});", info)
    time.sleep(3)
    driver.save_screenshot('bs_address_final_info.png')
    
    # Scroll to Footer section
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    driver.save_screenshot('bs_address_final_footer.png')
    
    print("Screenshots captured.")
finally:
    driver.quit()
    print("Done")
