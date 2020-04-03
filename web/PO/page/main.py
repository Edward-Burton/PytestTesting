from selenium.webdriver.common.by import By

from web.PO.page.basepage import BasePage
from web.PO.page.login import Login
from web.PO.page.register import Register


class Main(BasePage):

    #对父类变量进行改写，该变量的值仅在该类中起作用
    _base_url = "https://work.weixin.qq.com/"

    def goto_register(self):
        self.find(By.CSS_SELECTOR,'[class="index_head_info_pCDownloadBtn"]').click()
        return Register(self._driver)

    def goto_login(self):
        self.find(By.CSS_SELECTOR,'.index_top_operation_loginBtn').click()
        return Login(self._driver)