import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope="function")
def setup_browser():
    browser.config.driver = webdriver.Chrome()
    browser.config.window_width = 1600
    browser.config.window_height = 1200
    browser.config.base_url = 'https://demoqa.com'

    yield

    browser.quit()