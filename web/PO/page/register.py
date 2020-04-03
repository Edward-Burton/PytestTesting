from selenium.webdriver.common.by import By

from web.PO.page.basepage import BasePage


class Register(BasePage):
    def register(self):
        self.find(By.ID,'corp_name').send_keys("hello")
        self.find(By.ID,'manager_name').send_keys("hello")
        return True
