import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome(desired_capabilities={'unexpectedAlertBehaviour': 'dismiss'})
    wd.implicitly_wait(10)  # Устанавливаем таймаут на отображение элемента на странице
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    wait = WebDriverWait(10)
    driver.get("http://www.google.com/")
    driver.find_element(By.NAME, "q").send_keys('webdriver')
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()
    alert.dismiss()
    alert = wait.until(EC.alert_is_present())
    driver.switch_to.frame()
    driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
    driver.switch_to.parent_frame(driver.find_element(By.TAG_NAME, "iframe"))
    driver.switch_to.default_content()
    driver.set_window_size(800, 600)
    driver.get_window_size()
    driver.set_window_position()
    driver.get_window_position()
    driver.fullscreen_window()
    driver.maximize_window()

    driver.close()
    if driver.find_element(By.NAME, "btnK"):
        return True  # Тест проходит
    # if driver.find_elements(By.XPATH, "//div(["):
    #     return False  # Тест возвращает InvalidSelectorException, т.к. локатор невалидный

# http://localhost/litecart/rubber-ducks-c-1/
# main_window = driver.current_window_handle
#
# old_windows = driver.window_handles
#
# link.click() # открывает новое окно
#
# # ожидание появления нового окна,
#
# # идентификатор которого отсутствует в списке oldWindows,
#
# # остаётся в качестве самостоятельного упражнения
#
# new_window = wait.until(there_is_window_other_than(old_windows))
#
# driver.switch_to_window(new_window)
#
# # ...
#
# driver.close()

