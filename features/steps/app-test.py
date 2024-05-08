from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

url = 'https://todo-react-q5jffr7s6-v4ljoks-projects.vercel.app/'

@given('Users launch chrome browser')
def step_impl(context):

    options = webdriver.ChromeOptions()
    context.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

@when('Users open form webpage')
def step_impl(context):
    
    context.driver.get(url)
    time.sleep(5)

@then('Users add item')
def step_impl(context):
    
    add_item_textbox = context.driver.find_element(By.XPATH, '//input[contains(@placeholder, "What needs to be done")]')
    add_item_textbox.send_keys('Task')

    add_item_button = context.driver.find_elements(By.CLASS_NAME, "btn-outline-secondary")

    add_item_button[2].click()

    time.sleep(1)

@then('Users highlight item')
def step_impl(context):
    highlight_item = context.driver.find_element(By.CLASS_NAME, "btn-outline-success")
    highlight_item.click()

    time.sleep(1)

@then('Users mark item as done')
def step_impl(context):
    mark_item = context.driver.find_element(By.XPATH, '//*[contains(text(), "Have a lunch")]')
    mark_item.click()

    time.sleep(1)

@then('Users delete item')
def step_impl(context):
    delete_item = context.driver.find_elements(By.CLASS_NAME, "btn-outline-danger")
    delete_item[1].click()

    time.sleep(1)

@then('Users filter active items')
def step_impl(context):
    active_item = context.driver.find_element(By.XPATH, '//*[contains(text(), "Active")]')
    active_item.click()

    time.sleep(1)

@then('Users filter done items')
def step_impl(context):
    done_item = context.driver.find_element(By.XPATH, '//*[contains(text(), "Done")]')
    done_item.click()

    time.sleep(1)

@then('Users view all tasks')
def step_impl(context):
    done_item = context.driver.find_element(By.XPATH, '//*[contains(text(), "All")]')
    done_item.click()

    time.sleep(1)