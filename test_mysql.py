
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options


# @pytest.fixture(scope='function')
# def driver(request):
#     options = chrome_options()
#     options.add_argument('--start-maximixed')
#     driver = webdriver.Chrome(options=options)
#     yield driver
#     driver.quit()


# Мой вариант
@pytest.fixture(scope='function')
def driver(request, wdwsize='--start-maximized'):
    options = chrome_options()
    options.add_argument(wdwsize)
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    request.addfinalizer(driver.quit)
    return driver

def test_example(driver):
    pass
