import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver(request, wdwsize='--start-maximized'):
    options = chrome_options()
    options.add_argument(wdwsize)
    wd = webdriver.Chrome(options=options)
    wd.implicitly_wait(10)
    request.addfinalizer(wd.quit)
    return wd