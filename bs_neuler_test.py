import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# BrowserStack configuration
BROWSERSTACK_USERNAME = os.environ.get("BROWSERSTACK_USERNAME", "USER")
BROWSERSTACK_ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY", "KEY")

with open('browserstack_credentials.txt', 'r') as f:
    lines = f.read().splitlines()
    BROWSERSTACK_USERNAME = lines[0].split('=')[1]
    BROWSERSTACK_ACCESS_KEY = lines[1].split('=')[1]

URL = f"https://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"

desired_cap = {
    'browserName': 'iPhone',
    'device': 'iPhone 15 Pro',
    'realMobile': 'true',
    'os_version': '17',
    'name': 'Neuler Hero Benchmark',
    'build': 'STRETCH+ Benchmarks'
}

options = Options()
for key, value in desired_cap.items():
    options.set_capability(key, value)

url = "https://neuler.jp"
driver = webdriver.Remote(command_executor=URL, options=options)

try:
    print(f"Loading {url}...")
    driver.get(url)
    
    # Wait for hero to render
    import time
    time.sleep(5)
    
    # Take screenshot
    screenshot_path = '/Users/ai_stretch/.gemini/antigravity/brain/5b227e4a-2e93-4b73-b436-af64a60dd58c/neuler_mobile.png'
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved to {screenshot_path}")
    
finally:
    driver.quit()
