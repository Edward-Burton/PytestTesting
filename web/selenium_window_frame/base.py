import os

from selenium import webdriver


class Base():
    def setup(self):
        self.driver = webdriver.Chrome()
        # browser = os.getenv("browser")
        # if browser == "firefox":
        #     self.driver = webdriver.Firefox()
        # elif browser == "headless":
        #     self.driver = webdriver.PhantomJS()
        # else:
        #     self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()