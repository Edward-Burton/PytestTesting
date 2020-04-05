from selenium.webdriver.common.by import By

from web.PO.page.basepage import BasePage
from web.PO.page.register import Register


class Login(BasePage):
    def scan(self):
        pass

    def goto_register(self):
        self.find(By.CSS_SELECTOR,'.login_registerBar_link').click()
        return Register(self._driver)