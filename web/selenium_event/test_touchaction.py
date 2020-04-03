import time

from selenium import webdriver
from selenium.webdriver import TouchActions


class TestTouchAction():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c',False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_touch_action_scrollbottom(self):
        self.driver.get("http://www.baidu.com")
        ele = self.driver.find_element_by_id("kw")
        ele_search = self.driver.find_element_by_id("su")

        ele.send_keys("selenium")
        action = TouchActions(self.driver)
        #点击操作加入队列
        action.tap(ele_search)
        #执行操作
        action.perform()
        #滚动操作
        action.scroll_from_element(ele_search,0,10000).perform()

