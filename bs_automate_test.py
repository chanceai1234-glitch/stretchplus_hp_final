from selenium import webdriver
import sys
import time

BROWSERSTACK_USERNAME = "chance.ai1234@gmail.com"
BROWSERSTACK_ACCESS_KEY = "b3FH73CfMgAazQnPrT14"
URL = f"https://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"

bstack_options = {
    "osVersion" : "17",
    "deviceName" : "iPhone 15 Pro",
    "realMobile" : "true",
    "projectName" : "StretchPlus",
    "buildName" : "Mobile_Testing",
    "sessionName" : "iPhone 15 Pro text",
    "local" : "false",
}

options = webdriver.safari.options.Options()
options.set_capability('bstack:options', bstack_options)
options.set_capability('browserName', 'safari')

try:
    print("Connecting to BrowserStack Hub...")
    driver = webdriver.Remote(command_executor=URL, options=options)
    
    print("Navigating to https://stretch-plus.co.jp/v2/ ...")
    driver.get("https://stretch-plus.co.jp/v2/")
    
    print("Waiting for page load...")
    time.sleep(5)
    
    save_path = "/Users/ai_stretch/.gemini/antigravity/brain/5b227e4a-2e93-4b73-b436-af64a60dd58c/bs_iphone15_pro.png"
    driver.save_screenshot(save_path)
    print(f"✅ Screenshot saved to {save_path}")
    
    driver.quit()
except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)
