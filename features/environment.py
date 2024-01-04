
# pip install selenium==4.15.2
# pip install behave
import time
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException



def before_scenario(context, scenario):
    # Code to run before each scenario
    print("I am in the before function ")
    options = ChromeOptions()
    options.browser_version = 'latest'
    options.platform_name = 'Windows 11'
    sauce_options = {}
    sauce_options['username'] = os.environ["SAUCE_USERNAME"]
    sauce_options['accessKey'] = os.environ["SAUCE_ACCESS_KEY"]
    sauce_options['build'] = "My test Build 1"
    sauce_options['name'] = scenario.name
    options.set_capability('sauce:options', sauce_options)

    url = 'https://ondemand.eu-central-1.saucelabs.com/wd/hub'
    # print("Desired Capabilities (dc): ", options)

    context.driver = webdriver.Remote(command_executor=url, options=options)
    context.driver.implicitly_wait(60)

def after_scenario(context, scenario):
    try:
        # Execute the script to set the job result in Sauce Labs
        status = 'passed' if scenario.status == 'passed' else 'failed'
        context.driver.execute_script(f"sauce:job-result={status}")

    finally:
        print("Sauce - release driver")
        context.driver.quit()
