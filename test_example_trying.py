import pytest
# import time
from selenium import webdriver
# from webdriver.common.alert import alert
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options as chrome_options
# from selenium.webdriver.support import expected_conditions as EC


# @pytest.fixture
# def driver(request):
#     wd = webdriver.Chrome(options=options)
#     request.addfinalizer(wd.quit)
#     return wd


def driver(request):
    wd = webdriver.Chrome(options=options)
    request.addfinalizer(wd.quit)
    return wd


@driver
def options():
    options = chrome_options()
    options.add_argument('--start-maximized')
    capabilities = {'unexpectedAlertBehaviour': 'dismiss', 'pageLoadStrategy': 'normal'}
    return options


@pytest.fixture
def test_example(driver):
    url = "http://mail.ru/"
    driver.get(url)
    main_window = driver.window_handles
    print(main_window)
    return len(driver.find_elements(By.CSS_SELECTOR, 'ul.right')) > 0


