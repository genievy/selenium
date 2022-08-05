
class BasePage:
    # url = 'http://localhost/litecart'
    # driver = webdriver.Chrome()
    def __int__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        return self.driver.get(self.url)