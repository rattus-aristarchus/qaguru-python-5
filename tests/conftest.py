import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope="function")
def setup_browser():
    browser.config.driver = webdriver.Chrome()
    browser.config.base_url = 'https://demoqa.com'
