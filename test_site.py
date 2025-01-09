import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicity_wait(3)
    yield browser
    browser.close()

def test_open_s6():
    browser.get("https://demoblaze.com/index.html")
    galaxy_s6 = browser.find_element(By.LINK_TEXT, value = 'Samsung galaxy s6')
    galaxy_s6.click()
    title = browser.find_element(By.CSS_SELECTOR, value = 'h2')
    assert title.text == 'Samsung galaxy s6'