import pytest
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

"""
    Получаем webelement посредством выполнения JavaScript методами:
    1) document.querySelectorAll("<css-selector>") - возвращает список
    2) document.getElementById(<"ID>") - возвращает вебэлемент
    3) document.getElementsByClassName("<ClassName>") - возвращает список
"""
def test_example(driver):
    c = chrome_options.arguments
    print(c)
    wait = WebDriverWait(driver, 15)
    url = "https://webdriver.ru/"
    driver.get(url)
    elem1 = driver.find_element(By.CSS_SELECTOR, 'ul.right')
    wait.until(EC.element_to_be_clickable(elem1))
    elem1.click()
    doc1 = driver.execute_script("return document.querySelectorAll('input.ais-search-box--input')")
    doc1[0].send_keys('webdriver\n')
    time.sleep(10)
    elem2 = driver.find_element(By.CSS_SELECTOR, "ul.left li:nth-of-type(9) a")
    wait.until(EC.element_to_be_clickable(elem2))
    elem2.click()
    cur_win_id = driver.current_window_handle
    list_win_ids = driver.window_handles
    for index in list_win_ids:
        if cur_win_id not in list_win_ids:
            driver.switch_to.window(index)
    time.sleep(5)
    # wait.until(EC.title_is("Selenium - Functional Testing - Форум тестировщиков"))


# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

# wait = WebDriverWait(driver, 10) # seconds
# driver.refresh()
# wait.until(EC.staleness_of(element))
