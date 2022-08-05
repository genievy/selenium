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
    wd.implicitly_wait(10)  # Устанавливаем таймаут на отображение элемента на странице
    request.addfinalizer(wd.quit)
    return wd


# # Вариант использования с созданием объекта options внутри функции
# @pytest.fixture
# def driver(request):
#     options = chrome_options()
#     options.add_argument('--start-maximized')
#     wd = webdriver.Chrome(options=options)
#     wd.implicitly_wait(10)  # Устанавливаем таймаут на отображение элемента на странице
#     request.addfinalizer(wd.quit)
#     return wd

# # Посмотреть capabilities
# @pytest.fixture
# def driver(request):
#     wd = webdriver.Chrome(desired_capabilities = {'platformName' : 'windows'})  # wd = webdriver.Firefox()
#     print(wd.capabilities)  # Выводим на печать все актуальные астройки браузера
#     wd.implicitly_wait(10)  # Устанавливаем таймаут на отображение элемента на странице
#     request.addfinalizer(wd.quit)
#     return wd


# def test_example(driver):
#     driver.get("http://www.google.com/")
#     driver.find_element(By.NAME, "q").send_keys("webdriver")
#     driver.find_element(By.NAME, "btnK").click()
#     WebDriverWait(driver, 30).until(EC.title_is("webdriver - Поиск в Google"))


# # Поиск элемента с использ-м сложного локатора
# def test_example(driver):
#     driver.get("https://www.advanced-ip-scanner.com/ru/download/")
#     # driver.find_element(By.CSS_SELECTOR, "a.button-blue.download_link li:last-child").click()
#     # driver.find_element(By.CSS_SELECTOR, "a.button-blue.download_link").click()
#     driver.find_element(By.CSS_SELECTOR, "div[style*='float:left;']>a.button-blue.download_link").click()
#     WebDriverWait(driver, 30).until(EC.title_is("webdriver - Поиск в Google"))


# Поиск элемента с разделением сложного локатора на модули
def test_example(driver):
    driver.get("https://www.advanced-ip-scanner.com/ru/download/")
    # driver.find_element(By.CSS_SELECTOR, "a.button-blue.download_link li:last-child").click()
    # driver.find_element(By.CSS_SELECTOR, "a.button-blue.download_link").click()
    module = driver.find_element(By.CSS_SELECTOR, "div[style*='float:left;']")
    module.find_element(By.CSS_SELECTOR, "a.button-blue.download_link").click()
    WebDriverWait(driver, 30).until(EC.title_is("webdriver - Поиск в Google"))