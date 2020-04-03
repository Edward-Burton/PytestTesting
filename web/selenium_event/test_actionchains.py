from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click=self.driver.find_element_by_xpath("//input[@value='click me']")
        element_double_click=self.driver.find_element_by_xpath('//input[@value="dbl click me"]')
        element_rightclick=self.driver.find_element_by_xpath('//input[@value="right click me"]')
        action = ActionChains(self.driver)
        action.click(element_click)
        action.double_click(element_double_click)
        #右键点击鼠标操作
        action.context_click(element_rightclick)
        action.perform()

    @pytest.mark.skip
    def test_moveto_element(self):
        self.driver.get("https://www.baidu.com/")
        ele = self.driver.find_element_by_link_text("设置")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        
    @pytest.mark.skip
    def test_drag_drop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_element = self.driver.find_element_by_id("dragger")

        drop_element = self.driver.find_element_by_css_selector('.item')
        #drop_element = self.driver.find_element_by_xpath('/html/body/div[2]')

        action = ActionChains(self.driver)

        #action.drag_and_drop(drag_element,drop_element).perform()

        #release将鼠标抬起
        action.click_and_hold(drag_element).release(drop_element).perform()
        action.click_and_hold(drag_element).move_to_element(drop_element).release().perform()

    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element_by_xpath("/html/body/label[1]/input")
        ele.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        # Keys模拟键盘上的指令,如Ctrl+A,Ctrl+C,Ctrl+X等
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)

