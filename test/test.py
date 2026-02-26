import pytest
from selenium import webdriver
from selene import browser

@pytest.fixture(scope="session", autouse=True)
def browser_management():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    browser.config.driver = driver
    yield driver
    browser.config.driver = driver
    browser.config.timeout = 10

    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield


    browser.quit()
