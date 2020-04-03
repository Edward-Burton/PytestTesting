from time import sleep

from selenium import webdriver

from web.selenium_window_frame.base import Base


class TestWindows(Base):

    def test_window(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_link_text("登录").click()
        #打印当前窗口
        print(self.driver.current_window_handle)

        self.driver.find_element_by_link_text("立即注册").click()
        #打印当前窗口
        print(self.driver.current_window_handle)
        #获得窗口列表
        wind = self.driver.window_handles
        #切换到最近窗口
        self.driver.switch_to_window(wind[-1])
        #再次答应当前窗口
        print(self.driver.current_window_handle)

        #默认仍在第一个窗口，该窗口此处找不到该元素
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("username")

        #切换回第一个窗口
        self.driver.switch_to_window(wind[0])
        self.driver.find_element_by_xpath('//*[@title="用户名登录"]').click()
        self.driver.find_element_by_css_selector('[id="TANGRAM__PSP_10__userName"]').send_keys("username")
        self.driver.find_element_by_css_selector('#TANGRAM__PSP_10__password').send_keys("password")
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__submit"]').click()
        sleep(3)


