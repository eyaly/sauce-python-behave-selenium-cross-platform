# pip install Appium-Python-Client==3.1.0
# pip install selenium==4.15.2

import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from appium import webdriver
from appium.options.ios import XCUITestOptions

dc = {'platformName': 'iOS'}
dc['browserName'] = "safari"
dc['appium:automationName'] = 'XCUITest'
dc['appium:deviceName'] = "iPhone 15 Pro Max Simulator"
dc['appium:platformVersion'] = "17"
dc['sauce:options'] = {}
dc['sauce:options']['username'] = os.environ["SAUCE_USERNAME"]
dc['sauce:options']['accessKey'] = os.environ["SAUCE_ACCESS_KEY"]
dc['sauce:options']['build'] = "My test Build 1"
dc['sauce:options']['name'] = "My iOS Safari test"


url = 'https://ondemand.eu-central-1.saucelabs.com/wd/hub'
print("Desired Capabilities (dc): ", dc)
options = XCUITestOptions().load_capabilities(dc)
driver = webdriver.Remote(url, options=options)
driver.implicitly_wait(60)

try:
    driver.get("https://www.saucedemo.com/")
    # Useful when you are waiting for a specific page to load
    WebDriverWait(driver, 5).until(EC.title_contains("Swag Labs"))

    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.CSS_SELECTOR,'.btn_action').click()

    assert "/inventory.html" in driver.current_url

finally:
    driver.quit()