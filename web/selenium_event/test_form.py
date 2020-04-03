from selenium import webdriver


class TestForm():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def tear(self):
        self.driver.quit()

    def test_form(self):
        self.driver.get("")