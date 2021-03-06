from selenium.webdriver.common.by import By

from web.PO.page.addmember import AddMember
from web.PO.page.basepage import BasePage
from web.PO.page.login import Login
from web.PO.page.register import Register


class Main(BasePage):

    #对父类变量进行改写，该变量的值仅在该类中起作用
    #_base_url = "https://work.weixin.qq.com/"
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"

    #进入注册页
    def goto_register(self):
        #点击注册按钮
        self.find(By.CSS_SELECTOR,'[class="index_head_info_pCDownloadBtn"]').click()
        #进入注册页的page
        return Register(self._driver)
    #进入登录页
    def goto_login(self):
        self.find(By.CSS_SELECTOR,'.index_top_operation_loginBtn').click()
        return Login(self._driver)

    def goto_add_member(self):
        self.find(By.CSS_SELECTOR,'.index_service_cnt_item').click()
        return AddMember(self._driver)

    def import_address(self):
        pass

    def member_join(self):
        pass