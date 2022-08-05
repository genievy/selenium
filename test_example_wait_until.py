import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as chrome_options


# Создаем объект 'chrome_options', в который добавляются аргументы
@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')  # Use headless' if you don't need a browser UI
    options.add_argument('--start-maximized')
    # options.add_argument('--windows-size=800,600')
    return options


@pytest.fixture
def driver(request, get_chrome_options):
    options = get_chrome_options
    wd = webdriver.Chrome(options=options)  # If chromedriver is in the PATH, it's default
    wd.implicitly_wait(10)  # Таймаут на отображение (не явного типа) элемента
    request.addfinalizer(wd.quit)
    return wd


# Ожидание (явного типа) отображения элемента
def test_example(driver):
    driver.get("https://www.advanced-ip-scanner.com/ru/")
    WebDriverWait(driver, 30).until(lambda x: driver.find_element(By.CSS_SELECTOR, 'img.screenshot_main.img_responsive'))