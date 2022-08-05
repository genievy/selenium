import pytest
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    options = chrome_options()
    options.add_argument('--start-maximized')
    wd = webdriver.Chrome(options=options)
    wd.implicitly_wait(10)
    request.addfinalizer(wd.quit)
    return wd

def test_example_litecart(driver):
    wait = WebDriverWait(driver, 15)
    url = "http://localhost/litecart/"
    driver.get(url)
    # print(driver.page_source)  # выводит исходный HTML – код всей страницы
    l_ccks = driver.get_cookies()
    print(l_ccks)
    time.sleep(10)
