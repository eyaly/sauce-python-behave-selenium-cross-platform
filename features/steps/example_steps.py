from behave import given, when, then

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

@given('I load the SauceDemo Web App')
def step_impl(context):
    print("I am in the given function ")
    context.driver.get("https://www.saucedemo.com/")
    # Useful when you are waiting for a specific page to load
    WebDriverWait(context.driver, 5).until(EC.title_contains("Swag Labs"))


@when('I login with a valid credential')
def step_impl(context):
    print("I am in the when function ")
    context.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    context.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    context.driver.find_element(By.CSS_SELECTOR,'.btn_action').click()

@then('I see the products page')
def step_impl(context):
    print("I am in the then function ")
    assert "/inventory.html" in context.driver.current_url