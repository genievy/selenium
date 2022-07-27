
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome(desired_capabilities={'unexpectedAlertBehaviour':'dismiss'})  # wd = webdriver.Firefox()
    # print(wd.capabilities)  # Выводим на печать все актуальные астройки браузера
    wd.implicitly_wait(10)  # Устанавливаем таймаут на отображение элемента на странице
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://www.google.com/")
    driver.find_element(By.CSS_SELECTOR, "q").send_keys("webdriver\n") # Эмуляция "Enter" <\n>
    # driver.find_element(By.NAME, "btnK").click()
    WebDriverWait(driver, 30).until(EC.title_is("webdriver - Поиск в Google"))

def test_example1(driver):
    driver.get("http://www.google.com/")
    element = driver.find_element(By.NAME, "q")
    # driver.refresh()  # После refresh() id элемента принимает другое значение
    element.send_keys("webdriver")
    driver.find_element(By.NAME, "btnK").click()
    WebDriverWait(driver, 30).until(EC.title_is("webdriver - Поиск в Google"))


def test_example2(driver):
    driver.get("http://www.google.com/")
    driver.find_element(By.CLASS_NAME, "ly0Ckb").click()
    driver.find_element(By.ID, "K68").click()
    driver.find_element(By.NAME, "btnK").click()
    WebDriverWait(driver, 30).until(EC.title_is("в - Поиск в Google"))