from selenium.webdriver.common.by import By

from web.PO.page.basepage import BasePage
from web.PO.page.contact import Contact


class AddMember(BasePage):

    def add_member(self):
        # 点击添加头像
        self._driver.find_element(By.CSS_SELECTOR, '.member_edit_cover_avatar').click()
        self._driver.find_element(By.XPATH, '//*[@class="ww_fileInput js_file"]').send_keys(
            'C:\\Users\\Lin\\Pictures\\him.jpg')
        # 点击保存图片
        self._driver.find_element(By.CSS_SELECTOR, '[class="qui_btn ww_btn ww_btn_Blue js_save"]').click()
        # 添加姓名
        self._driver.find_element(By.CSS_SELECTOR, '#username').send_keys("丁海寅")
        self._driver.find_element(By.CSS_SELECTOR, '[name=english_name]').send_keys("him")
        self._driver.find_element(By.CSS_SELECTOR, '[name=acctid]').send_keys('DingHaiYin')
        # 单选按钮点击
        self._driver.find_element(By.CSS_SELECTOR, '[value="1"]').click()
        self._driver.find_element(By.ID, "memberAdd_mail").send_keys("DingHaiYin@qq.com")
        self._driver.find_element(By.CSS_SELECTOR, '#memberAdd_title').send_keys("男朋友")
        # 点击保存
        self._driver.find_element(By.XPATH, '//*[@class="qui_btn ww_btn js_btn_save"]').click()

        return Contact(self._driver)