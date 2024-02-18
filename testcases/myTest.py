
# pip install selenium==4.15.2
# pip install behave
# pip install Appium-Python-Client
import time
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


options = ChromeOptions()
options.browser_version = 'latest'
options.platform_name = 'Windows 11'
sauce_options = {}
sauce_options['username'] = os.environ["SAUCE_USERNAME"]
sauce_options['accessKey'] = os.environ["SAUCE_ACCESS_KEY"]
sauce_options['build'] = "My test Build 1"
sauce_options['name'] = "My test"
options.set_capability('sauce:options', sauce_options)

url = 'https://ondemand.eu-central-1.saucelabs.com/wd/hub'
# print("Desired Capabilities (dc): ", options)

driver = webdriver.Remote(command_executor=url, options=options)
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